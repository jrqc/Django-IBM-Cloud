## Bluemix Deployment Script for Django Applications

* First you need to create your requirements.txt file to get ready for deployment

* Configure your Project's static file settings [get help ](https://docs.djangoproject.com/en/1.8/howto/static-files/)


* Add the management folder in one of your applications directory

* Run the command in your project folder:

  ```
  $ python manage.py bluemix_init {{app_name}}
  ```

  - {{app_name}} is the name of your python application on IBM Cloud


* Script will create manifest.yml, Procfile and runtime.txt(python version according to your environment).

* After running the script you are ready for deployment

```
$ cf api <API-endpoint>
$ cf login
$ cf push
```
