def create_m3u_file(base_url, num_channels, output_file, start_number, overwrite, group_name="Channels", prefix="Channel"):
    """
    Create or append M3U file with channels.

    :param base_url: The base URL where the streams are located.
    :param num_channels: The number of channels to generate.
    :param output_file: The name of the output M3U file.
    :param start_number: The starting number for the channel URLs.
    :param overwrite: Flag to determine if the file should be overwritten (True) or appended (False).
    :param group_name: The name of the group for the `group-title`.
    :param prefix: The prefix used for `tvg-id` and `tvg-name`.
    """
    
    # Open the file in write mode if overwrite is True, else append
    mode = 'w' if overwrite else 'a'
    
    with open(output_file, mode) as f:
        if overwrite:
            f.write("#EXTM3U\n")  # Write the M3U header only when overwriting
        
        

        # Iterate over the number of channels and create each entry
        for i in range(0, num_channels):
            # Format the num_channels to two digits
            i_formatted = str(i).zfill(2)

            # Format the channel number to two digits
            channel_number = str(start_number + i).zfill(2)

            # Generate the URL by incrementing the last part of the base URL
            url = f"{base_url}{start_number + i}"

            # Write the M3U entry with dynamic `tvg-id`, `tvg-name`, and `group-title`
            f.write(f'#EXTINF:-1 tvg-id="{prefix} {i_formatted}" tvg-name="{prefix} {i_formatted} {start_number + i}" tvg-logo="" group-title="{group_name}", {prefix} {i_formatted} {start_number + i}\n')
            f.write(f"{url}\n")
    
    action = "Overwritten" if overwrite else "Appended"
    print(f"Channels from {base_url} {action} to '{output_file}' successfully.")

# Example usage:

# Set the output file name
output_file = "sky.m3u"

# Whether to overwrite or append (set True to overwrite)
overwrite = True  # Change to True if you want to overwrite the file

# Clear the output file at the start if overwriting (so it starts fresh)
if overwrite:
    open(output_file, 'w').close()

# Create and append both playlists to the same file
create_m3u_file("http://blazetv.host:8080/DarrelReynolds70/Reynolds05/", 2, output_file, 791544, True, group_name="Disney+ Premier", prefix="Disney+ Premier")
create_m3u_file("http://blazetv.host:8080/DarrelReynolds70/Reynolds05/", 11, output_file, 791546, False, group_name="Disney Series+", prefix="Disney+ Series")
create_m3u_file("http://blazetv.host:8080/DarrelReynolds70/Reynolds05/", 18, output_file, 791557, False, group_name="HBO Max", prefix="HBO Max")
create_m3u_file("http://blazetv.host:8080/DarrelReynolds70/Reynolds05/", 14, output_file, 791575, False, group_name="Netflix Premier", prefix="Netflix Premier")
create_m3u_file("http://blazetv.host:8080/DarrelReynolds70/Reynolds05/", 11, output_file, 791589, False, group_name="Netflix Series", prefix="Netflix Series")
create_m3u_file("http://blazetv.host:8080/DarrelReynolds70/Reynolds05/", 11, output_file, 791600, False, group_name="Paramount", prefix="Paramount")
create_m3u_file("http://blazetv.host:8080/DarrelReynolds70/Reynolds05/", 13, output_file, 791611, False, group_name="Peacock", prefix="Peacock")
create_m3u_file("http://blazetv.host:8080/ivyhill85@gmail.com/EypmM6kXfEnB/", 11, output_file, 791624, False, group_name="Prime Series", prefix="Prime Series")
create_m3u_file("http://blazetv.host:8080/ivyhill85@gmail.com/EypmM6kXfEnB/", 31, output_file, 791635, False, group_name="Sky Premier", prefix="Sky Premier")


