class EditorialBoard:
    def __init__(self):
        self.members = []

    def add_member(self, name, role):
        """Menambahkan anggota baru ke dewan editorial."""
        self.members.append({'name': name, 'role': role})
        print(f"Anggota '{name}' dengan peran '{role}' berhasil ditambahkan.")

    def list_members(self):
        """Menampilkan daftar anggota dewan editorial."""
        if not self.members:
            print("Belum ada anggota di dewan editorial.")
        else:
            print("Daftar Anggota Dewan Editorial:")
            for i, member in enumerate(self.members, start=1):
                print(f"{i}. Nama: {member['name']}, Peran: {member['role']}")

    def remove_member(self, name):
        """Menghapus anggota dari dewan editorial berdasarkan nama."""
        self.members = [member for member in self.members if member['name'] != name]
        print(f"Anggota '{name}' berhasil dihapus.")


def main():
    board = EditorialBoard()

    while True:
        print("\n=== Sistem Manajemen Dewan Editorial Jurnal ===")
        print("1. Tambah Anggota")
        print("2. Lihat Daftar Anggota")
        print("3. Hapus Anggota")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            name = input("Masukkan nama anggota: ")
            role = input("Masukkan peran anggota (Editor/Reviewer): ")
            board.add_member(name, role)
        elif choice == '2':
            board.list_members()
        elif choice == '3':
            name = input("Masukkan nama anggota yang ingin dihapus: ")
            board.remove_member(name)
        elif choice == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main ()
