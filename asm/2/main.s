[bits 64]
    extern printf
    extern exit
    section .text
fmt: db "output: %d", 10, 0
    section .data
    global main    
main:
%macro print_num 1
    xor rax,rax
    mov rdi, fmt
    lea rsi, [%1]
    call printf
%endmacro



; fib counters
    mov r9, 1
    mov r10, 2
    mov r12, 2 ; sum
next_fib:
    cmp r10, 4000000
    jge out_of_the_loop

    add r9, r10

; swap r9 <-> r10
    mov r11, r10
    mov r10, r9
    mov r9, r11

    test r10, 1
    jnz next_fib
    
    add r12, r10
    jmp next_fib  

out_of_the_loop:
    
    print_num r12 

    mov rsi, 0
    call exit

    
    
