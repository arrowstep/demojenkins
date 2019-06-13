node {
	
	checkout([$class: 'GitSCM', branches: [[name: '*/master']],
		  userRemoteConfigs: [[url: 'https://github.com/arrowstep/demojenkins.git']]])
	stage('Build image') {
  		
		sh 'docker build -t healthdemo/img .'
	}
	
	stage('First step') {
			sh 'uptime'
	}
	
}

