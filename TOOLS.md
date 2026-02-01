# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- **TV LG:** IP `192.168.0.11`, Client Key `25d472261604e7ee1ba8af700b353232`.
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### Custom Automations 🚀

- **"Modo Relax"**: 
  - **Acción**: Reproducir radio Lofi en el Chromecast "Sala familiar".
  - **URL**: `https://www.youtube.com/watch?v=jfKfPfyJRdk`
  - **Comando**: `~/.local/bin/catt -d "Sala familiar" cast "https://www.youtube.com/watch?v=jfKfPfyJRdk"`

Add whatever helps you do your job. This is your cheat sheet.
