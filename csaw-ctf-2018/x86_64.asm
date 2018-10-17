00000000  FA                cli
00000001  B400              mov ah,0x0
00000003  B000              mov al,0x0
00000005  B80000B700        mov eax,0xb70000
0000000A  B300              mov bl,0x0
0000000C  BB0000B501        mov ebx,0x1b50000
00000011  B101              mov cl,0x1
00000013  B9000080FD        mov ecx,0xfd800000
00000018  017402EB          add [rdx+rax-0x15],esi
0000001C  01F4              add esp,esi
0000001E  80F900            cmp cl,0x0
00000021  7401              jz 0x24
00000023  F4                hlt
00000024  30F6              xor dh,dh
00000026  80E200            and dl,0x0
00000029  BAFFFFF7D2        mov edx,0xd2f7ffff
0000002E  83FA00            cmp edx,byte +0x0
00000031  75EA              jnz 0x1d
00000033  8ED8              mov ds,eax
00000035  8EC3              mov es,ebx
00000037  8EE1              mov fs,ecx
00000039  8EEA              mov gs,edx
0000003B  8ED0              mov ss,eax
0000003D  89CC              mov esp,ecx
0000003F  89D5              mov ebp,edx
00000041  89E6              mov esi,esp
00000043  89EF              mov edi,ebp
00000045  B80300CD10        mov eax,0x10cd0003
0000004A  B074              mov al,0x74
0000004C  B40E              mov ah,0xe
0000004E  CD10              int 0x10
00000050  B8557CEB10        mov eax,0x10eb7c55
00000055  61                db 0x61
00000056  63                db 0x63
00000057  4F53              push r11
00000059  0A0D20206279      or cl,[rel 0x7962207f]
0000005F  20456C            and [rbp+0x6c],al
00000062  796B              jns 0xcf
00000064  0089C6803C00      add [rcx+0x3c80c6],cl
0000006A  7409              jz 0x75
0000006C  8A04B4            mov al,[rsp+rsi*4]
0000006F  0E                db 0x0e
00000070  CD10              int 0x10
00000072  46EBF2            jmp short 0x67
00000075  EB09              jmp short 0x80
00000077  6C                insb
00000078  6F                outsd
00000079  6C                insb
0000007A  206B65            and [rbx+0x65],ch
0000007D  6B2000            imul esp,[rax],byte +0x0
00000080  BD777CB603        mov ebp,0x3b67c77
00000085  B20F              mov dl,0xf
00000087  B90700BB0F        mov ecx,0xfbb0007
0000008C  00B80113CD10      add [rax+0x10cd1301],bh
00000092  BE507DB442        mov esi,0x42b47d50
00000097  B280              mov dl,0x80
00000099  CD13              int 0x13
0000009B  EB55              jmp short 0xf2
0000009D  0D0A000000        or eax,0xa
000000A2  0000              add [rax],al
000000A4  2000              and [rax],al
000000A6  8D36              lea esi,[rsi]
000000A8  A37C89F7BB0A0031  mov [qword 0xd231000abbf7897c],eax
         -D2
000000B1  F7F3              div ebx
000000B3  83C230            add edx,byte +0x30
000000B6  88144E            mov [rsi+rcx*2],dl
000000B9  83F800            cmp eax,byte +0x0
000000BC  7402              jz 0xc0
000000BE  EBEF              jmp short 0xaf
000000C0  39FE              cmp esi,edi
000000C2  7504              jnz 0xc8
000000C4  C604304E          mov byte [rax+rsi],0x4e
000000C8  46803C0074        cmp byte [rax+r8],0x74
000000CD  185152            sbb [rcx+0x52],dl
000000D0  50                push rax
000000D1  31C9              xor ecx,ecx
000000D3  BAFFFFB486        mov edx,0x86b4ffff
000000D8  CD15              int 0x15
000000DA  58                pop rax
000000DB  5A                pop rdx
000000DC  59                pop rcx
000000DD  8A04B4            mov al,[rsp+rsi*4]
000000E0  0E                db 0x0e
000000E1  CD10              int 0x10
000000E3  46EBE3            jmp short 0xc9
000000E6  C3                ret
000000E7  89E8              mov eax,ebp
000000E9  E8BAFF89E0        call 0xffffffffe08a00a8
000000EE  E8B5FFC3B8        call 0xffffffffb8c400a8
000000F3  0100              add [rax],eax
000000F5  50                push rax
000000F6  E8ADFFE8EB        call 0xffffffffebe900a8
000000FB  FF                db 0xff
000000FC  B8020050E8        mov eax,0xe8500002
00000101  A3FFE8E1FFB80300  mov [qword 0x500003b8ffe1e8ff],eax
         -50
