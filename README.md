### ELK demo for the Platform Meetup

A dummy log generator together with the whole ELK stack.


### How to run it

```
docker compose up -d
```

Kibana needs an up and running Elasticsearch and Elasticsearch needs some time to start after the container is up. Because of this, we start the kibana container after the ES is up:


```
docker run --name kibana -e ELASTICSEARCH_URL=http://192.168.99.100:9200 -p 5601:5601 kibana
```

Where `192.168.99.100` is docker machine's IP. If you run Docker on native then you can use `localhost`.


### Resources

- Slides: https://docs.google.com/presentation/d/1WhIcb796_IldsT3TES5gQuE7NSnJfnlFqtQFwZ6ir1Q/edit?usp=sharing
- Book: https://www.logstashbook.com/
- Filebeat docs: https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-getting-started.html
- Logstash docs: https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html
- Elasticsearch docs: https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
- Kibana docs: https://www.elastic.co/guide/en/kibana/current/getting-started.html
- Grok deugger: http://grokdebug.herokuapp.com/
- Stage Monitor (thanks @maria): http://www.stagemonitor.org/
- Elast Alert (thanks @mihneadb): https://github.com/Yelp/elastalert
