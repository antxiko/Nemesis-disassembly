#!/usr/bin/env python3
"""La musica del cartucho, ejecutando su motor de sonido (ver motor_musica.py).

El reproductor `suena` (0x8063, banco 7 en 0x8000 y banco 8 en 0xA000) lo llama
la interrupcion en cada cuadro (p00:4035); el sonido se pide con `encola_sonido`
(p00:4A22, A = numero), que escribe en la cola de 0xE012/0xE034 la peticion con
los datos de la tabla de 0x8328 del banco 7. Tres fichas de 17 bytes desde
0xE010; la mezcla del PSG, en 0xE043. MegaROM Konami4 de 128 KB, sin SCC.
Uso:  musica.py registros 0x32 [cuadros] | mp3 0x32 f.mp3 | todas docs/audio
      musica.py barrido 0x01 0x50 | emu
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import motor_musica  # noqa: E402
from motor_musica import P  # noqa: E402

TABLA = "ninguna llamada directa: sale de la tabla de pistas por un número calculado"

PIEZAS = [
    P(0x32, "El principio de la fase 1", "The start of stage 1",
      "`suena_al_llegar`: en la fase 1, a la cuenta 0x1C1"),
    P(0x13, "El principio de las demás fases", "The start of the other stages",
      "`suena_al_llegar`: en las demás, a la cuenta 0xB3"),
    P(0x3B, "El núcleo revienta", "The core blows up",
      "`revienta_el_nucleo`"),
    P(0x41, "El final del juego", "The end of the game",
      "`arranca_el_final_del_juego`"),
    P(0x47, "La nave ha muerto", "The ship has died", "`la_nave_ha_muerto`"),
] + [P(n, "Pista 0x%02X de la tabla" % n, "Table track 0x%02X" % n, TABLA)
     for n in (0x16, 0x19, 0x29, 0x31, 0x33, 0x34, 0x35, 0x36, 0x37)]

PAGINA = motor_musica.pagina_basica(
    "`suena`, 0x8063 del banco 7, y `encola_sonido`, 0x4A22, que apunta la "
    "petición en las colas; lo llama la interrupción en p00:4035 con los "
    "bancos 7 y 8 puestos",
    "`suena`, 0x8063 of bank 7, and `encola_sonido`, 0x4A22, which writes the "
    "request into the queues; the interrupt calls it at p00:4035 with banks "
    "7 and 8 mapped",
    "C-BIOS MSX1 japonés",
    [("el principio de la fase 1 (0x32) entero, 126 cuadros",
      "the start of stage 1 (0x32), whole, 126 frames"),
     ("la pista 0x16, sus primeros 217 cuadros",
      "track 0x16, its first 217 frames")],
    [("Cómo se pide una pieza",
      "`pide_sonido` (p00:49E9) mete los bancos 7 y 8, llama a "
      "`encola_sonido` con el número en A y devuelve el reparto de antes; "
      "`mira_si_hay_sonido` (p00:49DE) mira antes el bit 6 de 0xE002. Los "
      "siete bits bajos son el número: por debajo del 0x16 el sonido va a "
      "la cola de 0xE034 con un canal, del 0x16 al 0x25 usa dos canales y del "
      "0x26 en adelante tres. Las fichas de 17 bytes están en 0xE010, 0xE021 "
      "y 0xE032, y 0xE043 guarda la copia del mezclador del PSG, que el "
      "arranque deja en 0xB8. Las pistas «de la tabla» (0x16 en adelante) "
      "salen de la tabla de 0x8328 por un número que el juego calcula; se "
      "omiten las de más de cuatro minutos.",
      "How a piece is asked for",
      "`pide_sonido` (p00:49E9) maps banks 7 and 8, calls `encola_sonido` "
      "with the number in A and restores the previous mapping; "
      "`mira_si_hay_sonido` (p00:49DE) first checks bit 6 of 0xE002. The "
      "low seven bits are the number: below 0x16 the sound goes to the "
      "0xE034 queue with one channel, from 0x16 to 0x25 it uses two channels "
      "and from 0x26 up three. The 17-byte records are at 0xE010, 0xE021 and "
      "0xE032, and 0xE043 holds the copy of the PSG mixer, which start-up "
      "leaves at 0xB8. The tracks marked «in the table» (0x16 up) come from "
      "the 0x8328 table by a number the game computes; those over four "
      "minutes are left out.")])

CFG = dict(rom="nemesis.rom", org=0x4000, mapper="konami",
           bancos0=((0x4000, 0), (0x6000, 1), (0x8000, 7), (0xA000, 8)),
           frame=0x8063, pide=0x4A22, banco_frame=7, banco_pide=0,
           ram=(0xE010, 0xE046), excluye=[0xE01A, 0xE02B, 0xE03C],
           ram0=[(0xE043, 0xB8)], hz=60, psg0={7: 0xB8}, romtype="konami",
           piezas=PIEZAS, pagina=PAGINA,
           cotejado=[(0x32, 126, None), (0x13, 96, None)])

if __name__ == "__main__":
    sys.exit(motor_musica.main(CFG, sys.argv[1:]))
