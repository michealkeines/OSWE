WebSockets:

	they are initiated over http and provide long-lived connections with asynchronus communication in both directions.

	bi directional, full duplex protocal

	var ws = new WebSocket("wss://site/test");

	wss protocal is over encrypted TLS, while ws is unencrypted

headers used in intial handshake:

	sec-websocket-version: 13 -> verion used
	sec-websocket-key: base64 key -> not for authentication just to make the handshake unique and not get cache overload
	concection: keep-alive, Upgrade
	updrade: websocket


