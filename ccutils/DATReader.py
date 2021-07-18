import struct
import io

class cc1Reader:
    def process_raw_level(self, raw_level):
        if 'trap_controls' in raw_level:
            num_entries = len(raw_level['trap_controls']) // 10
            traps = {}
            raw_bytes = io.BytesIO(raw_level['trap_controls'])
            for _ in range(num_entries):
                button_x = struct.unpack("<H", raw_bytes.read(2))[0]
                button_y = struct.unpack("<H", raw_bytes.read(2))[0]
                trap_x = struct.unpack("<H", raw_bytes.read(2))[0]
                trap_y = struct.unpack("<H", raw_bytes.read(2))[0]
                _ = struct.unpack("<H", raw_bytes.read(2))[0] # open/closed, unused
                traps[(button_x, button_y)] = (trap_x, trap_y)
            raw_level['trap_controls'] = traps
        if 'clone_controls' in raw_level:
            num_entries = len(raw_level['clone_controls']) // 8
            cloners = {}
            raw_bytes = io.BytesIO(raw_level['clone_controls'])
            for _ in range(num_entries):
                button_x = struct.unpack("<H", raw_bytes.read(2))[0]
                button_y = struct.unpack("<H", raw_bytes.read(2))[0]
                cloner_x = struct.unpack("<H", raw_bytes.read(2))[0]
                cloner_y = struct.unpack("<H", raw_bytes.read(2))[0]
                cloners[(button_x, button_y)] = (cloner_x, cloner_y)
            raw_level['clone_controls'] = cloners
        if 'movement' in raw_level:
            num_entries = len(raw_level['movement']) // 2
            movement = []
            raw_bytes = io.BytesIO(raw_level['movement'])
            for _ in range(num_entries):
                monster_x = struct.unpack("<B", raw_bytes.read(1))[0]
                monster_y = struct.unpack("<B", raw_bytes.read(1))[0]
                movement.append((monster_x, monster_y))
            raw_level['movement'] = movement
        
        # map layers
        map = [list(list() for i in range(32)) for j in range(32)]
        for raw_layer in (raw_level["layer2"], raw_level["layer1"]):
            raw_bytes = io.BytesIO(raw_layer)
            index = 0
            while index < 32 * 32:
                next_byte = struct.unpack("<B", raw_bytes.read(1))[0]
                if next_byte == 0xFF: # run length encoding
                    length = struct.unpack("<B", raw_bytes.read(1))[0]
                    obj = struct.unpack("<B", raw_bytes.read(1))[0]
                    for _ in range(length):
                        map[index % 32][index // 32].append(obj)
                        index += 1
                else:
                    map[index % 32][index // 32].append(next_byte)
                    index += 1

        raw_level.pop('layer1')
        raw_level.pop('layer2')
        raw_level['map'] = map
    
    def process_raw_levelset(self, raw_levelset):
        raw_levelset=io.BytesIO(raw_levelset)
        _ = struct.unpack("<L", raw_levelset.read(4))[0] # magic number, unused
        num_levels = struct.unpack("<H", raw_levelset.read(2))[0]
        levelset = []
        for i in range(num_levels):
            level = {}
            level_size_bytes = struct.unpack("<H", raw_levelset.read(2))[0]

            level['number'] = struct.unpack("<H", raw_levelset.read(2))[0]
            level['time'] = struct.unpack("<H", raw_levelset.read(2))[0]
            level['chips'] = struct.unpack("<H", raw_levelset.read(2))[0]
            
            map_detail = struct.unpack("<H", raw_levelset.read(2))[0] # 0 or 1, map_detail, unused
            
            layer1_bytes = struct.unpack("<H", raw_levelset.read(2))[0]
            level['layer1'] = raw_levelset.read(layer1_bytes)
            layer2_bytes = struct.unpack("<H", raw_levelset.read(2))[0]
            level['layer2'] = raw_levelset.read(layer2_bytes)

            bytes_left = struct.unpack("<H", raw_levelset.read(2))[0]
            while bytes_left > 0:
                field = struct.unpack("<B", raw_levelset.read(1))[0]
                length = struct.unpack("<B", raw_levelset.read(1))[0]
                if field == 3:
                    level['title'] = raw_levelset.read(length)[:-1].decode('utf-8')
                elif field == 4:
                    level['trap_controls'] = raw_levelset.read(length)
                elif field == 5:
                    level['clone_controls'] = raw_levelset.read(length)
                elif field == 6:
                    level['password'] = ''.join([chr(b^0x99) for b in raw_levelset.read(length)[:-1]])
                elif field == 7:
                    level['hint'] = raw_levelset.read(length)[:-1].decode('utf-8')
                elif field == 10:
                    level['movement'] = raw_levelset.read(length)
                else:
                    raise ValueError("Encountered Unexpected Field " + str(field))
                bytes_left -= length + 2
            self.process_raw_level(level)
            levelset.append(level)
        return levelset

