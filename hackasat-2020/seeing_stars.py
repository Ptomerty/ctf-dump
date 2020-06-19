import socket

global lastim
lastim = None

def solve(pts):
    global lastim
    pts = pts.split("\n")
    pts = [[int(x) for x in row.split(",")] for row in pts]

    import scipy.ndimage
    import numpy as np
    from PIL import Image

    def toim(raw_im):
        return Image.fromarray(np.clip(raw_im, 0, 255).astype(np.uint8))
        
    im = np.array(pts)/1.

    im2 = scipy.ndimage.gaussian_filter(im, sigma=1)

    thresh = im2.max() / 2

    mm = im2 > thresh
    im3 = 255. * mm
    lastim = toim(im)
    #toim(im).show()
    #toim(im2).show()
    #toim(im3).show()

    coords = []

    def succ(i,j):
        yield i+1,j
        yield i,j+1
        yield i-1,j
        yield i,j-1

    def dfs(m,i,j):
        mylist = [(i,j)]
        for nxt in succ(i,j):
            if nxt[0] in range(m.shape[0]) and nxt[1] in range(m.shape[1]):
                if m[nxt]:
                    m[nxt] = False
                    mylist.extend(dfs(m,*nxt))
        return mylist

    for i in range(mm.shape[0]):
        for j in range(mm.shape[1]):
            if mm[i,j]:
                mm[i,j] = False
                coords.append(dfs(mm,i,j))

    print(coords)
    centers = [max(pts, key = lambda x : im[x]) for pts in coords]

    #print()
    return "\n".join(",".join(map(str,pt)) for pt in centers)
# NB coords should be flipped before printing

ticket = "ticket{charlie63703whiskey:GA_ukR6dbCIK2IfswiJsV9EyiHkvSwe7eL6D0i3qyCsYssJxIqq0470n8pidO-uqsA}"
s = socket.socket()
s.settimeout(100)
s.connect(("stars.satellitesabove.me",5013))
print(s.recv(2048))
s.send((ticket+"\n").encode())

for _ in range(5):
    pts = ""
    while "empty line)" not in pts:
        pts += s.recv(2048).decode()
    pts = pts[:pts.find("Enter your answers")-1].strip()

    res = solve(pts)

    s.send((res+"\n\n").encode())

    print(s.recv(2048))

