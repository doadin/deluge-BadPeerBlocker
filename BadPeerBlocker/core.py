import deluge.component as component
from deluge.plugins.pluginbase import CorePluginBase

class Core(CorePluginBase):
    def enable(self):
        self.event_manager = component.get("EventManager")
        self.event_manager.register_event_handler(
            "PeerAddedEvent", self.on_peer_added
        )
    
    def disable(self):
        self.event_manager.deregister_event_handler(
            "PeerAddedEvent", self.on_peer_added
        )

    def on_peer_added(self, torrent_id, peer_info):
        """
        peer_info.client is the client string (e.g., 'qBittorrent', 'Unknown', etc.)
        peer_info.ip is the peer IP address.
        """
        client = getattr(peer_info, "client", "")
        ip = getattr(peer_info, "ip", "")

        if client.lower() == "unknown":
            ip_filter = component.get("IPFilter")
            ip_filter.block_ip_range(ip, ip)

            print(f"[BadPeerBlocker] Blocked Unknown client: {ip}")