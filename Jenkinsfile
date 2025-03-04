pipeline {
    agent any  // Corre en cualquier agente disponible

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Dukeloko/PruebaDeRegrecion.git', branch: 'main'  
            }
        }

        stage('Configurar Entorno Virtual') {
            steps {
                bat 'python -m venv venv'  // Crear entorno virtual en Windows
                bat 'venv\\Scripts\\activate'  // Activar el entorno virtual en Windows
            }
        }

        stage('Instalar Dependencias') {
            steps {
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'  // Instalar dependencias
                bat 'venv\\Scripts\\activate && pip install pytest'  // Asegurar que pytest esté instalado
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                bat 'venv\\Scripts\\activate && pytest src/ --junitxml=report.xml'  // Ejecutar pruebas con pytest
            }
        }

        stage('Publicar Reporte') {
            steps {
                junit 'report.xml'  // Publicar el reporte de pruebas en Jenkins
            }
        }
    }
}
