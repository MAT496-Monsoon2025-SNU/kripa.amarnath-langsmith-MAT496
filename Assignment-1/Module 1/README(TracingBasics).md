1. Tracing Basics
   Tracing is a foundational concept in LangSmith. Tracing can be defined as the way how you record, structure and visualize
   every action in your LLM. Another term that goes hand in hand is Run. A run is a single unit of work within your application.
   Every function call, model invoke, or retrieval is a Run.
   A Run captures the following data:-
     .Name
     .Input/Output
     .Run Type
     .Latency
     .Metadata
     .Feedback
   A Trace is the complete hierarchical view of a single request-response cycle. It is also known as a Run Tree, this shows how smaller Runs
   are nested within each other. This tree is essential for debugging.
   A project is the top level organizational container. It groups a collection of traces together. This collection represents a
   specific application or deployment environment. 
