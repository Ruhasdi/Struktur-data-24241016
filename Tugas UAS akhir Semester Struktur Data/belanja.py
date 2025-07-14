def main():
    # Meminta input nama customer dan tanggal belanja
    nama_customer = input("Masukkan nama customer: ")
    tanggal_belanja = input("Masukkan tanggal belanja (DD-MM-YYYY): ")
    
    # Menyimpan nama customer dan tanggal belanja dalam tuple
    customer_info = (nama_customer, tanggal_belanja)
    
    # Meminta input jumlah barang
    jumlah_barang = int(input("Masukkan jumlah barang yang akan dibeli: "))
    
    # List untuk menyimpan data barang
    daftar_barang = []
    
    for i in range(jumlah_barang):
        print(f"\nData Barang ke-{i + 1}:")
        # Meminta input untuk setiap barang
        nama_barang = input("Masukkan nama barang: ")
        harga_satuan = float(input("Masukkan harga satuan barang: "))
        jumlah_qiy = int(input("Masukkan jumlah barang: "))
        
        # Menyimpan data barang dalam dictionary
        barang = {
            'nama_barang': nama_barang,
            'harga_satuan': harga_satuan,
            'jumlah_qiy': jumlah_qiy,
            'total_harga': harga_satuan * jumlah_qiy
        }
        
        # Menambahkan dictionary barang ke dalam list
        daftar_barang.append(barang)
    
    # Menampilkan data customer
    print("\nData Customer:")
    print(f"Nama Customer: {customer_info[0]}")
    print(f"Tanggal Belanja: {customer_info[1]}")
    
    # Menampilkan daftar belanja
    print("\nDaftar Belanja:")
    total_bayar = 0
    for barang in daftar_barang:
        print(f"Jumlah: {barang['jumlah_qiy']}, Nama Barang: {barang['nama_barang']}, Harga Satuan: {barang['harga_satuan']}, Total Harga: {barang['total_harga']}")
        total_bayar += barang['total_harga']
    
    # Menampilkan total bayar
    print(f"\nTotal Bayar: {total_bayar}")

if __name__ == "__main__":
    main()
