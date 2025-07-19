
import os
import shutil

# 📍 MODIFIE cette variable pour mettre le chemin ABSOLU ou RELATIF vers ton dossier cloné
cloned_frontend_path = r"C:/Users/admin\Downloads\WebScrapBook\data/20250702113024191"

# Dossiers source dans ton dossier cloné
src_css = os.path.join(cloned_frontend_path, 'css')
src_js = os.path.join(cloned_frontend_path, 'js')
src_images = os.path.join(cloned_frontend_path, 'images')
src_logos = os.path.join(cloned_frontend_path, 'logos')  # si logos est séparé

# Dossier destination dans le projet Flask
dst_static = os.path.join('app', 'static')
dst_templates = os.path.join('app', 'templates')

# Fonction utilitaire
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def copy_files(src_dir, dst_dir, allowed_exts=None):
    if not os.path.exists(src_dir):
        print(f"[⚠] Dossier introuvable : {src_dir}")
        return

    ensure_dir(dst_dir)
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename)

        if os.path.isfile(src_file):
            ext = filename.split('.')[-1].lower()
            if allowed_exts and ext not in allowed_exts:
                continue
            shutil.copy2(src_file, dst_file)
            print(f"[✔] Copié: {src_file} -> {dst_file}")

def copy_html_files():
    for root, _, files in os.walk(cloned_frontend_path):
        for file in files:
            if file.endswith('.html'):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_templates, file)
                ensure_dir(os.path.dirname(dst_file))
                shutil.copy2(src_file, dst_file)
                print(f"[✔] Copié HTML: {src_file} -> {dst_file}")

def main():
    print("\n[🔄] Organisation du frontend cloné vers l’arborescence Flask...\n")

    copy_html_files()
    copy_files(src_css, os.path.join(dst_static, 'css'), allowed_exts=['css'])
    copy_files(src_js, os.path.join(dst_static, 'js'), allowed_exts=['js'])
    copy_files(src_images, os.path.join(dst_static, 'images'))
    copy_files(src_logos, os.path.join(dst_static, 'images', 'logos'))

    print("\n[✅] Frontend intégré dans Flask avec succès.\n")

if __name__ == "__main__":
    main()