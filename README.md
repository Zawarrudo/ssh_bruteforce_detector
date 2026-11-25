# ssh_bruteforce_detector

A lightweight Python script that parses SSH authentication logs to extract login activity and detect repeated failed attempts.

## Overview

This project is in an early development stage. It currently parses SSH log entries to extract source IP, username, authentication status, and timestamp, serving as the foundation for brute-force detection.

## Requirements

- Python 3.x

## Roadmap

- [x] Parse SSH logs from a local file and extract IP, user, status, and timestamp
- [ ] Add Perse security aginst malicius user name
- [ ] Count failed login attempts per IP and flag threshold breaches
- [ ] Add time-window analysis (e.g., X failed attempts within Y seconds)
