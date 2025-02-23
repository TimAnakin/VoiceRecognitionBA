 print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(language="de", input_device_index=1)

    # Erstelle die CSV-Datei mit korrektem Header
    with open("sst_results.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Gesprochener Satz", "Erwarteter Satz", "SequenceMatcher Genauigkeit", "Levenshtein-Distanz", "Wortgenauigkeit", "Positionsgenauigkeit", "Endgenauigkeit"])

    print("Als erstes zu sprechen:", all_sentences[current_index])

    while True:
        if keyboard.is_pressed("f"):
            recorder.text(process_text) 