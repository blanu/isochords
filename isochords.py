import itertools

i = 10000
# i = 10

harmonic_to_normal = {}
normals = []
octaves = {}
paths = {}

def normalize(x):
  current = x
  previous = x
  while current % 2 == 0:
    current //= 2
  return current

for x in range(1, i+1):
  nx = normalize(x)
  harmonic_to_normal[x] = nx
  if not nx in normals:
    normals.append(nx)

print("harmonic_to_normal: ", harmonic_to_normal)
print("normals: ", normals)

for nx in normals:
  octaves[nx] = [nx]
  for y in range (1, i):
    p = 2 ** y
    if p <= i:
      px = p * nx
      if px <= i:
        octaves[nx].append(px)

print("octaves: ", octaves)

for x in range(1, i):
  a = x
  b = x + 1
  normala = harmonic_to_normal[a]
  normalb = harmonic_to_normal[b]

  octavesa = octaves[normala]
  octavesb = octaves[normalb]

  if not normala in paths.keys():
    paths[normala] = {}

  for y in octavesa:
    for z in octavesb:
      distance = z - y
      if distance > 0 and distance <= i:
        if distance in paths[normala].keys():
          if not normalb in paths[normala][distance]:
            paths[normala][distance].append(normalb)
        else:
          paths[normala][distance] = [normalb]

print("paths: ", paths)

example = [1, 3, 7, 19]

isos = {}

for iso in range(1, i):
  isos[iso] = []
  for chordsize in range(2, len(example)):
    for combination in itertools.combinations(example, chordsize):
      isochord = True
      for index in range(len(combination) - 1):
        x = example[index]
        y = example[index + 1]

        nx = harmonic_to_normal[x]
        ny = harmonic_to_normal[y]

        if iso in paths[nx].keys():
          if ny in paths[nx][iso]:
            continue

        isochord = False
        break
      if isochord:
        isos[iso].append(combination)

todelete = []
for iso in isos.keys():
  if len(isos[iso]) == 0:
    todelete.append(iso)
for iso in todelete:
  del isos[iso]

print("isos: ", isos)