0000010A  E899FFE8D7        call 0xffffffffd7e900a8
0000010F  FF                db 0xff
00000110  B8040050E8        mov eax,0xe8500004
00000115  8F                db 0x8f
00000116  FF                db 0xff
00000117  E8CDFFB805        call 0x5b900e9
0000011C  0050E8            add [rax-0x18],dl
0000011F  85FF              test edi,edi
00000121  E8C3FF58E8        call 0xffffffffe85900e9
00000126  7EFF              jng 0x127
00000128  E8BCFF58E8        call 0xffffffffe85900e9
0000012D  77FF              ja 0x12e
0000012F  E8B5FF58E8        call 0xffffffffe85900e9
00000134  70FF              jo 0x135
00000136  E8AEFF58E8        call 0xffffffffe85900e9
0000013B  69FFE8A7FF58      imul edi,edi,dword 0x58ffa7e8
00000141  E862FFE8A0        call 0xffffffffa0e900a8
00000146  FF                db 0xff
00000147  E9B6E29090        jmp 0xffffffff9090e402
0000014C  90                nop
0000014D  90                nop
0000014E  90                nop
0000014F  90                nop
00000150  1000              adc [rax],al
00000152  0800              or [rax],al
00000154  006000            add [rax+0x0],ah
00000157  0001              add [rcx],al
00000159  0000              add [rax],al
0000015B  0000              add [rax],al
0000015D  0000              add [rax],al
0000015F  0000              add [rax],al
00000161  0000              add [rax],al
00000163  0000              add [rax],al
00000165  0000              add [rax],al
00000167  0000              add [rax],al
00000169  0000              add [rax],al
0000016B  0000              add [rax],al
0000016D  0000              add [rax],al
0000016F  0000              add [rax],al
00000171  0000              add [rax],al
00000173  0000              add [rax],al
00000175  0000              add [rax],al
00000177  0000              add [rax],al
00000179  0000              add [rax],al
0000017B  0000              add [rax],al
0000017D  0000              add [rax],al
0000017F  0000              add [rax],al
00000181  0000              add [rax],al
00000183  0000              add [rax],al
00000185  0000              add [rax],al
00000187  0000              add [rax],al
00000189  0000              add [rax],al
0000018B  0000              add [rax],al
0000018D  0000              add [rax],al
0000018F  0000              add [rax],al
00000191  0000              add [rax],al
00000193  0000              add [rax],al
00000195  0000              add [rax],al
00000197  0000              add [rax],al
00000199  0000              add [rax],al
0000019B  0000              add [rax],al
0000019D  0000              add [rax],al
0000019F  0000              add [rax],al
000001A1  0000              add [rax],al
000001A3  0000              add [rax],al
000001A5  0000              add [rax],al
000001A7  0000              add [rax],al
000001A9  0000              add [rax],al
000001AB  0000              add [rax],al
000001AD  0000              add [rax],al
000001AF  0000              add [rax],al
000001B1  0000              add [rax],al
000001B3  0000              add [rax],al
000001B5  0000              add [rax],al
000001B7  0000              add [rax],al
000001B9  0000              add [rax],al
000001BB  0000              add [rax],al
000001BD  0000              add [rax],al
000001BF  0000              add [rax],al
000001C1  0000              add [rax],al
000001C3  0000              add [rax],al
000001C5  0000              add [rax],al
000001C7  0000              add [rax],al
000001C9  0000              add [rax],al
000001CB  0000              add [rax],al
000001CD  0000              add [rax],al
000001CF  0000              add [rax],al
000001D1  0000              add [rax],al
000001D3  0000              add [rax],al
000001D5  0000              add [rax],al
000001D7  0000              add [rax],al
000001D9  0000              add [rax],al
000001DB  0000              add [rax],al
000001DD  0000              add [rax],al
000001DF  0000              add [rax],al
000001E1  0000              add [rax],al
000001E3  0000              add [rax],al
000001E5  0000              add [rax],al
000001E7  0000              add [rax],al
000001E9  0000              add [rax],al
000001EB  0000              add [rax],al
000001ED  0000              add [rax],al
000001EF  0000              add [rax],al
000001F1  0000              add [rax],al
000001F3  0000              add [rax],al
000001F5  0000              add [rax],al
000001F7  0000              add [rax],al
000001F9  0000              add [rax],al
000001FB  0000              add [rax],al
000001FD  0055AA            add [rbp-0x56],dl
00000200  F4                hlt
00000201  E492              in al,0x92
00000203  0C02              or al,0x2
00000205  E692              out 0x92,al
00000207  31C0              xor eax,eax
00000209  8ED0              mov ss,eax
0000020B  BC01608ED8        mov esp,0xd88e6001
00000210  8EC0              mov es,eax
00000212  8EE0              mov fs,eax
00000214  8EE8              mov gs,eax
00000216  FC                cld
00000217  66BF0000          mov di,0x0
0000021B  0000              add [rax],al
0000021D  EB07              jmp short 0x226
0000021F  90                nop
00000220  0000              add [rax],al
00000222  0000              add [rax],al
00000224  0000              add [rax],al
00000226  57                push rdi
00000227  66B90010          mov cx,0x1000
0000022B  0000              add [rax],al
0000022D  6631C0            xor ax,ax
00000230  FC                cld
00000231  F366AB            rep stosw
00000234  5F                pop rdi
00000235  26668D8500106683  lea ax,[es:rbp-0x7c99f000]
0000023D  C8032666          enter 0x2603,0x66
00000241  890526668D85      mov [rel 0xffffffff858d686d],eax
00000247  0020              add [rax],ah
00000249  6683C803          or ax,byte +0x3
0000024D  2666898500102666  mov [es:rbp+0x66261000],ax
00000255  8D8500306683      lea eax,[rbp-0x7c99d000]
0000025B  C8032666          enter 0x2603,0x66
0000025F  89850020578D      mov [rbp-0x72a8e000],eax
00000265  BD003066B8        mov ebp,0xb8663000
0000026A  0300              add eax,[rax]
0000026C  0000              add [rax],al
0000026E  2666890566050010  mov [rel es:0x100007dc],ax
00000276  0000              add [rax],al
00000278  83C708            add edi,byte +0x8
0000027B  663D0000          cmp ax,0x0
0000027F  2000              and [rax],al
00000281  72EB              jc 0x26e
00000283  5F                pop rdi
00000284  B0FF              mov al,0xff
00000286  E6A1              out 0xa1,al
00000288  E621              out 0x21,al
0000028A  90                nop
0000028B  90                nop
0000028C  0F011E            lidt [rsi]
0000028F  206066            and [rax+0x66],ah
00000292  B8A0000000        mov eax,0xa0
00000297  0F22E0            mov cr4,rax
0000029A  6689FA            mov dx,di
0000029D  0F22DA            mov cr3,rdx
000002A0  66B98000          mov cx,0x80
000002A4  00C0              add al,al
000002A6  0F32              rdmsr
000002A8  660D0001          or ax,0x100
000002AC  0000              add [rax],al
000002AE  0F30              wrmsr
000002B0  0F20C3            mov rbx,cr0
000002B3  6681CB0100        or bx,0x1
000002B8  00800F22C30F      add [rax+0xfc3220f],al
000002BE  0116              add [rsi],edx
000002C0  E260              loop 0x322
000002C2  EA                db 0xea
000002C3  58                pop rax
000002C4  61                db 0x61
000002C5  0800              or [rax],al
000002C7  0000              add [rax],al
000002C9  0000              add [rax],al
000002CB  0000              add [rax],al
000002CD  0000              add [rax],al
000002CF  0000              add [rax],al
000002D1  0000              add [rax],al
000002D3  009A20000000      add [rdx+0x20],bl
000002D9  0000              add [rax],al
000002DB  009200009000      add [rdx+0x900000],dl
000002E1  001A              add [rdx],bl
000002E3  00C7              add bh,al
000002E5  60                db 0x60
000002E6  0000              add [rax],al
000002E8  A5                movsd
000002E9  1F                db 0x1f
000002EA  B11F              mov cl,0x1f
000002EC  AB                stosd
000002ED  1F                db 0x1f
000002EE  A7                cmpsd
000002EF  1F                db 0x1f
000002F0  9F                lahf
000002F1  1F                db 0x1f
000002F2  091F              or [rdi],ebx
000002F4  B51F              mov ch,0x1f
000002F6  A31FD71F8F1FB31F  mov [qword 0x11fb31f8f1fd71f],eax
         -01
