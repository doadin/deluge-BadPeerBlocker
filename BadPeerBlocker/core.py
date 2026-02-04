import deluge.component as component
from deluge.plugins.pluginbase import CorePluginBase

class Core(CorePluginBase):
    def enable(self):
        self.event_manager = component.get("EventManager")
        self.torrent_manager = component.get("TorrentManager")

        # In-memory blacklist of IPs we’ve already blocked
        self.blocked_ips = set()

        # Subscribe to peer-added events
        self.event_manager.register_event_handler(
            "PeerAddedEvent", self.on_peer_added
        )

        print("[BadPeerBlocker] Enabled")

    def disable(self):
        self.event_manager.deregister_event_handler(
            "PeerAddedEvent", self.on_peer_added
        )
        print("[BadPeerBlocker] Disabled")

    def on_peer_added(self, torrent_id, peer_info):
        """
        Called whenever a new peer connects.
        peer_info.client -> client name string
        peer_info.ip     -> peer IP address
        """
        client = getattr(peer_info, "client", "")
        ip = getattr(peer_info, "ip", "")

        # If we've already blocked this IP, disconnect immediately
        if ip in self.blocked_ips:
            self._disconnect_peer(torrent_id, ip)
            return

        # Block peers with Unknown client name
        if client.lower() == "unknown":
            print(f"[BadPeerBlocker] Blocking Unknown client: {ip}")
            self.blocked_ips.add(ip)
            self._disconnect_peer(torrent_id, ip)

    def _disconnect_peer(self, torrent_id, ip):
        """Disconnect a peer cleanly using Deluge 2.x API."""
        try:
            torrent = self.torrent_manager.torrents.get(torrent_id)
            if torrent:
                torrent.remove_peer(ip)
                print(f"[BadPeerBlocker] Disconnected peer {ip}")
        except Exception as e:
            print(f"[BadPeerBlocker] Failed to disconnect {ip}: {e}")