import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promiseOne = signUpUser(firstName, lastName);
  const promiseTwo = uploadPhoto(fileName);

  const display = await Promise.allSettled([promiseOne, promiseTwo]);

  return display.map((display) => ({
    status: display.status,
    value: display.value || display.reason,
  }));
}
