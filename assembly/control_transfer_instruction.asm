;experiment:
;program of control instruction in assembly language



DTSEG SEGMENT
    DATA DB 25H, 12H, 15H, 10H, 11H
    DTSEG ENDS ; Data segment ends
CDSEG SEGMENT   ; code segment
    MAIN PROC FAR ; 
        ASSUME CS CDSEG, DS:DTSEG
        MOV AX, DTSEG
        MOV DS, AX
        MOV CX, 05H
        MOV AL, 0H
        AGAIN: ADD AL, [BX]
        INC BX
        DEC CX
        JNZ AGAIN
        
        MOV DL, AL
        MOV AH, 4CH
        INT 21H
        MAIN ENDP
    END MAIN