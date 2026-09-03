# Claim exclusion summary

Performance claim-eligible: 0; excluded rows: 4.
Energy claim-eligible: 0; excluded rows: 2.
Detailed and grouped counts represent one reason assignment per excluded claim-kind/source row. A source row with multiple explicit reasons therefore has multiple detail rows.

## Performance exclusions by primary reason

- `contract_fail_or_unavailable`: 2
- `screening_only`: 2

## Energy exclusions by primary reason

- `native_accuracy_gate_inconclusive`: 1
- `native_quality_claim_result_not_verified`: 1

## Grouped exclusions: model / backend / setup / reason

| Claim kind | Model | Backend | Setup | Reason | Count |
|---|---|---|---|---|---|
| performance | resnet50 | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | resnet50 | hailo8 | unknown_setup | contract_fail_or_unavailable | 1 |
| performance | resnet50 | tensorrt | orin_nx_hailo8_01 | screening_only | 2 |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_inconclusive | 1 |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | 1 |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |

## Per-dimension counts

| Claim kind | Dimension | Value | Count |
|---|---|---|---|
| performance | model | resnet50 | 4 |
| performance | backend | hailo8 | 2 |
| performance | backend | tensorrt | 2 |
| performance | setup | orin_nx_hailo8_01 | 3 |
| performance | setup | unknown_setup | 1 |
| performance | reason | contract_fail_or_unavailable | 2 |
| performance | reason | screening_only | 2 |
| energy | model | resnet50 | 4 |
| energy | backend | native_full_hailo8 | 2 |
| energy | backend | native_full_tensorrt | 2 |
| energy | setup | orin_nx_hailo8_01 | 4 |
| energy | reason | native_accuracy_gate_inconclusive | 1 |
| energy | reason | native_quality_claim_result_not_verified | 1 |
| energy | reason | screening_energy_policy_nonclaimable | 2 |

## Stable exclusion detail rows

| Claim kind | Model | Backend | Setup | Reason | Task | Case | Variant | Row status | Eligibility |
|---|---|---|---|---|---|---|---|---|---|
| performance | resnet50 | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | full | full | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8 | unknown_setup | contract_fail_or_unavailable | classification | full | full | available | contract_fail_or_unavailable |
| performance | resnet50 | tensorrt | orin_nx_hailo8_01 | screening_only | classification | b119 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_hailo8_01 | screening_only | classification | full | full | available | screening_only |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_inconclusive | classification | full | native_full_baseline | available | screening_only |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | classification | full | native_full_baseline | available | screening_only |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | classification | full | native_full_baseline | available | screening_only |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | classification | full | native_full_baseline | available | screening_only |

