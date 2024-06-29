# Information
  Simple RCON Client For minecraft
  Works on 1.21 and under
  Depends on https://pypi.org/project/aio-mc-rcon/](aiomcrcon) for networking
# Useage
  ServerPass (Str): Server's Rcon password
  ServerPort (Int): Server's Rcon port (must be forwarded on non local servers)
  ServerTSNIP (Str): Originally intended for Tailscale, but can be used if you wish to route through a VPN or VLAN. Ignored If blank.
  ServerIP (Str): Server's public or local ip, Localhost works or 192.168.X.XXX.
