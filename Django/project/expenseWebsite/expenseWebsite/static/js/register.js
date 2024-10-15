const usernameField = document.querySelector('#usernameField');
const emailField = document.querySelector('#emailField');
const passwordField = document.querySelector('#passwordField');

const feedBackArea = document.querySelector('.invalid_feedback');
const emailFeedBackArea = document.querySelector('.emailFeedBackArea');
const showPasswordToggle = document.querySelector(".showPasswordToggle")

// USERNAME
usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;

  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {
      fetch("/authentication/username_validation", {
          body: JSON.stringify({ username: usernameVal }),
          method: "POST",
      })
      .then(res => res.json())
      .then((data) => {     
        if (data.username_error) {
            usernameField.classList.add("is-invalid");
            feedBackArea.style.display = "block";
            feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
            submitBtn.disabled = true;
        }
      });
  }
});

// EMAIL
emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;

  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
      fetch("/authentication/email_validation", {
          body: JSON.stringify({ email: emailVal }),
          method: "POST",
      })
      .then(res => res.json())
      .then((data) => {     
        if (data.email_error) {
            emailField.classList.add("is-invalid");
            emailFeedBackArea.style.display = "block";
            emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
            submitBtn.disabled = true;
        }
      });
  }
});