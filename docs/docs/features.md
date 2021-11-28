# Features

As a django sidecar, it should:

[TOC]

## Request client

Give a request client.

通过 request client，我们可以知道该请求来自某一个微服务。
可以通过该 Client 隐藏一些复杂的细节：

1. 服务的可用性；
2. 自定义的请求头部
3. 自动检测该方法是否存在，该服务是否存在；
4. 尝试使用 DSL 的方式定义接口；
5. etc.

## Record every request

Record every request.

记录每一个请求用于链路溯源

## Proxy

通过 Proxy 允许远程访问