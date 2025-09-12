import sys
import argparse
import sounddevice as sd
import numpy as np


start_idx = 0

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-d', '--device', default=None, type=int,
        help='Output device.'
    )
    parser.add_argument(
        '--normal', action='store_true',
        help='Enable this flag to hear audio in-phase.'
    )
    args = parser.parse_args()
    if args.device is None:
        print(sd.query_devices())
        exit()
    if sd.query_devices(args.device)["max_output_channels"] < 2:
        raise RuntimeError(
            f"Audio device incompatible: `{sd.query_devices(args.device)['name']}`."
        )
    if args.normal:
        phase_shift = 0
        print("No phase shift enabled.")
    else:
        phase_shift = 1

    try:
        FREQUENCY = 440  # Hz (4th octave A)
        samplerate = sd.query_devices(args.device, 'output')['default_samplerate']

        def callback(outdata, frames, time, status):
            if status:
                print(status, file=sys.stderr)
            global start_idx
            t = (start_idx + np.arange(frames)) / samplerate
            t = t.reshape(-1, 1)
            # 180 degrees out of phase
            mono_left = np.sin(2 * np.pi * FREQUENCY * t)
            mono_right = np.sin(2 * np.pi * FREQUENCY * t + phase_shift * np.pi)
            stereo_data = np.column_stack((mono_left, mono_right))
            outdata[:] = stereo_data
            start_idx += frames

        with sd.OutputStream(device=1, channels=2, callback=callback,
                            samplerate=samplerate):
            print('#' * 80)
            print('Press Return to quit!')
            print('#' * 80)
            input()
    except KeyboardInterrupt:
        print("Stopping due to KeyboardInterrupt!")
        exit()
    except Exception as e:
        print(f"Other exception: {e}")

if __name__ == "__main__":
    main()
