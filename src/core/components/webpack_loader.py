from core.settings import BASE_DIR, DEBUG

WEBPACK_LOADER = {
  'DEFAULT': {
    'CACHE': not DEBUG,
    'STATS_FILE': BASE_DIR / '../frontend/webpack-stats-production.json',
    'POLL_INTERVAL': 0.1,
    'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
  },
}
