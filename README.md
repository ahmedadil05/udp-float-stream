# udp-float-stream

# Project Title

A brief description of what this project does and who it's for

UDP Float Stream

A minimal real-time networking project that streams binary float data over UDP, with sequence numbers, timestamps, packet-loss detection, and latency measurement.

This project is designed as a learning lab for understanding how real-time systems behave under UDP: fast, unordered, unreliable — and honest.

Why this project exists

TCP guarantees reliability but adds latency and head-of-line blocking.
Real-time systems (video streaming, games, XR, telemetry) often choose UDP and then rebuild only the guarantees they actually need.

This repository explores that idea step by step:

Binary protocols instead of strings

Explicit packet loss detection

One-way latency measurement

Running over real networks (not just localhost)

Features

Binary UDP protocol using struct

Sequence numbers to detect dropped packets

Timestamps to measure one-way latency

Works on localhost and over real networks (Tailscale)

Clean protocol separation (protocol.py)

Project Structure
udp-float-stream/
├── protocol.py   # Binary packet definition (single source of truth)
├── sender.py     # Sends UDP packets (sequence + timestamp + float)
├── receiver.py   # Receives packets, detects loss, measures latency
├── README.md
└── LICENSE

Packet Format

Each UDP packet is 16 bytes:

[ sequence_number | timestamp | value ]
[   uint32 (4)    | float64   | float32 ]


sequence_number: detects packet loss and reordering

timestamp: sender time (time.time())

value: streamed float payload

All fields use network byte order (big-endian).

Requirements

Python 3.9+

No external dependencies (optional: matplotlib for visualization)

Running on Localhost
1. Start the receiver
python receiver.py

2. Start the sender (in another terminal)
python sender.py


You should see:

sequence numbers

latency in milliseconds

packet loss messages (if any)

Stop either program with:

Ctrl + C

Running over a Real Network (Tailscale)

Localhost hides reality. To test real latency and packet loss:

Install Tailscale on both machines

Log in on both

Get the receiver’s Tailscale IP:

tailscale ip


Update sender.py:

addr = ("TAILSCALE_IP_HERE", 9999)


Run receiver first, then sender

Now the data flows over an encrypted real network.

What this project demonstrates

Why UDP does not “end” — silence is the only signal

How packet loss is detected, not prevented

How latency and jitter emerge naturally

Why real-time systems rebuild reliability selectively

The difference between local testing and real networks

Possible Extensions

Jitter buffer

Packet reordering

Heartbeat / control packets (STOP, PAUSE)

TCP control channel + UDP data channel

Live latency visualization

Streaming transforms for 3D / XR systems

License

MIT License — use, modify, break, rebuild.