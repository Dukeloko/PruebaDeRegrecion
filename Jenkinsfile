pipeline {
    agent any  // Corre en cualquier agente disponible

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Dukeloko/PruebaDeRegrecion.git', branch: 'main'  // Reemplaza con tu repo
            }
        }

        stage('Configurar Entorno Virtual') {
            steps {
                sh 'python -m venv venv'  // Crea el entorno virtual
                sh 'source venv/bin/activate'  // Activa el entorno virtual
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh '. venv/bin/activate && pip install -r requirements.txt || true'  // Instala dependencias
                sh '. venv/bin/activate && pip install pytest'  // Asegura que pytest está instalado
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                sh '. venv/bin/activate && pytest src/ --junitxml=report.xml'  // Ejecuta pytest en la carpeta src/
            }
        }

        stage('Publicar Reporte') {
            steps {
                junit 'report.xml'  // Publica el reporte de pruebas en Jenkins
            }
        }
    }
}
