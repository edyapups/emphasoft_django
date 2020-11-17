
# emphasoft_django  
Тестовое задание для Emphasoft.  
  
## Задача  
  
> Необходимо сделать регистрацию юзеров с помощью social auth: Google  
> или Github на выбор.   После регистрации нужно попросить юзера  
> заполнить информацию о себе: ФИО, загрузить аватар и информацию о  
> себе. После заполнения, поля должны быть сохранены и выдаваться при  
> следующих открытиях страницы\авторизациях с возможностью  
> редактирования. >  
> Опционально: сделать страницу со списком всех  
> юзеров, зарегистрированных в системе и информацией о них.  
  
## Настройка  
  
 - Создать [файл переменных среды](https://github.com/joke2k/django-environ) формата:  
   

	    SECRET_KEY=secret-key    
	    ALLOWED_HOSTS=first.domain,second.domain    
	    DEBUG=True  
	    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=auth-key
	    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=auth-secret
	    DATABASE_URL=sqlite:///my-local-sqlite.db
