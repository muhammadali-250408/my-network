# my-network

A small, hobby networking project implemented in Python that demonstrates fundamentals of TCP socket programming, a custom HTTP-like transfer, and a minimal client that receives and renders HTML. This repository currently contains the client component; the DNS and HTTP server components are a work in progress.

This project was built as a learning exercise to explore how basic networking protocols operate. It is not production-ready software — no security, privacy, or hardening measures are implemented. I built this project to practice systems-level programming and networking concepts prior to university and internship applications.

Table of contents
- Project summary
- Why I built it
- What I learned / skills demonstrated
- Repository structure
- Prerequisites
- How to run the client
- Example interaction
- Design notes & implementation details
- Limitations and security warnings
- Suggested interview talking points
- Future work
- Contributing
- License & contact

Project summary
This project demonstrates:
- Raw TCP socket programming in Python
- A simple, application-level protocol for requesting and transferring HTML (marker-based)
- Client-side file I/O to save received HTML for viewing
- Design considerations around framing, buffering, and protocol markers

Why I built it
- To gain hands-on experience with sockets, networking primitives, and protocol design
- To better understand how DNS resolution and HTTP transfers can be implemented at a low level
- As a compact, explainable project to discuss in technical interviews

What I learned / skills demonstrated
- Python network programming using the socket standard library
- Basic protocol design and simple message framing techniques
- File I/O and error handling in I/O-bound programs
- Debugging networked programs and iterative development
- Communicating trade-offs and limitations (important in professional settings)

Repository structure
- CLIENT.py — minimal client that connects to a server, requests a URL, and writes HTML to `WEBSITE.html`
- README.md — this file
- Version 0.1/ — planned area for server and DNS components (work in progress)

Prerequisites
- Python 3.8+ (or any modern Python 3 runtime)
- No external packages required — standard library only

How to run (client)
1. Clone the repository:
   git clone https://github.com/muhammadali-250408/my-network.git
   cd my-network

2. Edit CLIENT.py:
   - Replace the placeholder IP address at the top of the file (line where connect() is called) with the server IPv4 address you will connect to.
   - Confirm the port is set to the server port (default in the client: 4000).

3. Run the client:
   python3 CLIENT.py

4. Interaction:
   - The client receives an initial prompt from the server.
   - It sends a "USER" handshake then accepts a URL (or path) as input.
   - If the server replies with the `HTMLINCOMING` marker, the client will increase its receive buffer and append the next payload to `WEBSITE.html`.

Example interaction (high-level)
- Client connects → server greets.
- Client sends: USER
- Client enters: example.mali/index.html
- Server replies: HTMLINCOMING
- Client receives the HTML payload and writes/updates `WEBSITE.html`.

Design notes & implementation details
- Protocol markers: The implementation uses short text markers such as `HTMLINCOMING` to indicate the start of a large HTML payload. This is a simple, explicit signaling approach appropriate for demonstration code.
- Buffer strategy: The client uses a small default receive buffer for short text messages and switches to a larger buffer when a bulk HTML transfer is signaled. This is a teaching simplification; production systems use explicit framing (length-prefix or chunked transfer) and robust reassembly.
- File I/O: HTML is appended to `WEBSITE.html`. For a real browser experience, the client would parse and fetch assets and overwrite or manage files safely.

Limitations and security warnings (important)
- This is a hobby/educational project only.
- No encryption (no TLS/SSL), no authentication, no input validation.
- Not safe to use on public/untrusted networks or with sensitive data.
- The transfer framing is simplistic and may cause partial reads or broken transfers for larger or streamed content.
- The server and DNS components are incomplete — do not attempt to deploy this as a public service.

Suggested interview talking points
- Your role and intent: "I built this as a hobby project to understand sockets and protocol design before university."
- Technical highlights: raw sockets, simple marker-based protocol, buffer management, file writes, debugging strategies.
- Trade-offs: explain why marker-based signaling was chosen for demonstration and how you would replace it for production (length-prefixing, chunking, checksums, TLS).
- Future improvements: testing, framing, TLS, authentication, modular server, and HTML parsing/rendering.

Future work
- Release the HTTP server and custom DNS components
- Replace buffer-size heuristics with explicit framing (length-prefix or chunked encoding)
- Add tests and integration scripts
- Add optional TLS, authentication, and input validation
- Improve the client into a small renderer that can request and display assets (images/styles) safely in an isolated environment

Contributing
- This repository is a personal learning project. If you'd like to contribute:
  - Fork the repo, add changes with tests or example usage, and open a pull request with a clear description.
  - Focus areas: server/DNS implementation, robust transfer framing, unit tests, and documentation.
