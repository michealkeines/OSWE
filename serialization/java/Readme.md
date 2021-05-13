Reflection is a language's ability to inspect and dynamically call classes, methods, attributes, etc. at runtime.

Dynamic proxies allow one single class with one single method to serve multiple method calls to arbitrary classes with arbitary number of methods, it routes all method invocations to a single handler - invoke() method

It can be used in the cases where concrete class implementations won't be known untill runtime



