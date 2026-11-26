# ProctorIQ Secure Browser — Windows Installation & Login Guide

## Overview

The ProctorIQ Secure Browser (PSB) is required to attempt any proctored assessment on the ProctorIQ platform. This guide covers installation, login, and the most common errors students hit on Windows before an exam begins.

## Section 1: Installing PSB on Windows

1. Download the Windows installer from the link provided in your assessment invite email.
2. Run the installer as Administrator (right-click → "Run as administrator"). Standard user permissions are not sufficient to install PSB's kiosk-mode driver.
3. Restart your laptop after installation completes, even if not prompted. PSB's lockdown driver only loads fully after a restart.
4. Open PSB from the desktop shortcut, not from the downloads folder installer file.

## Section 2: Common Installation Errors

### "Element not found"
This error occurs when a required system component (usually a display or kiosk-mode driver) failed to register during install.
- Uninstall PSB completely via Control Panel → Programs.
- Restart your laptop.
- Re-download the installer fresh (do not reuse the old installer file).
- Install again as Administrator, then restart once more before opening PSB.

### "Session Start Error"
This error appears when PSB cannot establish a secure session with the ProctorIQ assessment server, usually due to a firewall or antivirus blocking the connection.
- Temporarily disable third-party antivirus/firewall software (not Windows Defender — Defender is compatible with PSB).
- Confirm your internet connection is active outside of PSB.
- Reopen PSB and attempt login again.
- If the error persists after two attempts, restart your laptop before trying a third time.

### "Unspecified Error"
A generic failure that can occur for several underlying reasons. Standard resolution sequence:
- Close PSB completely (check Task Manager to confirm no PSB process is still running).
- Restart your laptop.
- Reopen PSB and attempt the mock test again before your actual exam slot.
- If it recurs after a restart, this is escalated to Support with your device logs — do not keep retrying more than three times.

## Section 3: Login Issues

### Incognito/Private Browsing Login Failures
PSB requires a full account login through its native window, not a browser tab. If you were previously redirected to a browser incognito window during login:
- Close all browser windows.
- Reopen PSB from the desktop shortcut only.
- Log in using the credentials from your assessment invite email — do not use saved browser passwords, as PSB does not read browser-stored credentials.

### OTP / PIN Issues
- OTPs are valid for 5 minutes from generation. If it expires, request a new one — do not attempt to reuse an expired code.
- If the OTP is not received within 2 minutes, check that the phone number/email on your assessment profile matches your registered contact details.
- The PIN set during profile registration is separate from the OTP. If you have forgotten your PIN, use the "Forgot PIN" link on the PSB login screen — this is a self-service reset and does not require Support involvement.

## Section 4: Before You Begin

Always complete a mock test at least 24 hours before your actual assessment slot. Installation and login issues discovered during a mock test have time to be resolved; issues discovered minutes before your actual exam window may not.
