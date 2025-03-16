This Python script is designed to monitor and prevent memory leaks in specific processes. It continuously checks the memory usage of a target process and terminates it if the memory usage exceeds a predefined limit. This tool is particularly useful for managing long-running processes that may have memory leaks, ensuring they do not consume excessive system resources.

Features
Memory Leak Prevention: Automatically terminates processes that exceed a specified memory limit.

Process Name Matching: Monitors processes by their name.

Configurable Memory Limit: Set a memory threshold in megabytes (MB) for the process.

Periodic Checks: Monitors memory usage at regular intervals.

Cross-Platform: Works on any platform supported by the psutil library.

Mainly Made For Vrchat


Requirements
Python 3.x
psutil library

