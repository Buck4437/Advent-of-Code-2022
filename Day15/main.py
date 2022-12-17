from aoc import *
from collections import defaultdict

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

int_in = ints(s, neg=True, lines=True)


class Region:

    def __init__(self, start, end, is_inverted=False):
        self.start = min(start, end)
        self.end = max(start, end)
        self.is_inverted = is_inverted

    def find_overlap(self, region2):
        s1, e1, s2, e2 = self.start, self.end, region2.start, region2.end
        if e1 < s2 or e2 < s1:
            return None
        return Region(max(s1, s2), min(e1, e2), not region2.is_inverted)

    def get_count(self):
        return (self.end - self.start + 1) * (-1 if self.is_inverted else 1)

    def contains(self, num):
        return self.start <= num <= self.end and not self.is_inverted

    def __str__(self):
        return f"{self.start}, {self.end}, {'-ve' if self.is_inverted else '+ve'}"


segments = []


def dst(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


regions = []
required_row = int(input("Enter required row number: "))
beacon_on_same_row = set()
scanner_on_same_row = set()

for x1, y1, bx, by in int_in:
    beacon_dst = dst(x1, y1, bx, by)
    delta = beacon_dst - abs(required_row - y1)
    if delta < 0:
        continue
    # Beacons and scanners
    if by == required_row:
        beacon_on_same_row.add(bx)

    if y1 == required_row:
        scanner_on_same_row.add(x1)

    region = Region(x1 - delta, x1 + delta)
    regions.append(region)

for x1 in scanner_on_same_row:
    regions.append(Region(x1, x1, False))

regions_no_overlap = []
for region in regions:
    new_regions = [region]
    for old_region in regions_no_overlap:
        overlap = region.find_overlap(old_region)
        if overlap is not None:
            new_regions.append(overlap)
    regions_no_overlap.extend(new_regions)

for bx in beacon_on_same_row:
    regions_no_overlap.append(Region(bx, bx, True))


count = sum([region.get_count() for region in regions_no_overlap])
print(count)
