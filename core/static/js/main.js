// ===== Sidebar Toggle =====
const sidebar = document.getElementById('sidebar');
const toggleBtn = document.getElementById('toggleSidebar');

toggleBtn.addEventListener('click', () => {
  sidebar.classList.toggle('collapsed');
});

// ===== Settings Overlay =====
const settingsBtn = document.querySelector('.settings-btn');
const settingsOverlay = document.getElementById('settingsOverlay');
const closeSettings = document.getElementById('closeSettings');

settingsBtn.addEventListener('click', () => {
  settingsOverlay.classList.add('active');
});

closeSettings.addEventListener('click', () => {
  settingsOverlay.classList.remove('active');
});

// ===== Typing Animation for Search Bar =====
const typingElement = document.querySelector('.typing-animation');
const searchInput = document.querySelector('.search-bar');

const words = ["Django...", "Portfolio...", "E-Commerce..."];
let wordIndex = 0;
let charIndex = 0;
let currentWord = words[wordIndex];

function type() {
  if(charIndex < currentWord.length) {
    typingElement.textContent = currentWord.slice(0, charIndex + 1);
    charIndex++;
    setTimeout(type, 120);
  } else {
    setTimeout(erase, 1000);
  }
}

function erase() {
  if(charIndex > 0) {
    typingElement.textContent = currentWord.slice(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 60);
  } else {
    // Clear text immediately
    typingElement.textContent = '';
    wordIndex = (wordIndex + 1) % words.length;
    currentWord = words[wordIndex];
    setTimeout(type, 500);
  }
}

// Hide typing when input focused
searchInput.addEventListener('focus', () => {
  typingElement.style.display = 'none';
});

// Show typing when input blurred and empty
searchInput.addEventListener('blur', () => {
  if(searchInput.value === '') {
    typingElement.style.display = 'block';
  }
});

// Initialize typing animation
type();

