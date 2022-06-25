name "life_motto"

org 100h

; set video mode    
mov ax, 3     ; text mode 80x25, 16 colors, 8 pages (ah=0, al=3)
int 10h       ; do it!

; cancel blinking and enable all 16 colors:
mov ax, 1003h
mov bx, 0
int 10h


; set segment register:
mov     ax, 0b800h
mov     ds, ax

; print "KeepMoving"
; first byte is ascii code, second byte is color code.

mov [02h], 'K'

mov [04h], 'e'

mov [06h], 'e'

mov [08h], 'p'

mov [0ah], 'M'

mov [0ch], 'o'

mov [0eh], 'v'
 
mov [10h], 'i'

mov [12h], 'n'

mov [14h], 'g'

mov [16h], '.'

mov [18h], '.'

; color all characters:
mov cx, 12  ; number of characters.
mov di, 03h ; start from byte after 'h'

c:  mov [di], 11101100b   ; light red(1100) on yellow(1110)
    add di, 2 ; skip over next ascii code in vga memory.
    loop c

; wait for any key press:
mov ah, 0
int 16h

ret

