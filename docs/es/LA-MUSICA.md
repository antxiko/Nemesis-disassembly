# La música

Todo lo que suena aquí sale de ejecutar el motor de sonido del cartucho (`suena`, 0x8063 del banco 7, y `encola_sonido`, 0x4A22, que apunta la petición en las colas; lo llama la interrupción en p00:4035 con los bancos 7 y 8 puestos) en un Z80 emulado, cuadro a cuadro y a 60 por segundo, igual que lo llama el juego. Lo que el motor escribe en el PSG pasa a sonido con un AY-3-8910 (`tools/musica.py`). Cada MP3 es la pieza entera hasta donde vuelve a empezar, más 8 segundos de la vuelta apagándose; las que no se repiten acaban donde acaba el motor.

## Cotejado con openMSX

Las escrituras al PSG se han comparado cuadro a cuadro con las de openMSX (C-BIOS MSX1 japonés). En todos los cuadros el PSG queda igual:

- el principio de la fase 1 (0x32) entero, 126 cuadros;
- la pista 0x16, sus primeros 217 cuadros.

El timbre no está cotejado: es el de un AY-3-8910 de manual, no una grabación del emulador. Las sondas están en `tools/omsx_psg.tcl` y `tools/coteja_psg.py`.

## Cómo se pide una pieza

`pide_sonido` (p00:49E9) mete los bancos 7 y 8, llama a `encola_sonido` con el número en A y devuelve el reparto de antes; `mira_si_hay_sonido` (p00:49DE) mira antes el bit 6 de 0xE002. Los siete bits bajos son el número: por debajo del 0x16 el sonido va a la cola de 0xE034 con un canal, del 0x16 al 0x25 usa dos canales y del 0x26 en adelante tres. Las fichas de 17 bytes están en 0xE010, 0xE021 y 0xE032, y 0xE043 guarda la copia del mezclador del PSG, que el arranque deja en 0xB8. Las pistas «de la tabla» (0x16 en adelante) salen de la tabla de 0x8328 por un número que el juego calcula; se omiten las de más de cuatro minutos.

## Las músicas

**El principio de la fase 1** (0x32)

Lo pide `suena_al_llegar`: en la fase 1, a la cuenta 0x1C1; dura 2,1 s.

<audio controls preload="none" src="../audio/musica_32.mp3?v=f459bbfa"></audio>

**El principio de las demás fases** (0x13)

Lo pide `suena_al_llegar`: en las demás, a la cuenta 0xB3; dura 1,6 s.

<audio controls preload="none" src="../audio/musica_13.mp3?v=e1364249"></audio>

**El núcleo revienta** (0x3B)

Lo pide `revienta_el_nucleo`; dura 1,5 s.

<audio controls preload="none" src="../audio/musica_3B.mp3?v=d4ec7125"></audio>

**El final del juego** (0x41)

Lo pide `arranca_el_final_del_juego`; dura 2,0 s.

<audio controls preload="none" src="../audio/musica_41.mp3?v=a19ea6a1"></audio>

**La nave ha muerto** (0x47)

Lo pide `la_nave_ha_muerto`; dura 2,8 s.

<audio controls preload="none" src="../audio/musica_47.mp3?v=856299a9"></audio>

**Pista 0x16 de la tabla** (0x16)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 119,8 s.

<audio controls preload="none" src="../audio/musica_16.mp3?v=f33b678c"></audio>

**Pista 0x19 de la tabla** (0x19)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 123,6 s y vuelve a empezar en el segundo 51,1.

<audio controls preload="none" src="../audio/musica_19.mp3?v=c5dd13a5"></audio>

**Pista 0x29 de la tabla** (0x29)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 120,4 s y vuelve a empezar en el segundo 99,1.

<audio controls preload="none" src="../audio/musica_29.mp3?v=e239651e"></audio>

**Pista 0x31 de la tabla** (0x31)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 54,1 s y vuelve a empezar en el segundo 51,2.

<audio controls preload="none" src="../audio/musica_31.mp3?v=26c4fd69"></audio>

**Pista 0x33 de la tabla** (0x33)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 16,9 s y vuelve a empezar en el segundo 13,7.

<audio controls preload="none" src="../audio/musica_33.mp3?v=d2253fbe"></audio>

**Pista 0x34 de la tabla** (0x34)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 123,3 s y vuelve a empezar en el segundo 82,5.

<audio controls preload="none" src="../audio/musica_34.mp3?v=1b77ebed"></audio>

**Pista 0x35 de la tabla** (0x35)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 123,3 s y vuelve a empezar en el segundo 82,5.

<audio controls preload="none" src="../audio/musica_35.mp3?v=6b996bfc"></audio>

**Pista 0x36 de la tabla** (0x36)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 39,0 s y vuelve a empezar en el segundo 34,1.

<audio controls preload="none" src="../audio/musica_36.mp3?v=6a1dc3ab"></audio>

**Pista 0x37 de la tabla** (0x37)

Lo pide ninguna llamada directa: sale de la tabla de pistas por un número calculado; dura 34,2 s.

<audio controls preload="none" src="../audio/musica_37.mp3?v=d5a0b052"></audio>
