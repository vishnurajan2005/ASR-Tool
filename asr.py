import whisper
import os


def transcribe_audio(audio_file):
    print("\nLoading Whisper model...")
    
    # Use CPU for compatibility
    model = whisper.load_model("base", device="cpu")

    print("Transcribing audio...")
    
    result = model.transcribe(
        audio_file,
        fp16=False
    )

    return result["text"].strip()


def save_transcription(text, audio_file):
    output_file = os.path.splitext(audio_file)[0] + "_transcription.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    return output_file


def main():
    print("=" * 60)
    print("        AUTOMATIC SPEECH RECOGNITION TOOL")
    print("=" * 60)

    audio_file = input("\nEnter the path of your audio file: ").strip()

    if not os.path.exists(audio_file):
        print("\nError: Audio file not found.")
        return

    try:
        text = transcribe_audio(audio_file)

        print("\n" + "=" * 60)
        print("TRANSCRIPTION")
        print("=" * 60)
        print(text)
        print("=" * 60)

        output_file = save_transcription(text, audio_file)

        print("\nTranscription saved to:")
        print(output_file)

    except Exception as e:
        print(f"\nError during transcription: {e}")


if __name__ == "__main__":
    main()