'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const sets = {upper:'ABCDEFGHIJKLMNOPQRSTUVWXYZ',lower:'abcdefghijklmnopqrstuvwxyz',numbers:'0123456789',symbols:'!@#$%^&*()-_=+[]{}:,.?'};
  let revision = 0;
  function clear(message) {
    revision++; $('password').value = ''; $('copy').disabled = true; $('clear').disabled = true; $('notice').textContent = message;
  }
  function generate() {
    clear('');
    const length = Number($('length').value);
    if (!Number.isInteger(length) || length < 8 || length > 128) { $('notice').textContent = 'Choose a whole-number length from 8 to 128.'; return; }
    const groups = Object.entries(sets).filter(([id]) => $(id).checked).map(([,chars]) => chars);
    if (!groups.length) { $('notice').textContent = 'Select at least one character type.'; return; }
    const alphabet = groups.join(''), limit = Math.floor(256 / alphabet.length) * alphabet.length;
    try {
      let password;
      do {
        password = '';
        while (password.length < length) {
          const bytes = new Uint8Array(256);
          crypto.getRandomValues(bytes);
          for (const byte of bytes) {
            if (byte < limit) password += alphabet[byte % alphabet.length];
            if (password.length === length) break;
          }
        }
      } while (!groups.every(group => [...password].some(char => group.includes(char))));
      $('password').value = password; $('copy').disabled = false; $('clear').disabled = false;
      $('notice').textContent = `${length}-character password generated.`;
    } catch (_) { clear('Secure random generation is unavailable in this browser. Try an updated browser.'); }
  }
  $('settings').addEventListener('submit', e => {e.preventDefault(); generate();});
  $('settings').addEventListener('input', () => clear('Settings changed. Generate a new password.'));
  $('clear').addEventListener('click', () => clear('Password cleared from this page. Any clipboard copy is unchanged.'));
  $('copy').addEventListener('click', async () => {
    const password = $('password').value, current = revision;
    if (!password) return;
    try {
      await navigator.clipboard.writeText(password);
      if (revision === current) $('notice').textContent = 'Password copied.';
    } catch (_) {
      if (revision !== current) return;
      $('password').focus(); $('password').select();
      $('notice').textContent = 'Automatic copy is unavailable. Copy the selected password manually.';
    }
  });
  generate();
})();
