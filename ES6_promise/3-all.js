import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]).then(([newPhoto, newUser]) => {
    console.log(`${newPhoto.body} ${newUser.firstName} ${newUser.lastName}`);
  })
    .catch(() => {
      console.log('Signup system offline');
    });
}
