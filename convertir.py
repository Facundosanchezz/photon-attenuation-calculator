import json, glob, os

base = os.path.join(os.path.expanduser("~"), ".claude", "projects")
carpetas = glob.glob(os.path.join(base, "*calculadora-atenuacion*"))
if not carpetas:
    print("No encontré la carpeta de sesiones")
    raise SystemExit
archivos = glob.glob(os.path.join(carpetas[0], "*.jsonl"))

def texto(contenido):
    if isinstance(contenido, str):
        return contenido
    partes = []
    for bloque in contenido:
        if isinstance(bloque, dict) and bloque.get("type") == "text":
            partes.append(bloque.get("text", ""))
    return "\n".join(partes)

sesiones = []
for ruta in archivos:
    mensajes = []
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            try:
                d = json.loads(linea)
            except ValueError:
                continue
            if d.get("type") not in ("user", "assistant"):
                continue
            t = texto(d.get("message", {}).get("content", ""))
            if t.strip():
                mensajes.append((d.get("timestamp", ""), d["type"], t))
    if mensajes:
        sesiones.append((mensajes[0][0], mensajes))
sesiones.sort()

usuario = os.path.expanduser("~")
os.makedirs("devpost", exist_ok=True)
with open(os.path.join("devpost", "historial-conversacion.md"), "w", encoding="utf-8") as out:
    for i, (_, mensajes) in enumerate(sesiones, 1):
        out.write(f"\n# Sesión {i}\n\n")
        for ts, rol, t in mensajes:
            quien = "Yo" if rol == "user" else "Claude Code"
            out.write(f"**{quien}** ({ts[:16]}):\n\n{t.replace(usuario, '<usuario>')}\n\n---\n")
print("Listo:", len(sesiones), "sesiones")