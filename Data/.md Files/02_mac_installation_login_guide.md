# ProctorIQ Secure Browser — Mac Installation & Login Guide

## Overview

This guide covers installing and logging into the ProctorIQ Secure Browser (PSB) on macOS. Mac installation differs from Windows in a few important ways — do not follow the Windows guide on a Mac device.

## Section 1: Installing PSB on macOS

1. Download the macOS installer (.dmg file) from the link in your assessment invite email.
2. Open the .dmg file and drag the PSB application into your Applications folder.
3. On first launch, macOS will block PSB as an app from an "unidentified developer." Go to System Settings → Privacy & Security, scroll to the Security section, and click "Open Anyway" next to the PSB entry.
4. Grant PSB the required permissions when prompted: Camera, Microphone, Screen Recording, and Accessibility. All four must be enabled — PSB will not proceed to login if any permission is denied.
5. Restart your Mac after granting permissions, even if not explicitly prompted.

## Section 2: Common Installation Errors

### "Element not found"
On Mac, this most often means one or more of the required permissions (Camera, Microphone, Screen Recording, Accessibility) was not granted.
- Open System Settings → Privacy & Security and manually verify all four permissions are toggled on for PSB.
- Quit and relaunch PSB after changing permissions — permission changes do not apply to an already-running session.

### "Session Start Error"
Same underlying cause as on Windows — PSB cannot reach the ProctorIQ assessment server.
- Check System Settings → Network to confirm you are connected to Wi-Fi or Ethernet.
- macOS firewall (System Settings → Network → Firewall) rarely blocks PSB by default, but if you have a third-party firewall tool installed, temporarily disable it.
- Reattempt login. If it fails twice, restart your Mac before a third attempt.

### "Unspecified Error"
- Force-quit PSB via Activity Monitor if it is unresponsive.
- Restart your Mac.
- Reopen PSB and attempt the mock test again.
- Do not attempt more than three retries without restarting — repeated retries without a restart do not resolve this error.

## Section 3: Login Issues

### Incognito/Private Browsing Login Failures
As with Windows, PSB requires login through its native application window, not a Safari or Chrome private window.
- Quit all browser windows.
- Launch PSB directly from Applications (or Launchpad).
- Log in using the credentials from your assessment invite email.

### OTP / PIN Issues
- OTPs expire after 5 minutes — request a fresh one rather than reusing an expired code.
- Confirm your registered contact details match your assessment profile if the OTP does not arrive within 2 minutes.
- A forgotten PIN can be reset via the "Forgot PIN" link on the PSB login screen — this is self-service and does not require Support.

## Section 4: Apple Silicon Note

PSB runs natively on both Intel and Apple Silicon (M-series) Macs. There is no separate installer for M-series chips — the same .dmg file detects your architecture automatically. If PSB seems unusually slow to launch on an M-series Mac, this is normal on first launch only (Gatekeeper verification); subsequent launches are faster.

## Section 5: Before You Begin

Complete a mock test at least 24 hours before your actual assessment slot, same as the Windows guidance — Mac permission issues in particular are easier to resolve with time to spare.
