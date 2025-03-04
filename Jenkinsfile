pipeline {
    agent any  // Corre en cualquier agente disponible

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Dukeloko/PruebaDeRegrecion.git', branch: 'main'  // Reemplaza con tu repo
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh 'pip install -r requirements.txt || true'  // Si hay un archivo de dependencias
                sh 'pip install pytest'  // Asegura que pytest está instalado
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                sh 'pytest --junitxml=report.xml'  // Ejecuta las pruebas y genera reporte XML
            }
        }

        stage('Publicar Reporte') {
            steps {
                junit 'report.xml'  // Publica el reporte de pruebas en Jenkins
            }
        }
    }
}
