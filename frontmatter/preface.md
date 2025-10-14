# Preface {-}

Large language models are often explained as either equations without systems or systems without equations. *Inside the LLM* connects the two. It follows four recurring objects through the stack: the token that carries the data, the gradient that changes the model, the byte that pays the hardware cost, and the request that turns a model into a service.

The book begins with tensors and automatic differentiation, constructs a small Transformer, and then follows the same computation through training, kernels, distributed execution, inference serving, local deployment, retrieval, agents, interpretability, and research design. The examples intentionally separate mathematical mechanisms from framework conveniences so that readers can identify what must remain invariant when implementations change.

This working edition was developed with AI-assisted drafting, checking, and typesetting under the direction of the named authors. Automated checks establish structural coverage and executable invariants; they do not replace expert judgment. Technical claims should be evaluated against the cited primary sources and the reader's target software and hardware versions.

