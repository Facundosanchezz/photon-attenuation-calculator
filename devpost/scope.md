---
doc: scope
status: approved
---
<!-- `status` is the progress state every skill reads. Write `draft` when you first save this file,
     and change it to `approved` when the learner clearly approves the displayed plan ("looks good" counts).
     Do not request a second sign-off. Never skip the draft save —
     an unsaved draft dies with the conversation. -->

<!-- Scope is a rough sketch of the heart of the idea — NOT the detailed product
     definition. Resist the urge to fill this out exhaustively: features, screens,
     and behavior belong in the PRD, which comes next. Capture what makes this
     project distinctive and what belongs in a coherent proof of concept.
     Add a section if the conversation surfaced something important that
     doesn't fit below. Keep it short and readable. -->

# Photon Attenuation Calculator

One line: A web app that lets medical physics students explore photon attenuation by selecting material, energy, and thickness to see transmitted fraction, HVL, TVL, and an instantaneous attenuation curve using real NIST XCOM total attenuation coefficients (including coherent scattering).

## The Unique Kernel
The combination of medically‑relevant framing (water, bone, lead, air) with immediate visual feedback—changing any input updates the numbers and curve in real time—makes this tool feel like a lab widget students can tweak to build intuition.

## Who It's For
A medical physics student studying radiation interactions who wants to experiment with how attenuation varies across common tissue‑equivalent materials and energies, instead of just reading static tables or doing manual calculations.

## The Core Loop
1. Pick a material (water, air, bone, lead) and a photon energy (keV/MeV range).
2. Enter a thickness (cm).
3. Observe the transmitted fraction (I/I₀), half‑value layer (HVL), tenth‑value layer (TVL), and the attenuation curve I = I₀ × e^(-μx) update instantly.
4. Change any input and see everything respond without delay.

## Inspiration & Identity
- Clean, educational feel similar to PhET simulations but focused on a single concept.
- No flashy animations—just clear inputs, numbers, and a responsive plot.
- Reference: NIST XCOM database (https://physics.nist.gov/XCOM) for authentic attenuation coefficients.
- Tone: approachable, precise, and geared toward quick exploration.

## Why This Matters to the Learner
- Applies my medical physics background in code, showing I can bridge domain knowledge and software.
- Creates a portfolio‑ready visual demo for a first AI/LLM job.
- Gives me hands‑on experience working with an AI agent in a structured, plan‑first workflow so I can understand and explain every part of the code.

## What "Working" Looks Like
Open the app, select **water**, **100 keV**, and **5 cm** thickness. The screen shows:
- Transmitted fraction ≈ e^(-0.171 × 5) ≈ 0.42
- HVL ≈ ln(2)/0.171 ≈ 4.05 cm
- TVL ≈ ln(10)/0.171 ≈ 13.46 cm
- A curve plotting intensity vs. thickness from 0 to 5 cm.
Switching the material to **lead** updates μ to ~63 cm⁻¹, making the transmitted fraction drop to nearly zero and the curve steepen instantly—demonstrating the massive attenuation difference.

## The POC Boundary
**In:**
- Embedded CSV containing real NIST XCOM mass attenuation coefficients (μ/ρ in cm²/g) for water, air, bone, lead, multiplied by each material’s density to give μ (cm⁻¹). Source noted in CSV.
- Energy range 10 keV to 10 MeV (diagnostic imaging through radiotherapy, including lead L-edges). NIST XCOM CSV includes duplicate energy rows at lead K-edge (88 keV) with interpolation on each side separately.
- Log‑log interpolation (via pandas/numpy) to compute μ for any user‑entered energy.
- Three‑screen flow: (1) material + energy picker, (2) thickness input + compute (transmitted fraction, HVL, TVL), (3) attenuation curve plot.
- Four materials with NIST‑XCOM densities: water (ρ=1.0 g/cm³), dry air (ρ=0.001205 g/cm³), cortical bone (ρ=1.92 g/cm³), lead (ρ=11.35 g/cm³).
- Simple test: verify water at 100 keV yields μ ≈ 0.171 cm⁻¹ (within 1%).
- Thickness input accepts cm; the plot's x‑axis adapts to the selected material and energy, spanning 0 to 5×TVL for that combination.
- Energy input accepts both keV and MeV (e.g., 100 keV or 0.1 MeV).
- **Model note:** this is a narrow‑beam, monoenergetic, educational‑only model. It is not intended for clinical use and does not model scatter, broad beams, or polyenergetic spectra.
- Built with **Streamlit** using **Plotly** for interactive plotting; the math uses numpy/pandas for log‑log interpolation of NIST XCOM total attenuation coefficients (which include coherent scattering, photoelectric, Compton, and pair‑production contributions).

**Out of scope for the PoC:**
- Live fetching from NIST XCOM API (saved for later).
- Multiple material comparison or side‑by‑side curves.
- Export/save results, user accounts, sharing.
- Advanced beam geometries (divergent, broad beam) or scatter considerations.
- LLM‑generated explanations, dark mode, accessibility polish, responsive design beyond basic.
- Units beyond cm and keV/MeV (no conversion to mm, MeV, etc.).

## Later
- Replace embedded CSV with live NIST XCOM API calls with caching and error handling.
- Add comparison mode (overlay curves for different materials).
- Include export to CSV/PNG of results and plot.
- Implement an optional LLM explanation panel that translates the numbers into plain language.
- Polish UI with responsive layout, tooltips, and accessibility improvements.
- Expand material list (e.g., lung, fat, contrast agents).

## Explicitly Cut
- User authentication or persistence—nothing needs to be saved between sessions.
- Advanced physics: coherent scattering, pair production details beyond attenuation coefficient.
- Complex UI themes or multi‑language support.
- Any feature that requires backend server or database; the PoC runs entirely frontend‑or‑single‑process.