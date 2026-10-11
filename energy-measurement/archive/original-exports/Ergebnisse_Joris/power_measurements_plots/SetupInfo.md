# Setup Info

### Adressen etc.

Rechner Adressen

- Host Rechner: `jwachsmuth@memmert` / `jwachsmuth@129.70.144.168`
- Bench Setup: (von memmert auch mit `ssh bench` erreichbar) `joris@10.42.0.210`, pswd: `joris@bench`
- Jetson NX@u.RECS: `nx@10.42.0.44`, pswd: `nx`

Memmert wichtige Ordner

- Speicherort Messdaten: `/media/jwachsmuth/satassd/power_measurements`
- Speicherort `urecs-data-collector` src: `/media/jwachsmuth/dataRec/RustroverProjects/urecs-data-collector`
- Speicherort skripte & power-calc-tool: `/media/jwachsmuth/dataRec/PycharmProjects/data_analysis`

Jetson NX relevante Dateien/Ordner

- `~/CLionProjects/untitled` (Interfaceprogramm src um Leistungsmessung von hailort zu übertragen)
- `~/hailoexec.sh`, `~/idle_gpio_trigger.sh`, `~/llm_launch.sh`, `~/random_yolo_execution.sh`, `~/modelfile` 
- `~/hpc`, `~/yolo`

Bench Setup relevante Dateien/Ordner

- `~/CLionProjects/untitled` (Interfaceprogramm src um Leistungsmessung von nvidia-smi zu übertragen)
- benchmark start-skripte ähnlich wie auf Jetson NX
- onnx und engine dateien liegen im home-verzeichnis

### Benchmark Durchführung

#### Allgemeines

- Alle Benchmarks werden mit `/media/jwachsmuth/dataRec/PycharmProjects/data_analysis/measurement_suite.py` ausgeführt.
- Benchmark Skript wird innerhalb einer tmux session ausgeführt
  - es sollte eine passende sitzung bereits aufgrund der vorherigen durchläufe offen sein
- Nach einem Durchlauf vom Skript müssen die Messdaten gesichert werden & speicherplatz für den nächsten Messdurchlauf freigemacht werden
  - Zum freimachen hat es bisher gereicht alle `.npy` Dateien zu löschen
- Jegliche Skripte werden mit `uv run [skript.py]` ausgeführt
  - venv wird automatisch verwendet und muss nicht separat aktiviert werden
- Die CLI Interfaces sollten im schnitt ganz gut dokumentiert sein, ABER bei den parametern für umgebung und messtyp ist die doku teilweise unvollständig. Fehlerhafte eingaben werden hier auch eher kryptisch als fehler markiert

#### Samplerate Sweep

`uv run measurement_suite.py --command “ssh bench [benchmark start befehl]” --measurement-path /media/jwachsmuth/satassd/power_measurements/[pfad_zum_speicherort] --run-count 15 --picoscope --picoscope-use-measured-voltages --pico-samplerate-sweep --picoscope-measurement-type [INA225|INA225NVGPU] --measurement-environment [nvgpu|jetson|m.2|static]` 

Die zu messenden Abtastraten werden mithilfe von Ordnernamen festgelegt, welche im `measurement-path` liegen: `[Abtastrate]Sps` 

zur visualisierung kann das skript `plot_sweep.py` verwendet werden

#### Duration Sweep

`uv run measurement_suite.py --command “ssh bench [benchmark start befehl]” --measurement-path /media/jwachsmuth/satassd/power_measurements/[pfad_zum_speicherort] --run-count 15 --picoscope --picoscope-use-measured-voltages --picoscope-samplerate 2000 --shelly --nv-gpu --duration-sweep`

Die zu messenden Laufzeiten werden mithilfe von Ordnernamen festgelegt, welche im `measurement-path` liegen: `[Laufzeit]s`

zur visualisierung kann das skript `plot_duration_sweep.py` verwendet werden (evtl muss da aber auf die labels geschaut werden, die haben die letzten male nicht ganz gepasst)

#### Benchmark Start-Befehle

Bei Befehlen, die eine Laufzeit als letzten Parameter haben wird dieser für Duration Sweeps weggelassen, da dieser vom `measurement_suite.py` Skript ausgefüllt wird

- `/home/joris/timed_engine_execution.sh [pfad zur .engine datei] [laufzeit in sekunden]`
  - nach der bestimmten laufzeit wird die ausführung abgebrochen
- `/home/joris/random_yolo_execution.sh [laufzeit in sekunden]` 
- `/home/joris/llm_launch.sh`  
  Jetson gemm fp32 → (ungetestet) laufzeit bei ungefähr 100 sekunden
- `/usr/src/tensorrt/bin/trtexec --loadEngine=/home/nx/hpc/pwgemmnet-fp32.engine --iterations=100 --useSpinWait`