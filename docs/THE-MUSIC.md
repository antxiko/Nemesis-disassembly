# The music

Everything you hear here comes from running the cartridge's own sound engine (`suena`, 0x8063 of bank 7, and `encola_sonido`, 0x4A22, which writes the request into the queues; the interrupt calls it at p00:4035 with banks 7 and 8 mapped) on an emulated Z80, frame by frame at 60 per second, just as the game calls it. What the engine writes to the PSG is turned into sound with an AY-3-8910 (`tools/musica.py`). Each MP3 is the whole piece up to where it starts again, plus 8 seconds of the repeat fading out; those that do not repeat end where the engine ends.

## Checked against openMSX

The PSG writes have been compared frame by frame with those of openMSX (C-BIOS MSX1 japonés). In every frame the PSG ends up the same:

- the start of stage 1 (0x32), whole, 126 frames;
- track 0x16, its first 217 frames.

The timbre is not checked: it is a textbook AY-3-8910, not a recording of the emulator. The probes are `tools/omsx_psg.tcl` and `tools/coteja_psg.py`.

## How a piece is asked for

`pide_sonido` (p00:49E9) maps banks 7 and 8, calls `encola_sonido` with the number in A and restores the previous mapping; `mira_si_hay_sonido` (p00:49DE) first checks bit 6 of 0xE002. The low seven bits are the number: below 0x16 the sound goes to the 0xE034 queue with one channel, from 0x16 to 0x25 it uses two channels and from 0x26 up three. The 17-byte records are at 0xE010, 0xE021 and 0xE032, and 0xE043 holds the copy of the PSG mixer, which start-up leaves at 0xB8. The tracks marked «in the table» (0x16 up) come from the 0x8328 table by a number the game computes; those over four minutes are left out.

## The tunes

**The start of stage 1** (0x32)

Asked for by `suena_al_llegar`: en la fase 1, a la cuenta 0x1C1; lasts 2.1 s.

<audio controls preload="none" src="audio/musica_32.mp3?v=f459bbfa"></audio>

**The start of the other stages** (0x13)

Asked for by `suena_al_llegar`: en las demás, a la cuenta 0xB3; lasts 1.6 s.

<audio controls preload="none" src="audio/musica_13.mp3?v=e1364249"></audio>

**The core blows up** (0x3B)

Asked for by `revienta_el_nucleo`; lasts 1.5 s.

<audio controls preload="none" src="audio/musica_3B.mp3?v=d4ec7125"></audio>

**The end of the game** (0x41)

Asked for by `arranca_el_final_del_juego`; lasts 2.0 s.

<audio controls preload="none" src="audio/musica_41.mp3?v=a19ea6a1"></audio>

**The ship has died** (0x47)

Asked for by `la_nave_ha_muerto`; lasts 2.8 s.

<audio controls preload="none" src="audio/musica_47.mp3?v=856299a9"></audio>

**Table track 0x16** (0x16)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 119.8 s.

<audio controls preload="none" src="audio/musica_16.mp3?v=f33b678c"></audio>

**Table track 0x19** (0x19)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 123.6 s and starts again at second 51.1.

<audio controls preload="none" src="audio/musica_19.mp3?v=c5dd13a5"></audio>

**Table track 0x29** (0x29)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 120.4 s and starts again at second 99.1.

<audio controls preload="none" src="audio/musica_29.mp3?v=e239651e"></audio>

**Table track 0x31** (0x31)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 54.1 s and starts again at second 51.2.

<audio controls preload="none" src="audio/musica_31.mp3?v=26c4fd69"></audio>

**Table track 0x33** (0x33)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 16.9 s and starts again at second 13.7.

<audio controls preload="none" src="audio/musica_33.mp3?v=d2253fbe"></audio>

**Table track 0x34** (0x34)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 123.3 s and starts again at second 82.5.

<audio controls preload="none" src="audio/musica_34.mp3?v=1b77ebed"></audio>

**Table track 0x35** (0x35)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 123.3 s and starts again at second 82.5.

<audio controls preload="none" src="audio/musica_35.mp3?v=6b996bfc"></audio>

**Table track 0x36** (0x36)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 39.0 s and starts again at second 34.1.

<audio controls preload="none" src="audio/musica_36.mp3?v=6a1dc3ab"></audio>

**Table track 0x37** (0x37)

Asked for by ninguna llamada directa: sale de la tabla de pistas por un número calculado; lasts 34.2 s.

<audio controls preload="none" src="audio/musica_37.mp3?v=d5a0b052"></audio>
