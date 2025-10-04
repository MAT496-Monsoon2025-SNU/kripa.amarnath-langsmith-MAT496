An Experiment is the action of running a specific version of your application's code against a defined dataset and applying 
evaluators to score the results.

1.Process:
  -Select a specific version of your application code (your "runnable" or "chain").
  -Select a Dataset (or a subset/split of it).
  -Execute the application for every example in the dataset.
  -Run the configured Evaluators on the resulting output.

2.Configuration: Experiments allow for configurable parameters like the number of repetitions or concurrent threads.

3.Output: An experiment generates a table of results, showing the score for every evaluator for every single example in the dataset.
