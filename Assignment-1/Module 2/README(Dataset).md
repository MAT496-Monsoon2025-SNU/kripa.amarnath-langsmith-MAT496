A Dataset is the fundamental unit for reproducible testing. It ensures that every time you modify your LLM application, you 
test the new version against the exact same set of inputs.

-Examples:
          A dataset is a collection of individual test cases called examples.Each example must contain the Input that is fed 
          into the application.It can optionally contain a Reference Output, which is the desired correct response. 
          This reference output is crucial for many types of automated evaluation.

-Purpose:
         To serve as a golden benchmark—a stable, trusted source of truth to measure performance changes (improvement or degradation) 
         over time.
