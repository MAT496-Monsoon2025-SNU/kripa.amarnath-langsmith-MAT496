LangSmith uses specific Run Types to classify the different actions logged, which is essential for filtering, analysis, and targeted debugging.
The Run Types are given below:-
1.LLM:
     It records an explicit interaction with an external LLM. This captures the raw response, the prompt and is crucial for tracking model 
     usage and costs.
2.Chain:
       It's general purpose is to group a sequence of multiple steps of Runs. It acts as a container for logical flow and thus making it easy
       to read the Run Tree.
3.Retriever:
           It is useful in logging operations where the documents are fetched from a database or source. In RAG applications, it is critical 
           for diagnosing if the correct context is being returned.
4.Tool:
      It represents the execution of a specific capability or function external to the LLM (e.g., a search engine query or a code execution 
      call) often used by an Agent.
5.Prompt:
        It tracks the process of template hydration, where a template and its input variables are combined to generate the final text prompt
        sent to the LLM.
6.Parser:
        Logs steps dedicated to taking the raw, unstructured text output of an LLM and converting it into a structured format (like a JSON 
        object).
