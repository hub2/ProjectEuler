[bits 64]
    extern printf

    section .data:
fmt: db "output: %d", 10, 0   

    section .text:

    global main
main:
    mov rcx, 999
    mov r9, 0
    mov r10, 3
    mov r11, 5
count_them:
    xor rdx, rdx
    mov rax, rcx
    div r10
    cmp rdx, 0
    jz is_divisible    
    
    xor rdx, rdx
    mov rax, rcx
    div r11
    cmp rdx, 0
    jz is_divisible

    jmp continue

is_divisible:
    add r9, rcx


continue:
    loop count_them
    
    mov rdi, fmt
    lea rsi, [r9]
    xor rax, rax
    call printf

    mov rax, 1
    mov rbx, 0
    int 0x80
