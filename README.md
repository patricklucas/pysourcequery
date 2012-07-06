pysourcequery
=============

Library for communicating with Source Engine games via UDP

Example
-------

```python
import pysourcequery

print pysourcequery.server_info('tf2.patricklucas.net', 27015)

{'app_id': 440,
 'current_map': 'cp_steel',
 'dedicated': 'dedicated',
 'game_description': 'Team Fortress',
 'game_directory': 'tf',
 'game_version': '1.2.1.7',
 'max_players': 24,
 'number_of_bots': 0,
 'number_of_players': 0,
 'os': 'Linux',
 'password': False,
 'secure': True,
 'server_name': 'Test Sandvich Plz Ignore - 24/7 Steel',
 'type': 73,
 'version': 17}
```

Compatibility
-------------

This is a very rough draft. Only speaks the base Source Engine protocol.
