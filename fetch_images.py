import re, hashlib, pathlib, requests

OUT = pathlib.Path("assets/images/blogger")
OUT.mkdir(parents=True, exist_ok=True)

URL = re.compile(
    r'https?://(?:\d+\.bp\.blogspot\.com|blogger\.googleusercontent\.com'
    r'|lh\d+\.googleusercontent\.com)/[^\s"\'<>)]+')
EXT = {"image/jpeg": "jpg", "image/png": "png", "image/gif": "gif",
       "image/webp": "webp", "image/svg+xml": "svg"}
cache = {}

def full_size(u):
    u = re.sub(r'/(s\d+|w\d+-h\d+[^/]*)/', '/s0/', u)
    return re.sub(r'=[swh]\d+[^/]*$', '=s0', u)

def download(u):
    big = full_size(u)
    if big in cache:
        return cache[big]
    try:
        r = requests.get(big, timeout=60)
        r.raise_for_status()
    except Exception as e:
        print("FAILED", u, e)
        return None
    ext = EXT.get(r.headers.get("content-type", "").split(";")[0], "jpg")
    name = hashlib.md5(big.encode()).hexdigest()[:12] + "." + ext
    (OUT / name).write_bytes(r.content)
    cache[big] = "/assets/images/blogger/" + name
    return cache[big]

for f in pathlib.Path(".").rglob("*"):
    if f.suffix not in {".md", ".html", ".css", ".yml"} or ".git" in f.parts \
       or "_site" in f.parts:
        continue
    text = f.read_text(encoding="utf-8")
    new = URL.sub(lambda m: download(m.group(0)) or m.group(0), text)
    if new != text:
        f.write_text(new, encoding="utf-8")
        print("updated", f)