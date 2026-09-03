# Claim exclusion summary

Performance claim-eligible: 0; excluded rows: 8.
Energy claim-eligible: 0; excluded rows: 3.
Detailed and grouped counts represent one reason assignment per excluded claim-kind/source row. A source row with multiple explicit reasons therefore has multiple detail rows.

## Performance exclusions by primary reason

- `contract_fail_or_unavailable`: 8

## Energy exclusions by primary reason

- `effective_command_window_not_verified`: 3

## Grouped exclusions: model / backend / setup / reason

| Claim kind | Model | Backend | Setup | Reason | Count |
|---|---|---|---|---|---|
| performance | yolov7_paper | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo8 | unknown_setup | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo8_to_tensorrt | unknown_setup | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | 2 |
| performance | yolov7_paper | tensorrt | unknown_setup | contract_fail_or_unavailable | 2 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | effective_command_window_not_verified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | final_energy_gate_not_passed | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | measurement_execution_failed | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_output_endpoint_not_verified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | postprocess_not_ok | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | raw_input_energy_not_primary | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | effective_command_window_not_verified | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | exact_runtime_work_units_missing | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | final_energy_gate_not_passed | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | measurement_execution_failed | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_not_passed | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | postprocess_not_ok | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | raw_input_energy_not_primary | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | effective_command_window_not_verified | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | final_energy_gate_not_passed | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | measurement_execution_failed | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | postprocess_not_ok | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | raw_input_energy_not_primary | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |

## Per-dimension counts

| Claim kind | Dimension | Value | Count |
|---|---|---|---|
| performance | model | yolov7_paper | 8 |
| performance | backend | hailo8 | 2 |
| performance | backend | hailo8_to_tensorrt | 2 |
| performance | backend | tensorrt | 4 |
| performance | setup | orin_nx_hailo8_01 | 4 |
| performance | setup | unknown_setup | 4 |
| performance | reason | contract_fail_or_unavailable | 8 |
| energy | model | yolov7_paper | 28 |
| energy | backend | hailo8_to_trt | 10 |
| energy | backend | native_full_hailo8 | 9 |
| energy | backend | native_full_tensorrt | 9 |
| energy | setup | orin_nx_hailo8_01 | 28 |
| energy | reason | effective_command_window_not_verified | 3 |
| energy | reason | exact_runtime_work_units_missing | 3 |
| energy | reason | final_energy_gate_not_passed | 3 |
| energy | reason | measurement_execution_failed | 3 |
| energy | reason | native_accuracy_gate_not_passed | 1 |
| energy | reason | native_output_endpoint_not_verified | 1 |
| energy | reason | native_quality_claim_result_not_verified | 2 |
| energy | reason | postprocess_not_ok | 3 |
| energy | reason | raw_input_energy_not_primary | 3 |
| energy | reason | scientific_primary_unavailable_or_unverified | 3 |
| energy | reason | screening_energy_policy_nonclaimable | 3 |

## Stable exclusion detail rows

| Claim kind | Model | Backend | Setup | Reason | Task | Case | Variant | Row status | Eligibility |
|---|---|---|---|---|---|---|---|---|---|
| performance | yolov7_paper | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8 | unknown_setup | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b066 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | unknown_setup | contract_fail_or_unavailable | detection | b066 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b066 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | unknown_setup | contract_fail_or_unavailable | detection | b066 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | unknown_setup | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | effective_command_window_not_verified | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | final_energy_gate_not_passed | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | measurement_execution_failed | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_output_endpoint_not_verified | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | postprocess_not_ok | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | raw_input_energy_not_primary | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | detection | b066 | native_split | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | effective_command_window_not_verified | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | exact_runtime_work_units_missing | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | final_energy_gate_not_passed | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | measurement_execution_failed | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_not_passed | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | postprocess_not_ok | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | raw_input_energy_not_primary | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | effective_command_window_not_verified | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | final_energy_gate_not_passed | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | measurement_execution_failed | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | postprocess_not_ok | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | raw_input_energy_not_primary | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | detection | full | native_full_baseline | measurement_failed | measurement_failed |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | detection | full | native_full_baseline | measurement_failed | measurement_failed |

