import { createClient } from 'redis';

const redisClient = createClient();
const redis = require('redis');
const { promisify } = require('util');
const asyncClient = promisify(redisClient.get).bind(redisClient);

redisClient.on('Connected', () =>
    console.log('Redis client connected to the server'));
redisClient.on('error', (err) =>
    console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => {
    redisClient.set(schoolName, value, redis.print);
};
const displaySchoolValue = async(schoolName) => {
    const value = await asyncClient(schoolName);
    console.log(value);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');