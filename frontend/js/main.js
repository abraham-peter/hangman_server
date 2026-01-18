// main.js - placeholder for menu behaviours
console.log('main.js loaded');
// You can add menu interactivity here (sounds, help popup, etc.)

function closeWindow() {
  // Attempt to close the window. Note: most browsers only allow closing windows opened by script.
  window.close();
  // Fallback message when automatic close isn't permitted.
  setTimeout(() => {
    if (!window.closed) {
      alert('This window cannot be closed automatically. Please close the tab or window manually.');
    }
  }, 200);
}

document.addEventListener('DOMContentLoaded', () => {
  const exitBtn = document.getElementById('exit-btn');
  if (exitBtn) exitBtn.addEventListener('click', closeWindow);
});