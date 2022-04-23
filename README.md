# adagio

This is an extremely tiny `async`/`await` library for Python. "Groups" are
inspired by Trio's nurseries.

This is a project of fifteen minutes, without reading anything about how async
stuff works, so it's probably not working correctly. Also, the only 'true'
awaitable is `adagio.sleep()`, so you can't really do much with this.

The usual disclaimer applies: Don't use anywhere ever.
