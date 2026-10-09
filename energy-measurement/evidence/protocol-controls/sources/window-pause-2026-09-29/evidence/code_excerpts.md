# Analyzer code excerpts

Source S01: snapshot at review time, not proof of every historical build. Whole-member SHA-256 refers to original complete files.

## source_snapshot/analysis_tool/power_calculations/src/args.rs

SHA-256: `e80b974f6ee730485ff0f86b49139dab7c594b6d7afb2a3384a98df0458e780b`

```text
100:     type Err = String;
101: 
102:     fn from_str(s: &str) -> Result<Self, Self::Err> {
103:         match s.to_lowercase().as_str() {
104:             "ucurrent" => Ok(OscilloscopeMsmtType::UCurrent),
105:             "currentranger" => Ok(OscilloscopeMsmtType::CurrentRanger),
106:             "ina225" => Ok(OscilloscopeMsmtType::INA225),
107:             "ina225nvgpu" => Ok(OscilloscopeMsmtType::INA225),
108:             _ => Err(format!("String {s} is invalid")),
109:         }
110:     }
111: }
```

## source_snapshot/analysis_tool/power_calculations/src/data_reading_types.rs

SHA-256: `ada127f16770aabcab3ec888f67f2100f411a2454ee62e6fea58864318d50e0f`

```text
279:     pub(crate) fn fit_start_stop_to_duration(&self, initial_start_idx: usize, initial_stop_idx: usize, duration: f64, samplerate_opt: Option<f64>) -> (usize, usize) {
280:         let actual_duration = self.duration(Some((initial_start_idx, initial_stop_idx)), samplerate_opt);
281:         info!("Duration {actual_duration}");
282:         let duration_diff = duration - actual_duration;
283:         /*if duration_diff.abs() > duration * 0.1 {
284:             info!("Stopping fitting, duration deviation is too big");
285:             // if the difference between start and end is too big - this is done so external programs can detect that the measurement is not valid
286:             return (initial_start_idx, initial_stop_idx);
287:         }*/
288:         match self {
289:             PowerVec::Constant(data) => {
290:                 let samplerate = samplerate_opt.unwrap();
291:                 let sample_offset = ((duration_diff / 2.) * samplerate).round() as i64;
292:                 let start_idx = if initial_start_idx as i64 - sample_offset < 0 {
293:                     0
294:                 } else {
295:                     initial_start_idx as i64 - sample_offset
296:                 };
297:                 let stop_idx = if sample_offset + initial_stop_idx as i64 >= data.len() as i64 {
298:                     (data.len() - 1) as i64
299:                 } else {
300:                     initial_stop_idx as i64 + sample_offset
301:                 };
302:                 (start_idx as usize, stop_idx as usize)
303:             }
```

Analyzer alias only: do not change the collector input profile. The fitter moves detected boundaries to a requested duration; its large-deviation guard is commented out in this snapshot.
