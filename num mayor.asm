.model small
.data
    msj db 10,13, "Digite el valor del numero:  $"
    msj2 db 10,13, "El numero mayor es: $"
     
    
    nummayor db 0




.code 
    mov ax, @data
    mov ds, ax
    
    mov  cx, 5
    
    
    ciclo:
    
    dec cx
    mov ah, 9
    lea dx, msj 
    int 21h
    
    mov ah,1
    int 21h 
    
    sub al, 30h
    
    cmp al, nummayor
    
    jg agregar
    jl continuar
    
    agregar:
    mov nummayor, al
    mov al, 0
    continuar:
    cmp cx, 0
    je salir
    jg ciclo
      







Salir: 
    mov ah, 9
    lea dx, msj2
    int 21h  
    
    mov dl, nummayor
    add dl, 30h 
    mov ah, 2 
    int 21h
    
     
    
     


.exit