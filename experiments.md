\# Experiments: exp/shahzad-depth-trees



Baseline (max\_depth=6, n\_estimators=100): accuracy = 0.8887, f1\_macro = 0.8869



Only `train.max\_depth` and `train.n\_estimators` changed. Same seed (42) and same split.



| Experiment       | accuracy | f1\_macro | n\_estimators | max\_depth |

|------------------|----------|----------|--------------|-----------|

| depth10          | 0.9417   | 0.9410   | 100          | 10        |

| depth20          | 0.9620   | 0.9616   | 100          | 20        |

| trees200         | 0.8911   | 0.8894   | 200          | 6         |

| depth20-trees20  | 0.9524   | 0.9518   | 20           | 20        |



Best run: `depth20` (max\_depth=20, n\_estimators=100) with accuracy = 0.9620 and f1\_macro = 0.9616.

Depth drove the improvement; more trees at depth 6 added almost nothing.



This branch is exploration only and is never merged. The winner is re-applied on `feat/tune-random-forest`.

