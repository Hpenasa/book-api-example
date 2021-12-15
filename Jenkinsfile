pipeline{

	agent any
	options {
		buildDiscarder(logRotator(numToKeepStr: '5'))
	}
	environment {
		DOCKERHUB_CREDENTIALS = credentials ('dockerhub')
		THE_BUTLER_SAYS_SO=credentials('hpensa-aws-creds')
	}

	stages {

			
		stage('build') {
			steps {
				sh 'docker build -t hpenasa/alpine:latest .'
			}
		}
	    

		stage('Login'){
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push') {
			steps {
				sh 'docker push hpenasa/alpine:latest'
			}
		}

		stage('Run Docker container on remote hosts') {
             
            steps {
                sh "docker run -d -p 4000:4000 hpenasa/alpine"
 
            }
        }
	}
	post {
		always {
			sh 'docker logout'
		}
	}
}


	
