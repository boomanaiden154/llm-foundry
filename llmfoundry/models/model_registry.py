# Copyright 2022 MosaicML LLM Foundry authors
# SPDX-License-Identifier: Apache-2.0

from llmfoundry.models.hf import (ComposerHFCausalLM, ComposerHFPrefixLM,
                                  ComposerHFT5)
from llmfoundry.models.mpt import ComposerMPTCausalLM, ComposerMPTSequenceClassification

COMPOSER_MODEL_REGISTRY = {
    'mpt_causal_lm': ComposerMPTCausalLM,
    'mpt_sequence_classification': ComposerMPTSequenceClassification,
    'hf_causal_lm': ComposerHFCausalLM,
    'hf_prefix_lm': ComposerHFPrefixLM,
    'hf_t5': ComposerHFT5,
}
