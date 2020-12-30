![Image](https://images.uncyclomedia.co/uncyclopedia/en/e/e2/Dumbo.GIF "icon")

Dumpo_Acuator-v1.0
======
**Dumpo_Acuator-1.0** is a reconnaissance tool for Acuator endpoints. Dumpo_Acuator-1.0 will query the Acuator endpoints for sensetive information and save it into a file. Spring boot is a framework module which provides Rapid Application Development feature to the Spring framework.  Acuator endpoints are in-built HTTP endpoints available for any boot application for different monitoring and management purposes. Unfortunatly if Acuator endpoints are misconfigured can allow sensetive information to leak in the internet. 

The tool interogates the following endpoints available:

1.  auditevents: Exposes audit events information for the current application. Requires an AuditEventRepository bean.
2.  beans:  Displays a complete list of all the Spring beans in your application.
3.  caches: Exposes available caches.
4.  conditions: Shows the conditions that were evaluated on configuration and auto-configuration classes and the reasons why they did or did not match.
5.  configprops:  Displays a collated list of all @ConfigurationProperties.
6.  env: Exposes properties from Spring Environment.
7.  flyway: Shows any Flyway database migrations that have been applied. Requires one or more Flyway beans.
8.  health: Shows application health information.
9.  httptrace: Displays HTTP trace information (by default, the last 100 HTTP request-response exchanges). Requires an HttpTraceRepository bean.
10. info: Displays arbitrary application info.
11. integrationgraph:  Shows the Spring Integration graph. Requires a dependency on spring-integration-core.
12. loggers: Shows and modifies the configuration of loggers in the application.
13. liquibase: Shows any Liquibase database migrations that have been applied. Requires one or more Liquibase beans.
14. metrics: Shows metrics information for the current application.
15. mappings: Displays a collated list of all @RequestMapping paths.
16. scheduledtasks: Displays the scheduled tasks in your application.
17. sessions: Allows retrieval and deletion of user sessions from a Spring Session-backed session store.
18. jolokia: Exposes JMX beans over HTTP (when Jolokia is on the classpath, not available for WebFlux). Requires a dependency on jolokia-core.
19. logfile: Returns the contents of the logfile (if logging.file.name or logging.file.path properties have been set). 
20. prometheus:  Exposes metrics in a format that can be scraped by a Prometheus server. Requires a dependency on micrometer-registry-prometheus.
21. threaddump:  Performs a thread dump.
22. hystrix.stream: Set of metrics it gathers about each HystrixCommand

## Download
* [Version 1.0](https://github.com/supremeLame/Dumpo_Acuator-.git)

## Usage
---
```
$ git clone https://github.com/username/software-project.git
$ chmod +x Dumpo_Acuator-v1.0
$ ./Dumpo_Acuator-v1.0 https://www.target.com
OR
$ ./Dumpo_Acuator-v1.0 httpss//www.target.com```

## Contributors
---
supremeLame

## License 
---

* This tool is released under the Apache License, Version 2.0 for more information please see [LICENSE](https://opensource.org/licenses/Apache-2.0) file

## Version 
---

* Version 1.0

## Contact
---

* Blog page: https://securityhorror.blogspot.com/
