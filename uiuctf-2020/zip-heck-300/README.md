# Zip Heck (300 pts)
### Author: Ptomerty

Challenge description:
```
I zipped up the flag a few times for extra security.

https://files.uiuc.tf/flag.zip

The intended solution runs in under 10 minutes on a typical computer.

Author: kuilin
```
Challenge files: [flag.zip](flag.zip)

## Gathering Info
In this challenge, we're provided a ZIP file and told to find the flag. First, let's confirm that we're working with a legitimate ZIP file and that no shenanigans are present:
```bash
$ file flag.zip
flag.zip: Zip archive data, at least v2.0 to extract
$ binwalk flag.zip
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 61368967, uncompressed size: 61350811, name: flag.zip
```
Okay, seems normal enough. Let's try unzipping it to see what horrors lie within:
```bash
$ unzip flag.zip
Archive:  flag.zip
made for uiuctf by kuilin
replace flag.zip? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: flag.zip
```
Like a matryoshka doll, it seems that unzipping our original `flag.zip` results in another, smaller `flag.zip`. Let's do a quick sanity check and compare the sizes of our files:
```
$ ls -l flag.zip orig.zip
-rwxrwxrwx 1 john john 61350811 Dec 31  1979 flag.zip
-rwxrwxrwx 1 john john 61369113 Jul 18 13:54 orig.zip
```
## Attempt 1: DigitalOcean Credits Go Brrrrr
At first glance, this challenge looked ez; write a bash loop that continuously extracted our ZIP until we're left with the center of our ZIP onion, which was hopefully our flag. I wrote a quick script and stuck it in a `screen` session, then headed off to sleep:
```bash
$ while true; do
7z e flag.zip -aou > /dev/null # extract to flag_1.zip, silence output
cp flag_1.zip flag.zip # if we stop script, we can recover
rm flag_1.zip          # either flag.zip or flag_1.zip
done
```
...only to wake up super disappointed. A full night's worth of unzipping had only reduced our `flag.zip` from 59,931 KB to 45,047 KB, and the latest iterations were only shaving off ~1 KB from the ZIP every few seconds.

Clearly, this solution was unsustainable. Let's roll up our sleeves and get down and dirty with the ZIP file format.

## Extracting ZIP's Secrets

