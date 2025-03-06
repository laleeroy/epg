import xml.etree.ElementTree as ET
import os

def collect_channels(base_dir, target_dirs):
    all_channels = []

    target_dirs = [os.path.join(base_dir, d) for d in target_dirs]

    for dirpath, _, filenames in os.walk(base_dir):
        if any(dirpath.startswith(target_dir) for target_dir in target_dirs):
            for filename in filenames:
                if filename.endswith('.xml'):
                    input_file = os.path.join(dirpath, filename)
                    print(f'Processing {input_file}...')

                    tree = ET.parse(input_file)
                    root = tree.getroot()

                    all_channels.extend(root.findall('channel'))

    return all_channels

def save_channels(channels, output_file):
    root = ET.Element('channels')

    for channel in channels:
        root.append(channel)

    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

base_directory = 'sites'
output_file = 'updated_channels.xml'
target_dirs = ['clickthecity.com', 'mysky.com.ph', 'osn.com', 'nowplayer.now.com', 'ontvtonight.com', 'singtel.com', 'tvtv.us', 'starhubtvplus.com']

channels = collect_channels(base_directory, target_dirs)
save_channels(channels, output_file)
