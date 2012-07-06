import socket
import struct


def parse_reply(reply):
    info = {}

    _, rest = reply[:4], reply[4:] # Strip 4-byte prefix

    # Type (byte)
    info['type'], rest = struct.unpack('B', rest[0])[0], rest[1:]

    # Version (byte)
    info['version'], rest = struct.unpack('B', rest[0])[0], rest[1:]

    # Server name (string)
    end = rest.index('\0')
    info['server_name'], rest = rest[:end], rest[end + 1:]

    # Map (string)
    end = rest.index('\0')
    info['current_map'], rest = rest[:end], rest[end + 1:]

    # Game directory (string)
    end = rest.index('\0')
    info['game_directory'], rest = rest[:end], rest[end + 1:]

    # Game description (string)
    end = rest.index('\0')
    info['game_description'], rest = rest[:end], rest[end + 1:]

    # App ID (short)
    info['app_id'], rest = struct.unpack('H', rest[:2])[0], rest[2:]

    # Number of players (byte)
    info['number_of_players'], rest = struct.unpack('B', rest[0])[0], rest[1:]

    # Max players (byte)
    info['max_players'], rest = struct.unpack('B', rest[0])[0], rest[1:]

    # Number of bots (byte)
    info['number_of_bots'], rest = struct.unpack('B', rest[0])[0], rest[1:]

    # Dedicated (byte)
    dedicated_raw, rest = struct.unpack('c', rest[0])[0], rest[1:]
    if dedicated_raw == 'l':
        info['dedicated'] = 'listen'
    elif dedicated_raw == 'd':
        info['dedicated'] = 'dedicated'
    elif dedicated_raw == 'p':
        info['dedicated'] = 'SourceTV'

    # OS (byte)
    os_raw, rest = struct.unpack('c', rest[0])[0], rest[1:]
    if os_raw == 'l':
        info['os'] = 'Linux'
    elif os_raw == 'w':
        info['os'] = 'Windows'

    # Password (byte)
    info['password'], rest = struct.unpack('?', rest[0])[0], rest[1:]

    # Secure (byte)
    info['secure'], rest = struct.unpack('?', rest[0])[0], rest[1:]

    # Game version (string)
    end = rest.index('\0')
    info['game_version'], rest = rest[:end], rest[end + 1:]

    return info


def server_info(addr, port):
    message = struct.pack("i1s19sx", -1, "T", "Source Engine Query")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (addr, port))

    reply = sock.recv(1400)
    return parse_reply(reply)


if __name__ == '__main__':
    print server_info("tf2.patricklucas.net", 27015)
