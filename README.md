BadPeerBlocker
Automatically blocks peers in Deluge whose client name is reported as “Unknown.”
This plugin hooks into Deluge’s peer‑connection events and uses the built‑in IP filter to immediately reject and blacklist these peers.
Features
• 	Monitors all incoming peer connections
• 	Detects peers whose client string is 
• 	Instantly blocks their IP using Deluge’s IPFilter
• 	Prevents future connections from the same address
• 	Lightweight, core‑only plugin with no UI components
Why block “Unknown” clients?
Deluge often receives malformed or non‑BitTorrent traffic—especially from scanners, bots, and misbehaving peers. These connections frequently appear with a client name of  and provide no useful handshake data. BadPeerBlocker removes this noise automatically.
Installation
1. 	Build the plugin:

2. 	Copy the generated  file from the  directory into your Deluge plugin folder:
• 	Linux: 
• 	Windows: 
• 	macOS: 
3. 	Open Deluge → Preferences → Plugins
4. 	Enable BadPeerBlocker
Requirements
• 	Deluge 2.x
• 	Python 3.x
How it works
BadPeerBlocker listens for Deluge’s .
When a peer connects, the plugin inspects:
• 	 → the reported client name
• 	 → the peer’s IP address
If the client name matches  (case‑insensitive), the plugin:
1. 	Adds the IP to Deluge’s IPFilter
2. 	Disconnects the peer
3. 	Logs the block to the console

Notes
• 	This plugin only blocks peers with the exact client name .
• 	Additional client names or patterns can be added easily in .
• 	No UI components are included, keeping the plugin lightweight and daemon‑friendly.
