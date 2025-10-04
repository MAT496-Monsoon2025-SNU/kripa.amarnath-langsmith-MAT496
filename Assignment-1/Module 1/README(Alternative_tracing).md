While frameworks like LangChain and LangGraph integrate tracing automatically, the slides describe several ways to instrument code,
depending on the level of control and the underlying framework. The various tracing methods and it's uses are given below.

1.@traceable Decorator:
             This is the most common and recommended method. You simply place the decorator on any Python function. It automatically handles
             the creation of the Run, logs the function's arguments as Input, and logs the function's return value as Output, while correctly 
             nesting the Run within the overall Trace.

2.with trace(): Context Manager:
               Use this when you only need to trace a specific block of code within a function, or when you cannot use a decorator 
               (e.g., on a lambda function). It allows you to explicitly define the boundaries and details of the Run being logged.

3.wrap_openai(): 
               A helper function used when you are calling the OpenAI SDK directly (outside of LangChain) but still want those API
               calls logged in LangSmith as LLM type Runs.

4.RunTree Object: 
                This provides the lowest level of control. By manually creating and managing a RunTree object, you can precisely 
                control when a Run starts, what data is logged, and when it ends. This is necessary for highly customized integrations or 
                when you need the run_id for asynchronous logging.
