import struct


def f31(binary: bytes) -> dict:
    def struct_a(offset: int) -> dict:
        [a1] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1

        [length] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [link_str] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        a2 = str([struct.unpack('>' + str(length) + 's', binary[link_str: link_str + length])])[4:-4]

        [a3, a4, a5, a6] = struct.unpack('> B h i q',
                                         binary[offset: offset + 1 + 2 + 4 + 8])
        offset += 1 + 2 + 4 + 8

        [a7] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2

        [a8] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        return {
            'A1': a1,
            'A2': a2,
            'A3': a3,
            'A4': a4,
            'A5': a5,
            'A6': a6,
            'A7': struct_b(a7),
            'A8': struct_c(a8)
        }

    def struct_b(offset: int) -> dict:
        [b1] = struct.unpack('> Q', binary[offset: offset + 8])
        offset += 8

        [b2] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        return {
            'B1': b1,
            'B2': b2
        }

    def struct_c(offset: int) -> dict:
        [c1, c2] = struct.unpack('> f b', binary[offset: offset + 4 + 1])
        offset += 4 + 1
        [length] = struct.unpack('> L', binary[offset: offset + 4])
        offset += 4
        [link_list] = struct.unpack('> L', binary[offset: offset + 4])
        offset += 4
        list_links = [struct.unpack('> H', binary[link_list + i * 2: link_list + (i + 1) * 2])[0]
                      for i in range(length)]
        c3 = [struct_d(list_links[i]) for i in range(length)]
        return {
            'C1': c1,
            'C2': c2,
            'C3': c3
        }

    def struct_d(offset: int) -> dict:
        d1 = list(struct.unpack('> 8B', binary[offset: offset + 8]))
        offset += 8

        d2 = list(struct.unpack('> 5B', binary[offset: offset + 5]))
        offset += 5

        [d3] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1

        [d4] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4
        return {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4,
        }

    return struct_a(4)


print(f31(b'\x13PVI\x87\x00\x02\x00\x1e\xfd\xc2dz\x9c\x9a\xcd.\xdfk\xf9e\x06\xcd\xdb'
          b'\x00 \x00\x00\x00fbfp\x85\xf3\xaa>\x8e\xcb\x18\xb3X\x15\x13%\x86\xe9\xcc'
          b'g\x9f\xbb\xecaH\x8cH\x994\xb3\xa0\x84\xcf\r\xb9\tl\xf3\xf0\x03R\xd1\xaa'
          b'\xc3\xde{\xfdd\x80(\xe8k ~{\x16\x1f\xe00XC7-d\xe0\x04\xdd\x00*\x00<'
          b'\x00N\xbfBz\x88\xc2\x00\x00\x00\x03\x00\x00\x00`'))
