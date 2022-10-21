
we are using this because the operation for sending notification through the http request will be more than 30 seconds, also the business logic transactions will be taking more than 40% and 50% of the server resources. as a result we need to bring it to a background process i.e (Azure queue and and functions). I am going for Queue background Job because each of my transaction does not need an immediate execution. and lastly our application can be run in another process outside of the main UI application and Moving these tasks out of the UI application will result in faster response time, scalable architecture, and better user experience.



Azure Functions monthly cost is $0 monthly
Azure Database for PostgreSQL cost $127.90 Average per month and storage of $10.58 per month making the total of $138.47 per month

App Service cost Monthly: $54.75

Storage account cost Monthly: $21.84
