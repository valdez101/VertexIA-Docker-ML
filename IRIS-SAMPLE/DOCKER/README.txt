
##Comando de extracción del docker

Usa estos comandos con el cliente de Docker para extraer la imagen. Si quieres usar estos comandos, el cliente de Docker debe estar configurado para 
autenticarse con us-east1-docker.pkg.dev. Si es la primera vez que extraes una imagen de us-east1-docker.pkg.dev con tu cliente de Docker, ejecuta el 
siguiente comando en la máquina en la que se instaló Docker.

    gcloud auth configure-docker us-east1-docker.pkg.dev

--EJECUTAR EN CLOUD SHELL

    docker pull \
        us-east1-docker.pkg.dev/tottus-ml-iris/tottus-repo-new/iris_image:latest


--EJECUTAR EN CLOUD SHELL

    Extrae por resumen

    docker pull \
        us-east1-docker.pkg.dev/tottus-ml-iris/tottus-repo-new/iris_image@sha256:f1461255b2d466719d12325328ba6d42033801a5e2b68b523594ac2e5064ef4e

--EJECUTAR EN CLOUD SHELL