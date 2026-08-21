# my-network

A Python networking project exploring application-layer communication built on TCP sockets. The project implements a minimal client that connects to a server, exchanges messages using a simple custom protocol, receives HTML content, and saves it locally. This is an educational project demonstrating networking fundamentals and protocol design principles.

The project was built as a learning exercise to explore how basic networking protocols and client/server communication operate. The DNS and HTTP server components are incomplete. The codebase prioritizes clarity and correctness over production hardening.

## Table of contents

- [Project summary](#project-summary)
- [Why I built it](#why-i-built-it)
- [What I learned / skills demonstrated](#what-i-learned--skills-demonstrated)
- [Repository structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [How to run the client](#how-to-run-the-client)
- [Example interaction](#example-interaction)
- [Design notes & implementation details](#design-notes--implementation-details)
- [Limitations and security considerations](#limitations-and-security-considerations)
- [Future work](#future-work)
- [Contributing](#contributing)
- [License & contact](#license--contact)

## Project summary

This project demonstrates:

- TCP socket programming in Python using the standard library
- Client/server communication via a custom application-level protocol
- Message framing using text markers to delimit protocol transitions
- Buffer management strategies for variable-length payloads
- Receiving and writing HTML data to local files
- Error handling in I/O-bound network programs

## Why I built it

To gain practical experience with:

- Networking primitives and socket programming
- Application-layer protocol design and message framing
- Client/server architecture and data transfer
- Understanding what happens below high-level web abstractions (HTTP libraries, browsers)

## What I learned / skills demonstrated

- Python socket programming (`socket` module)
- TCP client implementation and server connectivity
- Application-layer protocol design and message framing
- Buffer management for variable-length data transfers
- File I/O and error handling in networked contexts
- Debugging and testing networked applications
- Understanding trade-offs in protocol design choices

## Repository structure

- `CLIENT.py` — minimal client that connects to a server, requests a URL or path, receives HTML data, and writes it to `WEBSITE.html`
- `README.md` — this file
- `Version 0.1/` — planned area for server and DNS components (in progress)

## Prerequisites

- Python 3.8+ (or any modern Python 3 runtime)
- No external packages required — standard library only

## How to run the client

1. Clone the repository:
   ```bash
   git clone https://github.com/muhammadali-250408/my-network.git
   cd my-network
   ```

2. Edit `CLIENT.py`:
   - Replace the placeholder IP address at the top of the file (line where `connect()` is called) with the server IPv4 address.
   - Confirm the port matches the server port (default: 4000).

3. Run the client:
   ```bash
   python3 CLIENT.py
   ```

4. Interaction:
   - The client connects to the server and receives an initial greeting.
   - It sends a `USER` handshake, then accepts a URL or path as input.
   - If the server replies with the `HTMLINCOMING` marker, the client increases its receive buffer and reads the HTML payload.
   - The HTML is written to (or appended to) `WEBSITE.html`.

## Example interaction

```
1. Client connects to server via TCP
2. Server sends greeting message
3. Client sends USER handshake
4. Client sends URL/path request
5. Server sends HTMLINCOMING marker
6. Server sends HTML payload
7. Client writes HTML to WEBSITE.html
```

## Design notes & implementation details

**Protocol markers:** The implementation uses short text markers (e.g., `HTMLINCOMING`) to signal state transitions and the start of bulk data transfers. This is a simple, explicit signaling approach suitable for demonstration. It works because TCP provides a reliable byte stream; however, this approach does not formally separate application-level message boundaries, which can lead to partial or fragmented reads if buffers are too small.

**Buffer strategy:** The client uses a small default receive buffer for short text messages and switches to a larger buffer when the `HTMLINCOMING` marker signals an incoming HTML transfer. This is a practical simplification for a learning project. Production systems would use explicit framing (length-prefixes, chunked encoding, or similar) to reliably determine when one message ends and another begins, independent of buffer sizes.

**File I/O:** Received HTML is written to `WEBSITE.html`. For a complete browser experience, the client would need to parse the HTML, fetch referenced assets (images, stylesheets), and manage file output safely. The current implementation prioritizes simplicity.

## Limitations and security considerations

- This is an educational project, not production software. It is not suitable for public or untrusted networks.
- No encryption (TLS/SSL), authentication, or input validation are implemented.
- The protocol framing is simplified and may not handle partial reads or large transfers reliably without explicit reassembly logic.
- The server and DNS components are incomplete and should not be deployed as a public service.

## Future work

- Complete the HTTP server and custom DNS resolver components
- Replace buffer-size heuristics with explicit framing (length-prefix or chunked encoding)
- Add unit tests and integration test scripts
- Improve error handling and graceful connection closure
- Add optional TLS/encryption and basic authentication
- Extend the client to request and safely cache referenced assets (images, stylesheets)

## Contributing

This repository is a personal learning project. If you'd like to contribute:

- Fork the repo, add changes with tests or example usage, and open a pull request with a clear description.
- Focus areas: server/DNS implementation, robust transfer framing, unit tests, and documentation.

## License & contact

This project is provided as-is for educational purposes. No formal licence is currently assigned. For questions or feedback, please open an issue or contact the author directly.