000002FF  1F                db 0x1f
00000300  0B1F              or ebx,[rdi]
00000302  0B1F              or ebx,[rdi]
00000304  D7                xlatb
00000305  1F                db 0x1f
00000306  FD                std
00000307  1F                db 0x1f
00000308  F3                rep
00000309  1F                db 0x1f
0000030A  C9                leave
0000030B  1F                db 0x1f
0000030C  D7                xlatb
0000030D  1F                db 0x1f
0000030E  A5                movsd
0000030F  1F                db 0x1f
00000310  B71F              mov bh,0x1f
00000312  8D1F              lea ebx,[rdi]
00000314  D7                xlatb
00000315  1F                db 0x1f
00000316  99                cdq
00000317  1F                db 0x1f
00000318  191F              sbb [rdi],ebx
0000031A  051FD71FB7        add eax,0xb71fd71f
0000031F  1F                db 0x1f
00000320  B51F              mov ch,0x1f
00000322  0F1FD7            hint_nop58 edi
00000325  1F                db 0x1f
00000326  B31F              mov bl,0x1f
00000328  011F              add [rdi],ebx
0000032A  8F                db 0x8f
0000032B  1F                db 0x1f
0000032C  8F                db 0x8f
0000032D  1F                db 0x1f
0000032E  0B1F              or ebx,[rdi]
00000330  851F              test [rdi],ebx
00000332  A31FD71F0B1FA31F  mov [qword 0xab1fa31f0b1fd71f],eax
         -AB
