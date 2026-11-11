# Measurement and evaluation

**Proposed measurement design | MOE 0.3.0**

Measure a system of work, not individual worth. Do not rank engineers by agent count, tokens, lines of code, or unadjusted mission throughput.

| Measure | Operational definition | Important caveat |
| --- | --- | --- |
| Time to accepted delivery | Elapsed time from authorized mission revision to delivered candidate | Report waiting and active time; handle cancelled work separately |
| Human effort | Time spent specifying, supervising, reviewing, correcting, and operating the change | Faster generation can shift work into review |
| Review load | Review minutes, waiting time, queue size, and re-review cycles | Small PR counts alone can conceal fragmentation |
| Quality | Escaped defects and incidents, stratified by severity and observation period | Equal follow-up windows are needed |
| Control performance | Unauthorized attempts, prevented actions, successful violations, and evidence gaps | Zero observed violations does not prove zero risk |
| Total cost | Human effort plus model, compute, integration, and operational costs | State costing assumptions; do not invent savings |
| Outcome attainment | Intended user or business effect observed by the agreed date | Delivery may precede an observable effect |
| Maintainability | Rework, understandability, and support burden after delivery | Needs longer observation than an initial demo |

## Throughput without a vanity metric

Report **accepted-delivery throughput** as the count of technically accepted and delivered missions in a defined interval and comparable work class. Report **outcome-confirmed throughput** separately as the count whose agreed outcome was observed. Neither count is a universal measure of business value.

If the label Verified Value Throughput is used, define its numerator, denominator, outcome criterion, observation window, and work classes explicitly. Do not sum arbitrary mission counts across teams or use subjective value weights as objective evidence.

## Comparison design

Use a baseline and a predeclared comparison, preferably matched changes or randomized assignment when appropriate and feasible. Compare similar risk, complexity, product context, and engineers' familiarity. Report sample size, distributions, medians, spread, and uncertainty instead of only a single percentage.

Include failed, abandoned, and superseded missions. Track policy, model, tool, and process revisions. Avoid causal claims from uncontrolled before-and-after changes. A short pilot can justify another experiment without establishing broad superiority.

## Expansion decision

Agree tolerances before the pilot. Expand only when observed benefits are useful and quality, security, cost, and human attention remain within those limits. Report uncertainty and contradictions. A negative result is useful learning, not a reason to hide the evidence.
