node {
    def success = true
    try {
        stage('Build') {
            checkout scm
            sh 'python setup.py sdist upload -r pypi'
        }
    } catch (e) {
        success = false
        currentBuild.result = "FAILED"
        throw e
    } finally {
        def result = success ? "succeeded" : "failed"
        mail body: "See ${currentBuild.absoluteUrl} for details", subject: "Hexahub build ${result}", to: 'xobb@citylance.biz'
    }
}