import os
from PIL import Image
from tkinter import Tk, filedialog
import sys

def konversi_ke_webp_dengan_dialog():
    # Sembunyikan jendela root Tkinter yang tidak perlu
    root = Tk()
    root.withdraw()

    # Tampilkan dialog "Pilih File" dan biarkan pengguna memilih beberapa file
    print("Membuka dialog pemilihan file...")
    file_paths = filedialog.askopenfilenames(
        title="Pilih File JPG atau PNG untuk Dikonversi ke WebP (Anda bisa memilih banyak file)",
        filetypes=[("File Gambar", "*.jpg *.jpeg *.png")]
    )

    if not file_paths:
        print("\nTidak ada file yang dipilih. Konversi dibatalkan.")
        return

    # Tentukan folder output (disimpan di sub-folder 'konversi_webp_output' di Desktop)
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    output_dir = os.path.join(desktop_path, "konversi_webp_output")
    
    # Buat folder output jika belum ada
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nFile WebP akan disimpan di: {output_dir}")

    sukses_count = 0
    gagal_list = []

    for path in file_paths:
        try:
            # 1. Buka gambar
            img = Image.open(path)
            
            # 2. Buat nama file output
            filename = os.path.basename(path)
            name_without_ext = os.path.splitext(filename)[0]
            output_path = os.path.join(output_dir, f"{name_without_ext}.webp")

            # 3. Konversi dan simpan ke WebP
            img.save(output_path, "webp", quality=85) 
            
            print(f"✅ Berhasil konversi: '{filename}' -> '{os.path.basename(output_path)}'")
            sukses_count += 1

        except Exception as e:
            print(f"❌ Gagal konversi '{path}'. Error: {e}")
            gagal_list.append(path)

    print("\n" + "="*50)
    print(f"Konversi Selesai! Total File Berhasil: {sukses_count}")
    if gagal_list:
        print(f"Perhatian, ada {len(gagal_list)} file yang gagal dikonversi.")
        
    print(f"Silakan cek file Anda di folder: {output_dir}")
    print("="*50)
if __name__ == "__main__":
    konversi_ke_webp_dengan_dialog()