0000033B  1F                db 0x1f
0000033C  891F              mov [rdi],ebx
0000033E  D7                xlatb
0000033F  1F                db 0x1f
00000340  011F              add [rdi],ebx
00000342  D7                xlatb
00000343  1F                db 0x1f
00000344  DB1F              fistp dword [rdi]
00000346  091F              or [rdi],ebx
00000348  C3                ret
00000349  1F                db 0x1f
0000034A  93                xchg eax,ebx
0000034B  1F                db 0x1f
0000034C  0000              add [rax],al
0000034E  0000              add [rax],al
00000350  0000              add [rax],al
00000352  0000              add [rax],al
00000354  0000              add [rax],al
00000356  0000              add [rax],al
00000358  66B81000          mov ax,0x10
0000035C  8ED8              mov ds,eax
0000035E  8EC0              mov es,eax
00000360  8EE0              mov fs,eax
00000362  8EE8              mov gs,eax
00000364  8ED0              mov ss,eax
00000366  BF00800B00        mov edi,0xb8000
0000036B  B9F4010000        mov ecx,0x1f4
00000370  48B8201F201F201F  mov rax,0x1f201f201f201f20
         -201F
0000037A  F348AB            rep stosq
0000037D  BF00800B00        mov edi,0xb8000
00000382  4831C0            xor rax,rax
00000385  4831DB            xor rbx,rbx
00000388  4831C9            xor rcx,rcx
0000038B  4831D2            xor rdx,rdx
0000038E  B245              mov dl,0x45
00000390  80CA6C            or dl,0x6c
00000393  B679              mov dh,0x79
00000395  80CE6B            or dh,0x6b
00000398  20F2              and dl,dh
0000039A  B600              mov dh,0x0
0000039C  48BEE86000000000  mov rsi,0x60e8
         -0000
000003A6  48833C0600        cmp qword [rsi+rax],byte +0x0
000003AB  7427              jz 0x3d4
000003AD  B904000000        mov ecx,0x4
000003B2  8A1C06            mov bl,[rsi+rax]
000003B5  30D3              xor bl,dl
000003B7  D0EB              shr bl,1
000003B9  881C06            mov [rsi+rax],bl
000003BC  4883C002          add rax,byte +0x2
000003C0  E2F0              loop 0x3b2
000003C2  4883E808          sub rax,byte +0x8
000003C6  488B0C06          mov rcx,[rsi+rax]
000003CA  48890C07          mov [rdi+rax],rcx
000003CE  4883C008          add rax,byte +0x8
000003D2  EBD2              jmp short 0x3a6
