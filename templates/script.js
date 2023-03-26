const form = document.querySelector('.login-form');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const username = form.username.value;
  const password = form.password.value;
  if (username === 'myusername' && password === 'mypassword') {
    alert('Login successful!');
  } else {
    alert('Incorrect username or password!');
  }
});