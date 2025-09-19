async function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;
  const errorBox = document.getElementById("error");
  errorBox.style.display = "none";

  try {
    await auth.signInWithEmailAndPassword(email, password);
    // Success → go to admin page
    window.location.href = "admin.html";
  } catch (err) {
    errorBox.textContent = err.message;
    errorBox.style.display = "block";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("loginForm").addEventListener("submit", handleLogin);

  // If already logged in, skip login page
  auth.onAuthStateChanged((user) => {
    if (user) window.location.href = "admin.html";
  });
});