In our modern "TBs aren't enough storage" world, an archive file is usually considered synonymous with a compressed file, with RAR, 7z, and ZIP files usually automatically compressing their contents using various algorithms. However, before compression methods were widespread, archive files existed primarily to *group* several files into one unique file, making file transfer easier. <sup>[Footnote](#fn1)</sup><a name="fn1r"></a>

Let's see what a ZIP file actually looks like by skimming the [Wikipedia page](https://en.wikipedia.org/wiki/Zip_(file_format)#Compression_methods). We note that ZIP supports a lot of compression methods, the most common of which is DEFLATE, but also supports a `STORE (no compression)` method. With that in mind, let's see what our flag file has to offer us, using a utility called `zipdetails`:

<details>
<summary><code>zipdetails -v</code> full output </summary>

```bash
$ zipdetails -v flag.zip

0000000 0000004 50 4B 03 04 LOCAL HEADER #1       04034B50
0000004 0000001 14          Extract Zip Spec      14 '2.0'
0000005 0000001 00          Extract OS            00 'MS-DOS'
0000006 0000002 00 00       General Purpose Flag  0000
                            [Bits 1-2]            0 'Normal Compression'
0000008 0000002 08 00       Compression Method    0008 'Deflated'
000000A 0000004 00 00 00 00 Last Mod Time         00000000 'Fri Nov 30 00:00:00 1979'
000000E 0000004 55 49 55 43 CRC                   43554955
0000012 0000004 87 6A A8 03 Compressed Length     03A86A87
0000016 0000004 9B 23 A8 03 Uncompressed Length   03A8239B
000001A 0000002 08 00       Filename Length       0008
000001C 0000002 00 00       Extra Length          0000
000001E 0000008 66 6C 61 67 Filename              'flag.zip'
                2E 7A 69 70
0000026 3A86A87 ...         PAYLOAD

3A86AAD 0000004 50 4B 01 02 CENTRAL HEADER #1     02014B50
3A86AB1 0000001 14          Created Zip Spec      14 '2.0'
3A86AB2 0000001 00          Created OS            00 'MS-DOS'
3A86AB3 0000001 14          Extract Zip Spec      14 '2.0'
3A86AB4 0000001 00          Extract OS            00 'MS-DOS'
3A86AB5 0000002 00 00       General Purpose Flag  0000
                            [Bits 1-2]            0 'Normal Compression'
3A86AB7 0000002 08 00       Compression Method    0008 'Deflated'
3A86AB9 0000004 00 00 00 00 Last Mod Time         00000000 'Fri Nov 30 00:00:00 1979'
3A86ABD 0000004 55 49 55 43 CRC                   43554955
3A86AC1 0000004 87 6A A8 03 Compressed Length     03A86A87
3A86AC5 0000004 9B 23 A8 03 Uncompressed Length   03A8239B
3A86AC9 0000002 08 00       Filename Length       0008
3A86ACB 0000002 00 00       Extra Length          0000
3A86ACD 0000002 00 00       Comment Length        0000
3A86ACF 0000002 00 00       Disk Start            0000
3A86AD1 0000002 00 00       Int File Attributes   0000
                            [Bit 0]               0 'Binary Data'
3A86AD3 0000004 00 00 00 00 Ext File Attributes   00000000
3A86AD7 0000004 00 00 00 00 Local Header Offset   00000000
3A86ADB 0000008 66 6C 61 67 Filename              'flag.zip'
                2E 7A 69 70

3A86AE3 0000004 50 4B 05 06 END CENTRAL HEADER    06054B50
3A86AE7 0000002 00 00       Number of this disk   0000
3A86AE9 0000002 00 00       Central Dir Disk no   0000
3A86AEB 0000002 01 00       Entries in this disk  0001
3A86AED 0000002 01 00       Total Entries         0001
3A86AEF 0000004 36 00 00 00 Size of Central Dir   00000036
3A86AF3 0000004 AD 6A A8 03 Offset to Central Dir 03A86AAD
3A86AF7 0000002 20 00       Comment Length        0020
3A86AF9 0000020 6D 61 64 65 Comment               'made for uiuctf by kuilin       '
                20 66 6F 72
                20 75 69 75
                63 74 66 20
                62 79 20 6B
                75 69 6C 69
                6E 00 00 00
                00 00 00 00
Done
```
</details>

&nbsp;
Whew! That's a lot of data, but we got a lot of information about our ZIP. First, we see that the header at the beginning of the file specifies the compression of the ZIP's internal payload. We can also see that our payload starts at 0x26 (38) bytes in, and that our footer takes up 108 bytes at the end (count 'em!). Using Python syntax, this means that any valid ZIP file's payload should be located at `file[38:-108]`. Perhaps we can extract the payload and do something with it.

Our flag.zip appears to be using "normal" compression (DEFLATE), which means that we won't have too much luck stripping out the ZIP payload, as we don't have an easy method of decompressing DEFLATE'd files. Hey, remember that unzipping program we left running overnight, though? Let's see what that file's compression looks like:


```bash
$ zipdetails -v save.zip

0000000 0000004 50 4B 03 04 LOCAL HEADER #1       04034B50
0000004 0000001 14          Extract Zip Spec      14 '2.0'
0000005 0000001 00          Extract OS            00 'MS-DOS'
0000006 0000002 00 00       General Purpose Flag  0000
0000008 0000002 00 00       Compression Method    0000 'Stored'
<output truncated>
```
Now we're talking! After unzipping for a certain amount of time, it looks like our ZIP files are just getting STORE'd recursively, with no additional compression applied. Theoretically, since we know the ZIP payload location, we can theoretically snip off many ZIP "layers" at once by modifying the file, instead of waiting for `unzip` to extract one layer at a time.

Let's inspect the raw hex of the file in `xxd` to check our hypothesis: (Note: `use xxd flag.zip | less` to avoid overloading your terminal with 50 MB of garbage)
```bash
00000000: 504b 0304 1400 0000 0000 0000 0000 5549  PK............UI
00000010: 5543 bb98 6402 bb98 6402 0800 0000 666c  UC..d...d.....fl
00000020: 6167 2e7a 6970 504b 0304 1400 0000 0000  ag.zipPK........
00000030: 0000 0000 5549 5543 2998 6402 2998 6402  ....UIUC).d.).d.
00000040: 0800 0000 666c 6167 2e7a 6970 504b 0304  ....flag.zipPK..
00000050: 1400 0000 0000 0000 0000 5549 5543 9797  ..........UIUC..
00000060: 6402 9797 6402 0800 0000 666c 6167 2e7a  d...d.....flag.z
00000070: 6970 504b 0304 1400 0000 0000 0000 0000  ipPK............
00000080: 5549 5543 0597 6402 0597 6402 0800 0000  UIUC..d...d.....
00000090: 666c 6167 2e7a 6970 504b 0304 1400 0000  flag.zipPK......
000000a0: 0000 0000 0000 5549 5543 7396 6402 7396  ......UIUCs.d.s.
000000b0: 6402 0800 0000 666c 6167 2e7a 6970 504b  d.....flag.zipPK
<output truncated>
```

We know from our Wikipedia browsing that ZIP files begin with the magic number `PK\x03\x04`, so we're probably seeing a lot of ZIP files, nested within each other. This fits with our earlier theory that a STORE ZIP holds its payload directly in the file. Theoretically, that means that if we cut the file at the final `PK\x03\x04` header and its corresponding footer, we can directly extract the payload from inside all these layers without unzipping it!

## Attempt 2: Manual Labor Always Works (Usually)

Let's test our theory out by manually cutting out a payload. In `save.zip`, we can scroll down to find our final `PK\x03\x04` header at location `0x827a`. Since we know the size of our header, we know that we have `0x827a / 38` or 879 nested ZIP headers and footers. Thus, we need to trim starting from byte `33402 (879 * 38)`, as well as cut off the final `94932 (879 * 108)` bytes. Since `save.zip` has a total size of `40147277` bytes, I ran the following `dd` command:
```bash
dd if=save.zip of=out.zip iflag=skip_bytes,count_bytes,fullblock \
    bs=4096 skip=33402 count=40018943
    # Note that 40147277 - 879 * (38 + 108) = 40018943
```
Let's inspect our `out.zip` to make sure our theory works:
```bash
$ zipdetails -v out.zip

0000000 0000004 50 4B 03 04 LOCAL HEADER #1       04034B50
0000004 0000001 14          Extract Zip Spec      14 '2.0'
0000005 0000001 00          Extract OS            00 'MS-DOS'
0000006 0000002 00 00       General Purpose Flag  0000
                            [Bits 1-2]            0 'Normal Compression'
0000008 0000002 08 00       Compression Method    0008 'Deflated'
```

Looks like we're not done extracting yet. We've successfully cut away 879 ZIP "wrappers", but our final payload seems like an actual compressed file, which we can't work our `dd` magic on. To make matters worse, our file size has barely changed, only decreasing by 128334 bytes to 40018943. Since we're working by hand, solving this challenge would result in us likely zipped up ourselves, but in a straitjacket.

Let's see what happens if we extract `out.zip` and inspect it with `xxd`: (don't forget `less`!)
```bash
00000000: 504b 0304 1400 0000 0000 0000 0000 5549  PK............UI
00000010: 5543 0132 6402 0132 6402 0800 0000 666c  UC.2d..2d.....fl
00000020: 6167 2e7a 6970 504b 0304 1400 0000 0000  ag.zipPK........
00000030: 0000 0000 5549 5543 6f31 6402 6f31 6402  ....UIUCo1d.o1d.
00000040: 0800 0000 666c 6167 2e7a 6970 504b 0304  ....flag.zipPK..
00000050: 1400 0000 0000 0000 0000 5549 5543 dd30  ..........UIUC.0
```

We lucked out! If we've got more STORE ZIPs inside our compressed ZIP, we can cut those away and only decompress when we encounter a DEFLATE ZIP.

## Attempt 3: Scripting Stonks 📈📈

We've established that our `flag.zip` files seem to be a recursive structure, usually made up of a few hundred STORE layers that contain a compressed DEFLATE ZIP. With this knowledge, let's establish a game plan for our desired behavior:

1. Given flag.zip, look for multiple `PK\x03\x04` headers.
    a. If we find multiple headers, our file has STORE layers. Cut the extra headers and footers off of the file to remove them.
    b. If we *don't* find many headers (1 or 2 are fine), our file has been compressed with DEFLATE. Extract the contents, which should yield more STORE layers.

With this plan, I wrote a Python script to automate the extraction process.
<details>
<summary><h2>Solution (click to open)</h2></summary>

This Python3 program opens an input file `flag.zip` then executes the plan we described above. First, we use regex on the bytes of the file to find all matches of `PK\x03\x04\x14\x00`, which should match our ZIP headers. <sup>[Footnote](#fn2)</sup><a name="fn2r"></a>

We take the number of matches we have and calculate where the final STORE header and footer is located, then slice it out of our bytearray. (Don't forget to subtract by 1, as Python is zero-indexed!) We should be left with a DEFLATE ZIP file in memory, which we can convert to a `ZipFile` object and decompress. Rinse and repeat as needed.

Every 250 iterations, we also save our current ZIP file to our filesystem, ensuring that if our process breaks we haven't lost all of the work we've already put in. If we encounter a file that can no longer be unzipped, this should be our flag!

My final output:
```bash
$ time python3 zipheck.py
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
Saving intermediary output...
b'uiuctf{tortoises_all_the_way_down}'

real    2m30.507s
user    2m13.005s
sys     0m16.040s
```

[The final script!](script.py)

</details>

### Flag: `uiuctf{tortoises_all_the_way_down}`

## Notes

<a name="fn1">1</a>: One example of archive files that we still see today is [`tar`](https://en.wikipedia.org/wiki/Tar_(computing)), which takes in multiple files as an input and outputs an single, uncompressed archive file. Nowadays, the `-z` option automagically compresses your tar archive using gzip., which is why you almost never see raw `.tar` files in practice, but rather compressed `.tar.gz` or `.tar.bz2` files. <sup>[Return](#fn1r)</sup>

<a name="fn2">2</a>: Yes, the ZIP header is techically only 4 bytes long. However, it's possible that a compressed payload could randomly have bytes `PK\x03\x04` that match a valid ZIP header.  I noted that the 2 bytes after the header were consistently equal to `\x14\x00` and extended my pattern to decrease the likelihood of having to manually fix invalid matches. <sup>[Return](#fn2r)</sup>