# Cross-platform Pico PSD

4 Hailo workload/window results available. See the inventory and metadata.

Legacy oscilloscope.npy is treated as stored power only after rate, index, duration, shape, and energy-integral checks. It is not converted back to current, and the Jetson voltage model is never applied to it.

The complete active interval and a first-duration-matched prefix are separate results. Longer recordings contribute more Welch averages, not more independent physical runs. Idle comes only from the same Hailo recording, never from Jetson. Missing idle stays active-only.

The NPY energy comparison checks internal consistency, not instrument calibration. Unknown measurement boundaries, setup settings, host contributions, and precision remain explicit. A visually different spectrum alone is not proof of an accelerator architecture effect.
