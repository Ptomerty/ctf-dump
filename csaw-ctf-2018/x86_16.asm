00000000  FA                cli
00000001  B400              mov ah,0x0
00000003  B000              mov al,0x0
00000005  B80000            mov ax,0x0
00000008  B700              mov bh,0x0
0000000A  B300              mov bl,0x0
0000000C  BB0000            mov bx,0x0
0000000F  B501              mov ch,0x1
00000011  B101              mov cl,0x1
00000013  B90000            mov cx,0x0
00000016  80FD01            cmp ch,0x1
00000019  7402              jz 0x1d
0000001B  EB01              jmp short 0x1e
0000001D  F4                hlt
0000001E  80F900            cmp cl,0x0
00000021  7401              jz 0x24
00000023  F4                hlt
00000024  30F6              xor dh,dh
00000026  80E200            and dl,0x0
00000029  BAFFFF            mov dx,0xffff
0000002C  F7D2              not dx
0000002E  83FA00            cmp dx,byte +0x0
00000031  75EA              jnz 0x1d
00000033  8ED8              mov ds,ax
00000035  8EC3              mov es,bx
00000037  8EE1              mov fs,cx
00000039  8EEA              mov gs,dx
0000003B  8ED0              mov ss,ax
0000003D  89CC              mov sp,cx
0000003F  89D5              mov bp,dx
00000041  89E6              mov si,sp
00000043  89EF              mov di,bp
00000045  B80300            mov ax,0x3
00000048  CD10              int 0x10
0000004A  B074              mov al,0x74
0000004C  B40E              mov ah,0xe
0000004E  CD10              int 0x10
00000050  B8557C            mov ax,0x7c55
00000053  EB10              jmp short 0x65
00000055  61                popa
00000056  634F53            arpl [bx+0x53],cx
00000059  0A0D              or cl,[di]
0000005B  2020              and [bx+si],ah
0000005D  627920            bound di,[bx+di+0x20]
00000060  45                inc bp
00000061  6C                insb
00000062  796B              jns 0xcf
00000064  0089C680          add [bx+di-0x7f3a],cl
00000068  3C00              cmp al,0x0
0000006A  7409              jz 0x75
0000006C  8A04              mov al,[si]
0000006E  B40E              mov ah,0xe
00000070  CD10              int 0x10
00000072  46                inc si
00000073  EBF2              jmp short 0x67
00000075  EB09              jmp short 0x80
00000077  6C                insb
00000078  6F                outsw
00000079  6C                insb
0000007A  206B65            and [bp+di+0x65],ch
0000007D  6B2000            imul sp,[bx+si],byte +0x0
00000080  BD777C            mov bp,0x7c77
00000083  B603              mov dh,0x3
00000085  B20F              mov dl,0xf
00000087  B90700            mov cx,0x7
0000008A  BB0F00            mov bx,0xf
0000008D  B80113            mov ax,0x1301
00000090  CD10              int 0x10
00000092  BE507D            mov si,0x7d50
00000095  B442              mov ah,0x42
00000097  B280              mov dl,0x80
00000099  CD13              int 0x13
0000009B  EB55              jmp short 0xf2
0000009D  0D0A00            or ax,0xa
000000A0  0000              add [bx+si],al
000000A2  0000              add [bx+si],al
000000A4  2000              and [bx+si],al
000000A6  8D36A37C          lea si,[0x7ca3]
000000AA  89F7              mov di,si
000000AC  BB0A00            mov bx,0xa
000000AF  31D2              xor dx,dx
000000B1  F7F3              div bx
000000B3  83C230            add dx,byte +0x30
000000B6  8814              mov [si],dl
000000B8  4E                dec si
000000B9  83F800            cmp ax,byte +0x0
000000BC  7402              jz 0xc0
000000BE  EBEF              jmp short 0xaf
000000C0  39FE              cmp si,di
000000C2  7504              jnz 0xc8
000000C4  C60430            mov byte [si],0x30
000000C7  4E                dec si
000000C8  46                inc si
000000C9  803C00            cmp byte [si],0x0
000000CC  7418              jz 0xe6
000000CE  51                push cx
000000CF  52                push dx
000000D0  50                push ax
000000D1  31C9              xor cx,cx
000000D3  BAFFFF            mov dx,0xffff
000000D6  B486              mov ah,0x86
000000D8  CD15              int 0x15
000000DA  58                pop ax
000000DB  5A                pop dx
000000DC  59                pop cx
000000DD  8A04              mov al,[si]
000000DF  B40E              mov ah,0xe
000000E1  CD10              int 0x10
000000E3  46                inc si
000000E4  EBE3              jmp short 0xc9
000000E6  C3                ret
000000E7  89E8              mov ax,bp
000000E9  E8BAFF            call 0xa6
000000EC  89E0              mov ax,sp
000000EE  E8B5FF            call 0xa6
000000F1  C3                ret
000000F2  B80100            mov ax,0x1
000000F5  50                push ax
000000F6  E8ADFF            call 0xa6
000000F9  E8EBFF            call 0xe7
000000FC  B80200            mov ax,0x2
000000FF  50                push ax
00000100  E8A3FF            call 0xa6
00000103  E8E1FF            call 0xe7
00000106  B80300            mov ax,0x3
00000109  50                push ax
0000010A  E899FF            call 0xa6
0000010D  E8D7FF            call 0xe7
00000110  B80400            mov ax,0x4
00000113  50                push ax
00000114  E88FFF            call 0xa6
00000117  E8CDFF            call 0xe7
0000011A  B80500            mov ax,0x5
0000011D  50                push ax
0000011E  E885FF            call 0xa6
00000121  E8C3FF            call 0xe7
00000124  58                pop ax
00000125  E87EFF            call 0xa6
00000128  E8BCFF            call 0xe7
0000012B  58                pop ax
0000012C  E877FF            call 0xa6
0000012F  E8B5FF            call 0xe7
00000132  58                pop ax
00000133  E870FF            call 0xa6
00000136  E8AEFF            call 0xe7
00000139  58                pop ax
0000013A  E869FF            call 0xa6
0000013D  E8A7FF            call 0xe7
00000140  58                pop ax
00000141  E862FF            call 0xa6
00000144  E8A0FF            call 0xe7
00000147  E9B6E2            jmp 0xe400
0000014A  90                nop
0000014B  90                nop
0000014C  90                nop
0000014D  90                nop
0000014E  90                nop
0000014F  90                nop
00000150  1000              adc [bx+si],al
00000152  0800              or [bx+si],al
00000154  006000            add [bx+si+0x0],ah
00000157  0001              add [bx+di],al
00000159  0000              add [bx+si],al
0000015B  0000              add [bx+si],al
0000015D  0000              add [bx+si],al
0000015F  0000              add [bx+si],al
00000161  0000              add [bx+si],al
00000163  0000              add [bx+si],al
00000165  0000              add [bx+si],al
00000167  0000              add [bx+si],al
00000169  0000              add [bx+si],al
0000016B  0000              add [bx+si],al
0000016D  0000              add [bx+si],al
0000016F  0000              add [bx+si],al
00000171  0000              add [bx+si],al
00000173  0000              add [bx+si],al
00000175  0000              add [bx+si],al
00000177  0000              add [bx+si],al
00000179  0000              add [bx+si],al
0000017B  0000              add [bx+si],al
0000017D  0000              add [bx+si],al
0000017F  0000              add [bx+si],al
00000181  0000              add [bx+si],al
00000183  0000              add [bx+si],al
00000185  0000              add [bx+si],al
00000187  0000              add [bx+si],al
00000189  0000              add [bx+si],al
0000018B  0000              add [bx+si],al
0000018D  0000              add [bx+si],al
0000018F  0000              add [bx+si],al
00000191  0000              add [bx+si],al
00000193  0000              add [bx+si],al
00000195  0000              add [bx+si],al
00000197  0000              add [bx+si],al
00000199  0000              add [bx+si],al
0000019B  0000              add [bx+si],al
0000019D  0000              add [bx+si],al
0000019F  0000              add [bx+si],al
000001A1  0000              add [bx+si],al
000001A3  0000              add [bx+si],al
000001A5  0000              add [bx+si],al
000001A7  0000              add [bx+si],al
000001A9  0000              add [bx+si],al
000001AB  0000              add [bx+si],al
000001AD  0000              add [bx+si],al
000001AF  0000              add [bx+si],al
000001B1  0000              add [bx+si],al
000001B3  0000              add [bx+si],al
000001B5  0000              add [bx+si],al
000001B7  0000              add [bx+si],al
000001B9  0000              add [bx+si],al
000001BB  0000              add [bx+si],al
000001BD  0000              add [bx+si],al
000001BF  0000              add [bx+si],al
000001C1  0000              add [bx+si],al
000001C3  0000              add [bx+si],al
000001C5  0000              add [bx+si],al
000001C7  0000              add [bx+si],al
000001C9  0000              add [bx+si],al
000001CB  0000              add [bx+si],al
000001CD  0000              add [bx+si],al
000001CF  0000              add [bx+si],al
000001D1  0000              add [bx+si],al
000001D3  0000              add [bx+si],al
000001D5  0000              add [bx+si],al
000001D7  0000              add [bx+si],al
000001D9  0000              add [bx+si],al
000001DB  0000              add [bx+si],al
000001DD  0000              add [bx+si],al
000001DF  0000              add [bx+si],al
000001E1  0000              add [bx+si],al
000001E3  0000              add [bx+si],al
000001E5  0000              add [bx+si],al
000001E7  0000              add [bx+si],al
000001E9  0000              add [bx+si],al
000001EB  0000              add [bx+si],al
000001ED  0000              add [bx+si],al
000001EF  0000              add [bx+si],al
000001F1  0000              add [bx+si],al
000001F3  0000              add [bx+si],al
000001F5  0000              add [bx+si],al
000001F7  0000              add [bx+si],al
000001F9  0000              add [bx+si],al
000001FB  0000              add [bx+si],al
000001FD  0055AA            add [di-0x56],dl
00000200  F4                hlt
00000201  E492              in al,0x92
00000203  0C02              or al,0x2
00000205  E692              out 0x92,al
00000207  31C0              xor ax,ax
00000209  8ED0              mov ss,ax
0000020B  BC0160            mov sp,0x6001
0000020E  8ED8              mov ds,ax
00000210  8EC0              mov es,ax
00000212  8EE0              mov fs,ax
00000214  8EE8              mov gs,ax
00000216  FC                cld
00000217  66BF00000000      mov edi,0x0
0000021D  EB07              jmp short 0x226
0000021F  90                nop
00000220  0000              add [bx+si],al
00000222  0000              add [bx+si],al
00000224  0000              add [bx+si],al
00000226  57                push di
00000227  66B900100000      mov ecx,0x1000
0000022D  6631C0            xor eax,eax
00000230  FC                cld
00000231  F366AB            rep stosd
00000234  5F                pop di
00000235  26668D850010      lea eax,[es:di+0x1000]
0000023B  6683C803          or eax,byte +0x3
0000023F  26668905          mov [es:di],eax
00000243  26668D850020      lea eax,[es:di+0x2000]
00000249  6683C803          or eax,byte +0x3
0000024D  266689850010      mov [es:di+0x1000],eax
00000253  26668D850030      lea eax,[es:di+0x3000]
00000259  6683C803          or eax,byte +0x3
0000025D  266689850020      mov [es:di+0x2000],eax
00000263  57                push di
00000264  8DBD0030          lea di,[di+0x3000]
00000268  66B803000000      mov eax,0x3
0000026E  26668905          mov [es:di],eax
00000272  660500100000      add eax,0x1000
00000278  83C708            add di,byte +0x8
0000027B  663D00002000      cmp eax,0x200000
00000281  72EB              jc 0x26e
00000283  5F                pop di
00000284  B0FF              mov al,0xff
00000286  E6A1              out 0xa1,al
00000288  E621              out 0x21,al
0000028A  90                nop
0000028B  90                nop
0000028C  0F011E2060        lidt [0x6020]
00000291  66B8A0000000      mov eax,0xa0
00000297  0F22E0            mov cr4,eax
0000029A  6689FA            mov edx,edi
0000029D  0F22DA            mov cr3,edx
000002A0  66B9800000C0      mov ecx,0xc0000080
000002A6  0F32              rdmsr
000002A8  660D00010000      or eax,0x100
000002AE  0F30              wrmsr
000002B0  0F20C3            mov ebx,cr0
000002B3  6681CB01000080    or ebx,0x80000001
000002BA  0F22C3            mov cr0,ebx
000002BD  0F0116E260        lgdt [0x60e2]
000002C2  EA58610800        jmp 0x8:0x6158
000002C7  0000              add [bx+si],al
000002C9  0000              add [bx+si],al
000002CB  0000              add [bx+si],al
000002CD  0000              add [bx+si],al
000002CF  0000              add [bx+si],al
000002D1  0000              add [bx+si],al
000002D3  009A2000          add [bp+si+0x20],bl
000002D7  0000              add [bx+si],al
000002D9  0000              add [bx+si],al
000002DB  00920000          add [bp+si+0x0],dl
000002DF  90                nop
000002E0  0000              add [bx+si],al
000002E2  1A00              sbb al,[bx+si]
000002E4  C7                db 0xc7
000002E5  60                pusha
000002E6  0000              add [bx+si],al
000002E8  A5                movsw
000002E9  1F                pop ds
000002EA  B11F              mov cl,0x1f
000002EC  AB                stosw
000002ED  1F                pop ds
000002EE  A7                cmpsw
000002EF  1F                pop ds
000002F0  9F                lahf
000002F1  1F                pop ds
000002F2  091F              or [bx],bx
000002F4  B51F              mov ch,0x1f
000002F6  A31FD7            mov [0xd71f],ax
000002F9  1F                pop ds
000002FA  8F                db 0x8f
000002FB  1F                pop ds
000002FC  B31F              mov bl,0x1f
000002FE  011F              add [bx],bx
00000300  0B1F              or bx,[bx]
00000302  0B1F              or bx,[bx]
00000304  D7                xlatb
00000305  1F                pop ds
00000306  FD                std
00000307  1F                pop ds
00000308  F31F              rep pop ds
0000030A  C9                leave
0000030B  1F                pop ds
0000030C  D7                xlatb
0000030D  1F                pop ds
0000030E  A5                movsw
0000030F  1F                pop ds
00000310  B71F              mov bh,0x1f
00000312  8D1F              lea bx,[bx]
00000314  D7                xlatb
00000315  1F                pop ds
00000316  99                cwd
00000317  1F                pop ds
00000318  191F              sbb [bx],bx
0000031A  051FD7            add ax,0xd71f
0000031D  1F                pop ds
0000031E  B71F              mov bh,0x1f
00000320  B51F              mov ch,0x1f
00000322  0F1FD7            hint_nop58 di
00000325  1F                pop ds
00000326  B31F              mov bl,0x1f
00000328  011F              add [bx],bx
0000032A  8F                db 0x8f
0000032B  1F                pop ds
0000032C  8F                db 0x8f
0000032D  1F                pop ds
0000032E  0B1F              or bx,[bx]
00000330  851F              test [bx],bx
00000332  A31FD7            mov [0xd71f],ax
00000335  1F                pop ds
00000336  0B1F              or bx,[bx]
00000338  A31FAB            mov [0xab1f],ax
0000033B  1F                pop ds
0000033C  891F              mov [bx],bx
0000033E  D7                xlatb
0000033F  1F                pop ds
00000340  011F              add [bx],bx
00000342  D7                xlatb
00000343  1F                pop ds
00000344  DB1F              fistp dword [bx]
00000346  091F              or [bx],bx
00000348  C3                ret
00000349  1F                pop ds
0000034A  93                xchg ax,bx
0000034B  1F                pop ds
0000034C  0000              add [bx+si],al
0000034E  0000              add [bx+si],al
00000350  0000              add [bx+si],al
00000352  0000              add [bx+si],al
00000354  0000              add [bx+si],al
00000356  0000              add [bx+si],al
00000358  66B810008ED8      mov eax,0xd88e0010
0000035E  8EC0              mov es,ax
00000360  8EE0              mov fs,ax
00000362  8EE8              mov gs,ax
00000364  8ED0              mov ss,ax
00000366  BF0080            mov di,0x8000
00000369  0B00              or ax,[bx+si]
0000036B  B9F401            mov cx,0x1f4
0000036E  0000              add [bx+si],al
00000370  48                dec ax
00000371  B8201F            mov ax,0x1f20
00000374  201F              and [bx],bl
00000376  201F              and [bx],bl
00000378  201F              and [bx],bl
0000037A  F348              rep dec ax
0000037C  AB                stosw
0000037D  BF0080            mov di,0x8000
00000380  0B00              or ax,[bx+si]
00000382  48                dec ax
00000383  31C0              xor ax,ax
00000385  48                dec ax
00000386  31DB              xor bx,bx
00000388  48                dec ax
00000389  31C9              xor cx,cx
0000038B  48                dec ax
0000038C  31D2              xor dx,dx
0000038E  B245              mov dl,0x45
00000390  80CA6C            or dl,0x6c
00000393  B679              mov dh,0x79
00000395  80CE6B            or dh,0x6b
00000398  20F2              and dl,dh
0000039A  B600              mov dh,0x0
0000039C  48                dec ax
0000039D  BEE860            mov si,0x60e8
000003A0  0000              add [bx+si],al
000003A2  0000              add [bx+si],al
000003A4  0000              add [bx+si],al
000003A6  48                dec ax
000003A7  833C06            cmp word [si],byte +0x6
000003AA  007427            add [si+0x27],dh
000003AD  B90400            mov cx,0x4
000003B0  0000              add [bx+si],al
000003B2  8A1C              mov bl,[si]
000003B4  06                push es
000003B5  30D3              xor bl,dl
000003B7  D0EB              shr bl,1
000003B9  881C              mov [si],bl
000003BB  06                push es
000003BC  48                dec ax
000003BD  83C002            add ax,byte +0x2
000003C0  E2F0              loop 0x3b2
000003C2  48                dec ax
000003C3  83E808            sub ax,byte +0x8
000003C6  48                dec ax
000003C7  8B0C              mov cx,[si]
000003C9  06                push es
000003CA  48                dec ax
000003CB  890C              mov [si],cx
000003CD  07                pop es
000003CE  48                dec ax
000003CF  83C008            add ax,byte +0x8
000003D2  EBD2              jmp short 0x3a6
