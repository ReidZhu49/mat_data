import h5py


def read_hdf5_data(file_name):
    with h5py.File(file_name, 'r') as h5file:
        frame_count = 0
        for frame_key in h5file.keys():
            frame_group = h5file[frame_key]
            timestamp = frame_group['timestamp'][()]
            adc_values = frame_group['adc_values'][()]

            print(f"Frame {frame_count}:")
            print(f"Timestamp: {timestamp.decode('utf-8')}")
            print("ADC Values:")
            for i in range(0, len(adc_values), 16):
                print(adc_values[i:i + 16])

            frame_count += 1
            print("\n")


if __name__ == "__main__":
    read_hdf5_data('adc_data.h5')
