from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML con CSS moderno
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mayte Anchapanta - CI/CD</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 50px;
            max-width: 600px;
            width: 100%;
            text-align: center;
            animation: fadeIn 0.8s ease-in;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .emoji {
            font-size: 80px;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        h1 {
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        
        .badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin: 30px 0;
        }
        
        .badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }
        
        .links {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 30px;
        }
        
        .link-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-weight: bold;
            transition: transform 0.3s, box-shadow 0.3s;
            display: inline-block;
        }
        
        .link-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        
        .info {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin-top: 30px;
            text-align: left;
            border-radius: 5px;
        }
        
        .info p {
            margin: 5px 0;
            color: #555;
        }
        
        .footer {
            margin-top: 30px;
            color: #999;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">👩‍💻</div>
        <h1>¡Hola! Soy Mayte Anchapanta</h1>
        <p class="subtitle">Proyecto CI/CD con GitHub Actions & Docker</p>
        
        <div class="badges">
            <span class="badge">🐍 Python</span>
            <span class="badge">🐳 Docker</span>
            <span class="badge">⚙️ CI/CD</span>
            <span class="badge">🚀 Flask</span>
        </div>
        
        <div class="links">
            <a href="/saludo/Mayte" class="link-button">
                👋 Saludo Personalizado
            </a>
            <a href="/health" class="link-button">
                ❤️ Health Check
            </a>
            <a href="/info" class="link-button">
                ℹ️ Información del Proyecto
            </a>
        </div>
        
        <div class="footer">
            <p>✨ Desplegado con Render | Hecho con ❤️</p>
        </div>
    </div>
</body>
</html>
"""

SALUDO_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saludo - {{ nombre }}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 50px;
            max-width: 600px;
            width: 100%;
            text-align: center;
            animation: slideIn 0.5s ease-out;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        .emoji {
            font-size: 100px;
            margin-bottom: 20px;
            animation: wave 1s ease-in-out infinite;
        }
        
        @keyframes wave {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(20deg); }
            75% { transform: rotate(-20deg); }
        }
        
        h1 {
            color: #f5576c;
            font-size: 3em;
            margin-bottom: 20px;
        }
        
        .name {
            color: #f093fb;
            font-size: 2em;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .back-button {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            text-decoration: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-weight: bold;
            display: inline-block;
            margin-top: 30px;
            transition: transform 0.3s;
        }
        
        .back-button:hover {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">👋</div>
        <h1>¡Hola {{ nombre }}!</h1>
        <p class="name">Bienvenido/a a mi aplicación Flask</p>
        <p>✨ Desplegada con CI/CD automático</p>
        <a href="/" class="back-button">⬅️ Volver al inicio</a>
    </div>
</body>
</html>
"""

INFO_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Información del Proyecto</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 50px;
            max-width: 700px;
            width: 100%;
        }
        
        h1 {
            color: #4facfe;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .info-section {
            background: #f8f9fa;
            border-left: 4px solid #4facfe;
            padding: 20px;
            margin: 15px 0;
            border-radius: 5px;
        }
        
        .info-section h3 {
            color: #333;
            margin-bottom: 10px;
        }
        
        .info-section ul {
            list-style: none;
            padding-left: 0;
        }
        
        .info-section li {
            padding: 8px 0;
            color: #555;
        }
        
        .info-section li:before {
            content: "✓ ";
            color: #4facfe;
            font-weight: bold;
            margin-right: 10px;
        }
        
        .back-button {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            text-decoration: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-weight: bold;
            display: block;
            text-align: center;
            margin-top: 30px;
            transition: transform 0.3s;
        }
        
        .back-button:hover {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Información del Proyecto</h1>
        
        <div class="info-section">
            <h3>🎯 Características</h3>
            <ul>
                <li>Aplicación Flask en Python</li>
                <li>Containerizada con Docker</li>
                <li>CI/CD con GitHub Actions</li>
                <li>Tests automatizados con Pytest</li>
                <li>Desplegada en Render</li>
            </ul>
        </div>
        
        <div class="info-section">
            <h3>🔗 Endpoints Disponibles</h3>
            <ul>
                <li>/ - Página principal</li>
                <li>/saludo/&lt;nombre&gt; - Saludo personalizado</li>
                <li>/health - Health check</li>
                <li>/info - Esta página</li>
            </ul>
        </div>
        
        <div class="info-section">
            <h3>👩‍💻 Desarrollado por</h3>
            <ul>
                <li>Mayte Anchapanta</li>
                <li>Proyecto: CI/CD con GitHub Actions</li>
                <li>Tecnologías: Python, Flask, Docker, GitHub Actions</li>
            </ul>
        </div>
        
        <a href="/" class="back-button">⬅️ Volver al inicio</a>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    """Página principal con diseño moderno"""
    return render_template_string(HOME_TEMPLATE)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    """Saludo personalizado con diseño colorido"""
    return render_template_string(SALUDO_TEMPLATE, nombre=nombre)

@app.route('/health')
def health():
    """Health check endpoint con JSON"""
    return {
        'status': 'OK',
        'message': 'App funcionando correctamente',
        'version': '2.0',
        'author': 'Mayte Anchapanta'
    }

@app.route('/info')
def info():
    """Página de información del proyecto"""
    return render_template_string(INFO_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)