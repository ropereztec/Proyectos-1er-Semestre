.model small
.data  
;En primer lugar se declaran todas las variables que van a contener numeros
    num1 db 0    ;se almacena el primer numero
    num2 db 0    ;se almacena el segundo numero 
     
    suma db 0    ;resultado de la suma
    
    resta  db 0  ;resultado de la resta              
     
    multiplicacion db 0 ;resultado de la multiplicacion      
     
    division db 0       ;resultado de la division


;En segundo lugar se declaran todos los mensajes que va a mostrar la calculadora

    msj1 db 13,10, "Digite el valor del primer numero: $"
    msj2 db 13,10, "Digite el valor del segundo numero: $" 
    
    msj3 db 13,10, "La suma de los numeros es: $" 
    msj4 db 13,10, "La resta de los numeros es: $"
    msj5 db 13,10, "La multiplicacion de los numeros es: $"
    msj6 db 13,10, "La division de los numeros es: $"  
    linea db 13, 10, "Que operacion desea efectuar: 1. Resta 2. Multiplicacion $"



.code

inicio:           
    mov ax,@data
    mov ds, ax
    mov ah, 9
    lea dx, msj1
    int 21h
    mov ah,1
    int 21h 
    sub al, 30h  ;esto convierte a los numeros ascii a decimales 
    mov num1, al  
    mov ah, 9
    lea dx, msj2
    int 21h
    mov ah,1
    int 21h 
    sub al, 30h  ;esto convierte a los numeros ascii a decimales
    mov num2, al
    
    mov ah,9      ;El servicio 9 imprime
    lea dx, linea 
    int 21h
    mov ah,1      ;El servicio 1 solicita informacion
    int 21h
    sub al,30h 
    cmp al,1
    je ResultResta
    Jne ResultMultiplicacion 
    

 
ResultResta:


    mov al, num1
    sub al, num2 
    mov resta,al 

    mov ah, 9
    lea dx, msj4
    int 21h    
    
    mov dl, resta
    add dl, 30h   ;esto convierte al numero nuevamente en ascii
    mov ah, 2
    int 21h 
    jmp Salir
    
    
ResultMultiplicacion:


    mov al, num1
    mul num2
    mov multiplicacion, al
    
    mov ah, 9
    lea dx, msj5
    int 21h
    mov dl, multiplicacion
    add dl, 30h   ;esto convierte al numero nuevamente en ascii
    mov ah, 2
    int 21h 
    
    

Salir:
.exit
