;experiment:
;FIND AVERAGE

DTSEG SEGMENT
    DATA DB 25H, 12H, 15H, 10H, 11H
    DTSEG ENDS
SUM1 DB ?
AVG DB ?
 REMAINDER DB ?
 
 CDSEG SEGMENT 
    MAIN PROC FAR
        ASSUME CS: CDSEG, DS: DTSEG
        MOV AX, DTSEG
        MOV DS, AX
        MOV CX, 05H
        MOV AL, 00H
      AGAIN : ADD AL, [BX]
        INC BX
        DEC CX
        JNZ AGAIN
     
        MOV DL, AL
        MOV SUM1, AL
        MOV AH, 00H
        MOV BL, 5H
        DIV BL
        MOV AVG,AL
        MOV REMAINDER, AH
        MAIN ENDP
    CDSEG ENDS
 END MAIN
        