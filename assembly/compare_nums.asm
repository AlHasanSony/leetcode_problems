;compare two numbers


.model small
.stack 100h
.data
MsgEq db 'Numbers are Equal $'
MsgUneq db 'Numbers are Unequal and $'
MsgGr db ' First Number is greater than second number $'
MsgLs db ' First Number is lesser than second number $'

.code
main proc ; defines the main procedure
mov ax, @data ;The data section is used for declaring initialized data or constants
mov ds, ax    ;A 16-bit Data Segment register or DS register stores the starting address of the data segment

mov ah, 1     ; input first number
int 21h
mov bl, al     ; saving first number to bl from al

mov al, 1      ; input second number
int 21h
mov cl, al    ; saving second number to cl from al

L1:            
cmp bl,cl       ; Comparing whether they are equal or not
je EQUAL     ; Jump to Equal box, where we print the equal msg

mov dl, 10     ; for next line feed
mov ah, 2
int 21h
mov dl, 13      ; for carriage return
mov ah, 2
int 21h

mov dx, offset MsgUneq   ; but if not equal, then print msg they are not equal
mov ah, 9
int 21h

cmp bl, cl          ; again compare to check the first is greater or lesser
jge Greater         ; if greater, jump to greater to print a greater msg

mov dx, offset MsgLs  ; but if not greater, print lesser msg
mov ah, 9
int 21h
jmp PRINT



Greater:
mov dx, offset MsgGr
mov ah, 9
int 21h
jmp PRINT


EQUAL:
mov dl, 10     ; for next line feed
mov ah, 2
int 21h
mov dl, 13      ; for carriage return
mov ah, 2
int 21h

mov dx, offset MsgEq
mov ah, 9
int 21h
jmp PRINT



PRINT:
mov ah,4ch
int 21h
main endp

end main
