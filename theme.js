// Run before paint so saved themes carry across every page without a flash.
(() => {
  let saved;
  try { saved = localStorage.getItem('wpc-theme'); } catch (_) {}
  const theme = ['light', 'dark'].includes(saved) ? saved : (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.dataset.theme = theme;
})();
