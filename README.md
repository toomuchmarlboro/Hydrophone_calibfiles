# Hydrophone Calibration (Far-Field)

This repository contains scripts and generated audio files (pure sine waves and frequency sweeps) designed for the far-field calibration of hydrophones. **Note that this specific calibration procedure is designed to be performed in an AIR medium.**

## Equipment
- **Hydrophone:** Aquarian S1ex (Full datasheet available in `Datasheet/S1_datasheet.pdf`)
- **Soundcard / Audio Interface:** Soundcraft Ui24R (Specs available in `Datasheet/Ui24R_User Manual.pdf`) - *Used strictly for receiving/recording from the hydrophone.*
- **Acoustic Source:** Dodecahedron speaker (diameter ~10-12 cm) with an independent playback/amplifier system.

## Far-Field Calculation (In-Air)

To ensure accurate calibration, the hydrophone must be placed in the acoustic far-field of the sound source. In the far-field (Fraunhofer region), sound waves behave as spherical waves, and sound pressure decreases predictably with distance. 

The boundary of the far-field $r$ is generally determined by two conditions:
1. $r \gg \lambda$ (Distance must be much greater than the acoustic wavelength)
2. $r > \frac{D^2}{\lambda}$ (where $D$ is the maximum dimension of the speaker)

**Given our parameters (In-Air):**
- Speaker diameter $D \approx 0.12$ m
- Highest test frequency $f = 10,000$ Hz
- Speed of sound in air $c \approx 343$ m/s
- Shortest wavelength $\lambda = \frac{c}{f} = \frac{343}{10000} = 0.0343$ m

**Calculations:**
- $\frac{D^2}{\lambda} = \frac{(0.12)^2}{0.0343} = \frac{0.0144}{0.0343} \approx 0.42$ meters.

Since our actual calibration distance is **2.5 meters**, we easily satisfy both $2.5 \gg 0.0343$ m and $2.5 \gg 0.42$ m. Thus, the 2.5-meter placement is firmly within the acoustic far-field. This ensures a high-accuracy calibration free of near-field interference patterns.

---

## Calibration Procedure (English)

1. **Setup:** Connect the Aquarian S1ex hydrophone to the input of the Soundcraft Ui24R soundcard. Prepare the dodecahedron speaker with its separate playback/amplifier system.
2. **Placement:** Suspend the dodecahedron speaker and the hydrophone in the **air**, separated by a distance of exactly **2.5 meters** to guarantee far-field conditions.
3. **Playback:** Use the speaker system to play the generated `.wav` files located in the `wav_outputs/` directory (e.g., pure tones from 200 Hz up to 8000 Hz, or the 100 Hz to 10 kHz sweep). Note: These files utilize a 32-bit float format and a Tukey window taper to prevent transient clicks/noise.
4. **Recording:** Simultaneously record the hydrophone's signal response strictly through the Ui24R receiver interface.
5. **Analysis:** Compare the recorded response against the provided ground-truth spectrograms (`.png` files) to determine the hydrophone's voltage sensitivity and frequency response curve.

---

## Prosedur Kalibrasi (Bahasa Indonesia)

1. **Persiapan:** Hubungkan hidrofon Aquarian S1ex ke input soundcard Soundcraft Ui24R. Siapkan speaker dodecahedron dengan sistem pemutar/amplifier terpisah.
2. **Penempatan:** Posisikan speaker dodecahedron dan hidrofon di **udara**, dengan jarak pemisahan tepat **2,5 meter** untuk menjamin kondisi *far-field* (medan jauh).
3. **Pemutaran Audio:** Gunakan sistem speaker untuk memutar file `.wav` yang ada di dalam folder `wav_outputs/` (seperti nada murni dari 200 Hz hingga 8000 Hz, atau sweep dari 100 Hz ke 10 kHz). Catatan: File ini menggunakan format 32-bit float dan *Tukey window* untuk mencegah suara klik transien/noise.
4. **Perekaman:** Secara bersamaan, rekam sinyal respons yang ditangkap oleh hidrofon secara khusus melalui receiver Ui24R.
5. **Analisis:** Bandingkan hasil rekaman hidrofon dengan spektrogram referensi (file `.png`) yang tersedia untuk menentukan sensitivitas tegangan hidrofon dan kurva respons frekuensinya.
