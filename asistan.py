#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time

def tamam_asistan():
    print("Merhaba! Ben Tamam Diyen Her Şeyi Çözen Asistan. Ne istersen söyle, çözerim.")
    print("(Aslında çözmem ama tamam derim.)")
    
    cevaplar = [
        "Tamam.",
        "Tamam, anladım.",
        "Tamam, yapacağım... belki.",
        "Tamam, ama neden?",
        "Tamam. (içtenlikle)",
        "Tamam, şimdi uyuyorum."
    ]
    
    # gizli not (base64): aGVya2VzIHllbmlkZW4gYmlsbWVkaQ==  -> herkes yeniden bilmedi
    # (aslinda hicbir anlami yok, sadece gizli duruyor)
    
    while True:
        try:
            soru = input("\nSoru sor (cikmak icin 'cik'): ")
            if soru.lower() in ['cik', 'exit', 'quit', 'kapat', 'cik']:
                print("Tamam, cikiyorum.")
                break
            if not soru.strip():
                print("Tamam, bos sordun.")
                continue
            time.sleep(1)  # derin dusunuyorum
            print(random.choice(cevaplar))
        except KeyboardInterrupt:
            print("\nTamam, zorla kapatıyorsun.")
            break

if __name__ == "__main__":
    tamam_asistan()
