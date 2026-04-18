#!/usr/bin/env python3
"""
Generate navigation audio files using gTTS (Google Text-to-Speech)
"""

from gtts import gTTS
import os

# Create output directory if it doesn't exist
output_dir = '../src/assets/navigation_audio'
os.makedirs(output_dir, exist_ok=True)

# ==================== FLOOR SELECTION AUDIO ====================
floor_text = "Pilih lantai mana? 0 dasar, 1 lantai 1, 2 lantai 2, 3 lantai 3"
print(f"Generating: ask_floor.mp3")
print(f"Text: {floor_text}")
tts = gTTS(text=floor_text, lang='id', slow=False)
tts.save(f'{output_dir}/ask_floor.mp3')
print("✅ ask_floor.mp3 created\n")

# ==================== ROOM SELECTION AUDIO (FLOOR 0) ====================
room_floor_0_text = "Pilih ruangan lantai dasar. 0 pintu masuk, 1 meja piket guru, 2 lift utama, 3 kelas A, 4 kelas B"
print(f"Generating: ask_room_floor_0.mp3")
print(f"Text: {room_floor_0_text}")
tts = gTTS(text=room_floor_0_text, lang='id', slow=False)
tts.save(f'{output_dir}/ask_room_floor_0.mp3')
print("✅ ask_room_floor_0.mp3 created\n")

# ==================== ROOM SELECTION AUDIO (FLOOR 1) ====================
room_floor_1_text = "Pilih ruangan lantai 1.  1 kelas C, 2 kelas D, 3 kelas E, 4 lab kimia, 5 lab biologi, 6 lab fisika, 7 lab komputer, 8 toilet disabilitas"
print(f"Generating: ask_room_floor_1.mp3")
print(f"Text: {room_floor_1_text}")
tts = gTTS(text=room_floor_1_text, lang='id', slow=False)
tts.save(f'{output_dir}/ask_room_floor_1.mp3')
print("✅ ask_room_floor_1.mp3 created\n")

# ==================== ROOM SELECTION AUDIO (FLOOR 2) ====================
room_floor_2_text = "Pilih ruangan lantai 2. 1 kelas F, 2 kelas G, 3 kelas H, 4 kelas I, 5 kelas J, 6 kelas K, 7 kelas L, 8 toilet disabilitas, 9 ruang ekskul, 10 ruang OSIS"
print(f"Generating: ask_room_floor_2.mp3")
print(f"Text: {room_floor_2_text}")
tts = gTTS(text=room_floor_2_text, lang='id', slow=False)
tts.save(f'{output_dir}/ask_room_floor_2.mp3')
print("✅ ask_room_floor_2.mp3 created\n")

# ==================== ROOM SELECTION AUDIO (FLOOR 3) ====================
room_floor_3_text = "Pilih ruangan lantai 3. 1 kelas M, 2 kelas N, 3 kelas O, 4 kelas P, 5 kelas Q, 6 kelas R, 7 kelas S, 8 toilet disabilitas, 9 perpustakaan"
print(f"Generating: ask_room_floor_3.mp3")
print(f"Text: {room_floor_3_text}")
tts = gTTS(text=room_floor_3_text, lang='id', slow=False)
tts.save(f'{output_dir}/ask_room_floor_3.mp3')
print("✅ ask_room_floor_3.mp3 created\n")

print("=" * 50)
print("✅ All audio files generated successfully!")
print("=" * 50)
