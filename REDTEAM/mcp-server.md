# MCP Server



## Introduction

* MCP (Model Context Protocol) created by Antrophic.
* MCP gives LLM the limited access to do the thing(task). (Like a USB Cable from LLM).
* The LLM is clinet so normaly without MCP the user has to configuration APIs with the LLM for particular things.
* With MCP the user only configuration APIs in the MCP Servers and the LLM connect MCP.
* So there are the ways the MCP servers using Docker Desktop.
  * Register.yml -> is the refrences and the MCP Serves config.
* Every time use docker to RUN MCP SERVERs. Docker user the MCP Gateway. Then run the specific MCP Servers, it's using the standard input and output of MCP .json

{% code title="" overflow="wrap" %}
```
NetworkChuck's MCP Server Builder Prompt
INITIAL CLARIFICATIONS
Before generating the MCP server, please provide:
1. Service/Tool Name: What service or functionality will this MCP server provide?
2. API Documentation: If this integrates with an APl, please provide the documentation
URL
3. Required Features: List the specific features/tools you want implemented
4. Authentication: Does this require API keys, Auth, or other authentication?
5. Data Sources: Will this access files, databases, APls, or other data sources?

<Prompt>(I want to create a toggl mcp server. This will use the toggl api.)

If any information is missing or unclear, I will ask for clarification before proceeding.
```
{% endcode %}
