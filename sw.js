const CACHE_NAME = 'box-breathing-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/app.py',
  '/assets/style.css',
  '/assets/tone.mp3'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)));
});
