import os
import sys

def create_antigravity_app(app_name):
    base_dir = os.path.join('core', app_name)
    
    # Definición de la estructura basada en la Regla Global
    folders = [
        'models',
        'views',
        'services',
        'selectors',
        'signals',
        'migrations',
        f'templates/{app_name}'
    ]
    
    files = {
        'models/__init__.py': '',
        'views/__init__.py': '',
        'forms.py': '# Define tus formularios aquí\nfrom django import forms\n',
        'urls.py': f'from django.urls import path\n\napp_name = "{app_name}"\n\nurlpatterns = []\n',
        'admin.py': 'from django.contrib import admin\n',
        'apps.py': f'from django.apps import AppConfig\n\nclass {app_name.capitalize()}Config(AppConfig):\n    name = "core.{app_name}"\n'
    }

    if not os.path.exists('core'):
        os.makedirs('core')

    if os.path.exists(base_dir):
        print(f"❌ Error: La app '{app_name}' ya existe en core/.")
        return

    # Crear carpetas
    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)
        # Crear __init__.py en carpetas de lógica para que sean paquetes
        if folder not in ['migrations', 'templates']:
            with open(os.path.join(base_dir, folder, '__init__.py'), 'w') as f:
                f.write('')

    # Crear archivos base
    for file_path, content in files.items():
        with open(os.path.join(base_dir, file_path), 'w') as f:
            f.write(content)

    print(f"✅ App '{app_name}' creada exitosamente en core/{app_name}")
    print(f"👉 No olvides añadir 'core.{app_name}' a INSTALLED_APPS en settings.py")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python start_app.py [nombre_de_la_app]")
    else:
        create_antigravity_app(sys.argv[1])
        