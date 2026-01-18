// Game frontend logic: create session -> create game -> handle guesses (click + keyboard)
// Relies on helpers from app.js: apiRequest, getCurrentUser

let _sessionId = null;
let _gameId = null;
let _locked = false; // when game finishes

function renderPattern(patternStr) {
  // patternStr uses '*' for hidden and letters for revealed
  const parts = Array.from(patternStr).map(ch => ch === '*' ? '_' : ch.toUpperCase());
  return parts.join(' ');
}

function setMessage(text, isError = false) {
  const el = document.getElementById('game-message');
  el.textContent = text || '';
  el.style.color = isError ? 'var(--danger)' : 'inherit';
}

function updateUi(game) {
  // Ensure pattern length matches reported length (if available) and fix if necessary
  let pattern = game.pattern || '';
  if (game.length && pattern.length !== game.length) {
    console.warn(`Pattern length ${pattern.length} != reported length ${game.length}; adjusting pattern.`);
    if (pattern.length < game.length) pattern = pattern.padEnd(game.length, '*');
    else pattern = pattern.slice(0, game.length);
  }
  document.getElementById('word-pattern').textContent = renderPattern(pattern);
  document.getElementById('misses-count').textContent = String(game.remaining_misses);
  document.getElementById('wrong-list').textContent = game.wrong_letters.map(l => l.toUpperCase()).join(' ') || '-';

  // Update flower progression
  updateFlower(game);

  if (game.status === 'WON') {
    setMessage('You won! 🎉');
    _locked = true;
    disableAllKeys();
  } else if (game.status === 'LOST') {
    setMessage(`You lost. The word was: ${game.revealed_word || '(hidden)'}`);
    _locked = true;
    disableAllKeys();
  }
}

function updateFlower(game) {
  const flowerImg = document.getElementById('flower-img');
  if (!flowerImg) return;

  // Calculate progress based on revealed letters
  const pattern = game.pattern || '';
  const totalLetters = pattern.length;
  const revealedLetters = pattern.split('').filter(ch => ch !== '*').length;
  const progressPercent = totalLetters > 0 ? (revealedLetters / totalLetters) * 100 : 0;

  if (game.status === 'LOST') {
    // Wilted flower when lost
    flowerImg.src = '../assets/wilted_flower.png';
  } else if (game.status === 'WON') {
    // Full flower when won
    flowerImg.src = '../assets/full_flower.png';
  } else if (progressPercent >= 50) {
    // Full flower when more than 50% revealed
    flowerImg.src = '../assets/full_flower.png';
  } else if (progressPercent >= 20) {
    // Leaves when some letters are revealed
    flowerImg.src = '../assets/pot_w_leaves.png';
  } else {
    // Start with soil
    flowerImg.src = '../assets/pot_w_soil.png';
  }
}

function disableAllKeys() {
  document.querySelectorAll('.grid_letters button').forEach(b => b.disabled = true);
}

function enableKey(letter) {
  const el = document.getElementById('key-' + letter);
  if (el) el.disabled = false;
}

async function doGuess(letter) {
  if (_locked) return;
  letter = letter.toLowerCase();
  const btn = document.getElementById('key-' + letter);
  if (btn) btn.disabled = true;

  try {
    const game = await apiRequest(`/sessions/${_sessionId}/games/${_gameId}/guess`, 'POST', { letter });
    updateUi(game);
  
    (game.guessed_letters || []).forEach(l => {

      const el = document.getElementById('key-' + l.toLowerCase());

      if (el) el.disabled = true;

    });
  } catch (err) {
    // show server message
    setMessage(err.message || 'Guess failed', true);
  }
}

function attachButtonHandlers() {
  document.querySelectorAll('.grid_letters button').forEach(b => {
    b.addEventListener('click', () => {
      if (b.disabled) return;
      const id = b.id; // key-a
      const letter = id.split('-')[1];
      doGuess(letter);
    });
  });
}

function keyboardHandler(e) {
  if (_locked) return;
  const key = e.key.toLowerCase();
  if (key.length === 1 && key >= 'a' && key <= 'z') {
    const btn = document.getElementById('key-' + key);
    if (btn && !btn.disabled) {
      doGuess(key);
    }
  }
}

async function createSession() {
  // Choose a default dictionary id (1) and configuration; change if your DB expects another id
  const payload = {
    num_games: 1,
    dictionary_id: 1,
    difficulty: 'normal',
    language: 'en',
    max_misses: 6,
    allow_word_guess: false,
    seed: null
  };
  return apiRequest('/sessions', 'POST', payload);
}

async function createGame(sessionId) {
  return apiRequest(`/sessions/${sessionId}/games`, 'POST', null);
}

async function init() {
  // NOTE: MUST BE LOGGED IN - original behavior commented out to allow game to run without login.
  /*
  try {
    await getCurrentUser();
  } catch (err) {
    window.location.href = 'login.html';
    return;
  }
  */

  attachButtonHandlers();
  window.addEventListener('keydown', keyboardHandler);

  setMessage('Starting game...');

  try {
    const session = await createSession();
    _sessionId = session.session_id;
  } catch (err) {
    setMessage('Failed to create session. Ask admin to enable dictionaries or check server. ' + (err.message || ''), true);
    return;
  }

  try {
    const game = await createGame(_sessionId);
    _gameId = game.game_id;
    updateUi(game);
    // disable letters already guessed
    (game.guessed_letters || []).forEach(l => {
      const el = document.getElementById('key-' + l.toLowerCase());
      if (el) el.disabled = true;
    });
    setMessage('Good luck! Press letters or use the keyboard.');
  } catch (err) {
    setMessage('Failed to create game. ' + (err.message || ''), true);
  }
}

// Initialize when the DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}