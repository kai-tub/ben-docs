---
jupytext:
  formats: ipynb,md_representations//md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python
  language: python
  name: python3
---

# Recommended Metrics

Here, we would like to provide a short overview of different metrics and give our opionated recommendations.

- For multi-label classification: AP (micro or macro)
- For image-retrieval: NDCG

Before we dive into the recommended metrics, a short reminder:
Almost all metrics (Precision, Recall, AP, mAP) are defined _differently_ in the multi-label vs image-retrieval domain!

In the multi-label classification we have:

$$ \begin{align*}
    \text{Precision} &= \frac{\text{TP}}{\text{TP} + \text{FP}} \\
    \text{Recall} &= \frac{\text{TP}}{\text{TP} + \text{FN}} \\
\end{align*}
$$

with:
- TP: True positive
- FP: False positive
- FN: False negative

For more information see the [wikipedia definition](https://en.wikipedia.org/wiki/Precision_and_recall) under the section titled `Definition (classification context)`!

:::{admonition} ToDo
We will add more information about image retrieval and the recommended metrics in the future.
:::

+++

## AP for Evaluation of Multi-Label Classification

:::{important}

Thank you Tom for writing this section!

:::

A common way of summarizing evaluation performance in terms of Precision and Recall within a single term is the F1 score. The F1 score can be interpreted as a harmonic mean of Precision and Recall, where an F1 score of 1 is related to optimal performance and a F1 score of 0 to worst performance, respectively. The relative contribution of Precision and Recall to the F1 score are equal. If multiple classes are considered (e.g., in Multi-Class Classification tasks like [CIFAR-10/100](https://www.cs.toronto.edu/~kriz/cifar.html) or [ImageNet](https://www.image-net.org/)) the F1 score is usually either evaluated class-based or globally, considered as macro or micro averaging (further reading on macro and micro averaging can be seen in [this micro/macro tutorial on Medium](https://towardsdatascience.com/micro-macro-weighted-averages-of-f1-score-clearly-explained-b603420b292f)).

Typically, when evaluating models that were trained on a Multi-Label Classification task like [BigEarthNet](https://bigearth.net/) or the multi-label version of the [COCO dataset](https://cocodataset.org/#home), these evaluation procedures are adopted. However, due to the requirement of being able to predict multiple classes at once, the softmax function that is applied in classification tasks with a single label such as Binary Classfication or Multi-Class Classification serving as a probabilty normalizer, has to be exchanged by a sigmoid function that enables multiple (positive) predictions at the same time.

The drawback of the sigmoid function is that the final predictions per class become disentangled. It may happen that the optimal decision boundary for some classes fall below 0.5. A consequence is that the F1 score (as well as Precision and Recall) that rely on a fixed prediction threshold falsely indicate bad performance for that class, while the inherent predictive power for that class is good, but just at a different scale. A solution to overcome the artefact of class-wise disentangled probabilities provides the metric [(mean) Average Precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html). It refers to the area under the [Precision-Recall curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#in-multi-label-settings) and is a more holistic approach for describing predictive power as it does not depend on a probability threshold. Likewise, as other metrics, the AP metric can be either computed by micro or macro averaging.

In many multi-label scenarios, F1 score and AP will highly correlate. But there exist scenarios in which the F1 score looses its descriptivity for predictive power due to scaling problems (e.g., under some type of multi-label noise), whereas the AP score maintains its descriptivity. An example can be found below in the [example section](f1_fail). Therefore, it is recommended to always report both F1 score and AP under micro and macro averaging. 

SciKit-Learn provides a predefined function [average_prevision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html) to calculate the AP.
By setting `average=None` the AP is calculated for each class and can be used in the multi-label classification scenario to better understand what class might be misbehaving.
The averaged AP is then defined by the specific averaging procedure (`macro`, `micro`, `samples`).

:::{important}

Do not forget to mention what averaging procedure was used!
Otherwise the reported metric has no value, as there is no way of knowing what the metric is _measuring_.

:::

### Summary
It is not uncommon that the optimal decision boundary of a multi-label classification model is _not_ 0.5 for all classes.
Metrics that rely on a fixed prediction threshold (Precision/Recall/F1) may report bad performance, even though the model can predict the class, just not at the threshold of 0.5.
AP do not rely on any threshold and give _robust_ estimates of the predictive power of the model.
When reporting a mean AP for multi-label classification the averaging procedure has to be included.

+++

(f1_fail)=
### Example of F1 score failure of describing predictive power

The following code shows an failure of the F1 score.
For simplicity, a single label classification task is reviewed but the argumentation also holds for multi-label classification.

```{code-cell} ipython3
import numpy as np
from sklearn.metrics import average_precision_score, f1_score

rng = np.random.default_rng(424)


def _print_scores(y_true, y_pred):
    print("AP:       {:.2f}".format(average_precision_score(y_true, y_pred)))
    print("F1-Score: {:.2f}".format(f1_score(y_true, y_pred > 0.5)))


y_true = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1]
```

Perfect Probability scaling:

Our awesome prediction model samples from a uniform distribution [0, 1].
In other words, the model does output over the entire range of possible probability values [0, 1].
We call this "perfect" probability scaling.

```{code-cell} ipython3
y_pred = rng.random(len(y_true))
_print_scores(y_true=y_true, y_pred=y_pred)
```

Bad Probability scaling:

Here, our random model is predicting values in the range [0, 0.6], which is equal to bad probability scaling.
This will probably not happen for _all_ classes in the multi-label classification scenario, but might happen to some!

We multiply the old `y_pred` value by a value < 1 to show that the F1-score will differ, while the AP will remain constant.
The AP does not require setting/tuning a threshold!
Tuning the threshold could also be seen as adjusting to the output probability scale of the model.
The specific value of the F1-score will differ; it doesn't matter if the value itself becomes larger/smaller than the previously shown score in the 'perfect probability scaling' example.

The important take-away is that the predictive power of the model is the same.
Only the output probability scale has changed.

```{code-cell} ipython3
y_pred_bad = y_pred * 0.6
_print_scores(y_true=y_true, y_pred=y_pred_bad)
```

```{code-cell} ipython3

```
