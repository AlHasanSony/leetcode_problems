;ASSEMBLY LANGUAGE OF STRING OPERATION (PRINT A STRING) 

.MODEL SMALL
.STACK 100H
.DATA
MSG DB 'Hello World $';
MAIN PROC
     MOV AX,@DATA;
     MOV DS,AX  
     LEA DX,MSG;
     MOV AH,09H;
     INT 21H; 
     MAIN ENDP;
END MAIN