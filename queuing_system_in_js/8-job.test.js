const createPushNotificationsJobs = require('./8-job')
const kue = require('kue');
const queue = kue.createQueue();
const { expect } = require('chai');
const assert = require('assert');
const sinon = require('sinon');

describe("createPushNotificationsJobs", () => {
    const twoJobs = [
        {
          phoneNumber: '9187775555',
          message: 'This is the code 1234 to verify your account',
        },
        {
          phoneNumber: '4057775555',
          message: 'This is the code 4321 to verify your account',
        },
    ];

    let que;
    let conSpy;

    beforeEach(function() {
        que = kue.createQueue();
        que.testMode.enter();
        conSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        que.testMode.clear();
        que.testMode.exit();
        conSpy.restore();
    });

    it('display a error message if jobs is not an array', function() {
        assert.throws(() => createPushNotificationsJobs('!array', que), new Error('Jobs is not an array'));
      });

    it('Job 1 complete', function(done) {
        createPushNotificationsJobs(twoJobs, que);
        const job = que.testMode.twoJobs[0];

        job.on('complete', () => {
          assert(conSpy.calledWith(`Notification job ${job.id} completed`));
          done();
        });
        job.emit('complete');

    });

    it('create two new jobs to the queue', function() {
        const saveSpy = sinon.spy(kue.Job.prototype, 'save');
        createPushNotificationsJobs(twoJobs, que);
        assert.strictEqual(que.testMode.twoJobs.length, 2);
        assert(saveSpy.calledTwice);
        saveSpy.restore();
    });

	it("check error thrown from job array being Number", () => {
		expect(() => {
			createPushNotificationsJobs(1, queue);
		}).to.throw(Error, 'Jobs is not an array');
	});

	it("check error thrown from job array being String", () => {
		expect(() => {
			createPushNotificationsJobs("string", queue);
		}).to.throw(Error, 'Jobs is not an array');
	});

	it("check error thrown from job array being Object", () => {
		expect(() => {
			createPushNotificationsJobs({}, queue);
		}).to.throw(Error, 'Jobs is not an array');
	});

	it("check what is thrown if job is array", () => {
		expect(() => {
			createPushNotificationsJobs([], queue);
		}).to.not.throw(Error, 'Jobs is not an array');
	});
})