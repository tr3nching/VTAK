import re

# Function to modify tvg-id when tvg-id is "", "(no tvg-id)", contains "astro", contains "dummy", or missing
def modify_tvgid_with_channel_name(line):
    match = re.match(r'(#EXTINF:.*?tvg-id=")(.*?)(".*?)(",.*?)([^,]+)$', line)
    
    if match:
        tvg_id_value = match.group(2).strip()  # The current tvg-id value
        tvg_name = match.group(5).strip()      # The channel name after the last comma
        
        # Check if tvg-id is "", "(no tvg-id)", contains "netflix", "samsung", "usb", "astro", or "dummy"
        if tvg_id_value == "" or tvg_id_value == "(no tvg-id)" or "netflix" in tvg_id_value.lower() or "samsung" in tvg_id_value.lower() or "usb" in tvg_id_value.lower() or "astro" in tvg_id_value.lower() or "dummy" in tvg_id_value.lower() or "dimmy" in tvg_id_value.lower():
            # Modify the tvg-id value to be the tvg_name and add a space after the comma before the tvg_name
            modified_line = match.group(1) + tvg_name + ".ph" + match.group(3) + match.group(4) + tvg_name
            return modified_line + "\n"
        else:
            return match.group(1) + match.group(2) + match.group(3) + match.group(4) + tvg_name + "\n"
    else:
        return line

# Function to replace group-title based on specific mappings
def replace_group_title(line):
    group_title_mappings = {
        "Local": "Entertainment",
        "Animals, Nature & History": "Documentary",
        "CARTOONS AND ANIMATIONS": "Kids",
        "KIDS EXCLUSIVES": "Kids",
        "KIDS NETWORKS": "Kids",
        "Movie Central": "Movies",
        "HBOGO Asia": "VOD",
        "🎬 VIVAONE MOVIES MIX": "VOD",
        " 🎬 TFC MOVIES ": "VOD Tagalog",
        "🎬 VIVAONE MOVIES TAGALOG": "VOD Tagalog",
        "📀 MAALA-ALA MO KAYA": "VOD Tagalog",
        "PREMIUM SPORTS": "Sports",
        "🇵🇭 PILIPINAS LIVE": "Sports",
        "PREMIUM MUSIC": "Music Videos",
        "RELAXIATION AREA": "Scenes",
        "PH RADIO CHANNELS": "Music Videos",
        "RESERVED CHANNELS": "Music Videos",
    }
    
    # Match the group-title and replace with mapped value
    for old_title, new_title in group_title_mappings.items():
        pattern = r'group-title="{}"'.format(re.escape(old_title))
        if re.search(pattern, line):
            line = re.sub(pattern, 'group-title="{}"'.format(new_title), line)
    
    return line

# Function to disable #EXTINF:-1 group-logo=... lines
def disable_group_logo(line):
    # Match lines that contain group-logo and comment them out
    if re.search(r'#EXTINF:.*?group-logo=', line):
        # Prefix the line with '#' to disable it
        return f"` {line}"
    else:
        return line

# Function to find and append additional XML URLs to url-tvg="... lines
def append_xml_urls_to_tvg(line):
    # Match lines that contain url-tvg ending with .xml
    if re.match(r'#EXTM3U.*?url-tvg=".*\.xml"', line):
        # Append additional URLs to the existing url-tvg attribute
        new_urls = 'https://www.open-epg.com/files/philippines2.xml, https://www.open-epg.com/files/philippines3.xml, https://www.open-epg.com/files/philippines1.xml'
        line = re.sub(r'(url-tvg=".*\.xml")', r'\1, ' + new_urls + '"', line)
    return line

# Read the input file (JAPONESE)
with open('Tivikoh.m3u', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# Apply modifications to all lines
modified_lines = []
for line in lines:
    line = modify_tvgid_with_channel_name(line)  # Modify tvg-id
    line = replace_group_title(line)  # Modify group-title
    line = disable_group_logo(line)  # Disable group-logo lines
    line = append_xml_urls_to_tvg(line)  # Append XML URLs to url-tvg
    modified_lines.append(line)

# Write the modified content to the output file (trenching.m3u)
with open('Tivikoh2.m3u', 'w', encoding='utf-8') as outfile:
    outfile.writelines(modified_lines)

print("File processing complete. The modified content is saved in 'Tivikoh2.m3u'.")
