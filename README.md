# ArtViSiON — Interactive 3D Showroom

**Production Design · Branding · Signage · Vector Art — Indore**

Ek interactive 3D showroom experience jo ArtViSiON ki saari services ko ek virtual environment me dikhata hai — bahar ka plaza, 12 clickable products, aur andar division-wise gallery.

🔗 **Live Demo:** `https://<your-username>.github.io/artvision-showroom/`

---

## ✨ Features

- **3D Environment (Three.js)** — mouse se zoom/drag, product par click = full-screen focus + details panel
- **12 Products:** ACP Signage, Acrylic Letters, Window Display (saree mannequin + flying kiss), Backlight Fabric (live animated SEG), Arch Gate ("Welcome" click = enter), Offer Standee, Owl Mascot (namaste animation), Banner, Canvas Art, FMCG Kiosk, CNC (live cutting), Large Format Printer (live printing)
- **Real-time Day/Night** — bahar ka mausam aapke local time se badalta hai
- **Interior:** 5 division canvases (click = gallery), selfie zone, animated ceiling sky (rain/sunset/night + ambient sounds), full-wall backdrop
- **Auto Rickshaw** — engine start hokar precinct ke chakkar lagata hai (synth putt-putt sound)
- **Galleries:** 28 services, collage-style AI-generated photos, Before/After comparisons

## 🚀 Deploy (GitHub Pages)

1. Is repo ko GitHub par push/upload karo
2. **Settings → Pages → Source:** `Deploy from a branch` → `main` / `root` → Save
3. 1–2 minute me live!

Koi build step nahi — pure static site (HTML + JS + assets).

## 📁 Structure

```
index.html      — poora app (single file)
assets/         — logo, gallery images, textures
lib/            — three.js + OrbitControls (local, no CDN)
```

## 🎮 Controls

| Action | Result |
|---|---|
| Scroll | Zoom in/out |
| Drag | Rotate view |
| Click product | Focus + details |
| Click "Welcome" gate / roof structure | Enter showroom |
| Esc | Back / exit |
| ← → (focus me) | Agla/pichhla product |

---

© ArtViSiON Production Design, Indore. All rights reserved.
