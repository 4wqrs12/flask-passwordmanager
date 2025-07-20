function displayTable() {
  const pswdTable = document.getElementById("password-table");
  pswdTable.style.display = "block";
}

function checkInputs() {
  const subject_input = document.getElementById("subject-input");
  const password_input = document.getElementById("password-input");
  const subject = subject_input.getAttribute("value");
  const password = password_input.getAttribute("value");

  if (subject.length > 0 && password.length > 0) {
    console.log("yes");
  } else {
    console.log("no");
  }
}