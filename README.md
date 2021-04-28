# weather_report

**created using django framework**

1) similarity calculator was done using python inbuilt difflib

2) ratio above 50% weather matching cities has been returned

3) Cities took: mumbai, delhi, bangalore, hyderabad, ahemdabad, chennai, kolkata, surat, pune, jaipur

urls: 
      
      GET /weather/collect_data -- which collects the data and stores into slite3
      GET /weather/get_result -- calculatest the similarity and return the json
      
