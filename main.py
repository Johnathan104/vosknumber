from flask import Flask, request, jsonify, render_template
import logging
import json
import wave
from vosk import Model, KaldiRecognizer

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load Vosk model
try:
    logger.info("Loading Vosk model...")
    model = Model("model")  # folder name of extracted model
    logger.info("✓ Vosk model loaded")
except Exception as e:
    logger.error(f"✗ Failed to load model: {e}")
    model = None


@app.route('/')
def index():
    return render_template('index_whisper.html')


@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        if not model:
            return jsonify({'success': False, 'error': 'Model not loaded'}), 500

        if 'audio' not in request.files:
            return jsonify({'success': False, 'error': 'No audio file'}), 400

        audio_file = request.files['audio']
        audio_file.save("temp.wav")

        wf = wave.open("temp.wav", "rb")

        if wf.getnchannels() != 1 or wf.getframerate() != 16000:
            return jsonify({
                'success': False,
                'error': 'Audio must be mono PCM 16kHz WAV'
            }), 400

        rec = KaldiRecognizer(model,16000,'''["satu","dua","tiga","em pat",
        "empa","empat","lima","e nam","enam","tu juh","to jew",
        "de lapan","delapan","lapan",
        "sem bilan","sembilan","bilan",
        "say puluh","sepuluh", "puluh", "say poo luh"
    ]'''
)
        
        text = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                text += res.get("text", "")

        final_res = json.loads(rec.FinalResult())
        text += final_res.get("text", "")

        text = text.lower().strip().replace('.', '')
        logger.info(f"Transcribed: {text}")

        # SAME NUMBER LOGIC
        numbers = {
            'satu': 1, '1': 1, 'dua': 2, '2': 2, 'tiga': 3, '3': 3,
            'empat': 4, '4': 4, 'lima': 5, '5': 5, 'enam': 6, '6': 6,
            'tujuh': 7, '7': 7, 'delapan': 8, '8': 8, 'sembilan': 9, '9': 9,
            'sepuluh': 10, '10': 10,
            'satu saja': 1, 'dua saja': 2, 'tiga saja': 3,
            'empat saja': 4, 'lima saja': 5
        }

        if text in numbers:
            return jsonify({'success': True, 'number': numbers[text], 'text': text})

        for word in text.split():
            if word in numbers:
                return jsonify({'success': True, 'number': numbers[word], 'text': word})

        return jsonify({
            'success': False,
            'text': text,
            'error': 'Not recognized'
        })

    except Exception as e:
        logger.error(str(e))
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)