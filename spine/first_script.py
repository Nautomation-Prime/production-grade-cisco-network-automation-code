"""Chapter 4 - the starting point.

THIS SCRIPT IS DELIBERATELY FLAWED. It is the
"before" in a thirty-chapter argument, kept
here unchanged so later chapters can diff
against it.

It will work. That is the problem. Do not run
it against anything you care about - see
chapter 4 for the twelve things wrong with it,
and `git log spine/` for the fixes.
"""

from netmiko import ConnectHandler

devices = [
    "10.10.20.11",
    "10.10.20.12",
    "10.10.20.13",
]

for ip in devices:
    conn = ConnectHandler(
        device_type="cisco_ios",
        host=ip,
        username="admin",
        password="Cisco123",
    )
    output = conn.send_command("show version")
    print(f"--- {ip} ---")
    print(output)
    conn.disconnect()
