import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Reservation:
    def __init__(self, name, date, time, num_players, table_type, ruangan, stick, price):
        self.name = name
        self.date = date
        self.time = time
        self.num_players = num_players
        self.table_type = table_type
        self.ruangan = ruangan
        self.stick = stick
        self.price = price
        
    def display(self):
        return (f"Detail Reservasi:\n"
                f"Nama: {self.name}\n"
                f"Tanggal: {self.date}\n"
                f"Waktu: {self.time}\n"
                f"Jumlah Pemain: {self.num_players}\n"
                f"Jenis Meja: {self.table_type}\n"
                f"Ruangan Biliar: {self.ruangan}\n"
                f"Tongkat Biliar: {self.stick}\n"
                f"Harga: Rp{self.price:.2f}\n")

class ReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Reservasi Biliar")
        self.reservations = []

        # Harga default
        self.regular_table_price = 50000
        self.vip_table_price = 75000
        self.reguler_ruangan_price = 35000
        self.premium_ruangan_price = 45000
        self.reguler_stick_price = 15000
        self.premium_stick_price = 25000

        self.create_main_menu()

    def create_main_menu(self):
        ttk.Label(self.root, text="Sistem Reservasi Biliar", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

        self.make_reservation_button = ttk.Button(self.root, text="Buat Reservasi", command=self.open_make_reservation)
        self.make_reservation_button.grid(row=1, column=0, columnspan=2, pady=10, padx=20, ipadx=10)

        self.view_reservations_button = ttk.Button(self.root, text="Lihat Reservasi", command=self.open_view_reservations)
        self.view_reservations_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20, ipadx=10)
    
    def open_make_reservation(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Buat Reservasi")
        self.create_reservation_widgets(self.new_window)
    
    def open_view_reservations(self):
        self.display_reservations(self.root)
    
    def create_reservation_widgets(self, window):
        # Tampilkan daftar harga
        self.display_prices(window)

        # Buat label dan entri untuk detail reservasi
        ttk.Label(window, text="Nama:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = ttk.Entry(window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.name_entry.bind("<Return>", lambda event: self.date_entry.focus())

        ttk.Label(window, text="Tanggal (YYYY-MM-DD):").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.date_entry = ttk.Entry(window)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)
        self.date_entry.bind("<Return>", lambda event: self.time_entry.focus())
        
        ttk.Label(window, text="Waktu (HH:MM):").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.time_entry = ttk.Entry(window)
        self.time_entry.grid(row=3, column=1, padx=10, pady=5)
        self.time_entry.bind("<Return>", lambda event: self.num_players_entry.focus())
        
        ttk.Label(window, text="Jumlah Pemain:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.num_players_entry = ttk.Entry(window)
        self.num_players_entry.grid(row=4, column=1, padx=10, pady=5)
        self.num_players_entry.bind("<Return>", lambda event: self.table_type.set("Regular"))

        # Buat opsi untuk jenis meja, ruangan biliar, dan tongkat biliar
        ttk.Label(window, text="Jenis Meja:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        self.table_type = tk.StringVar()
        self.table_type.set("Regular")
        ttk.Radiobutton(window, text="Regular", variable=self.table_type, value="Regular").grid(row=5, column=1, sticky=tk.W, padx=10)
        ttk.Radiobutton(window, text="VIP", variable=self.table_type, value="VIP").grid(row=5, column=2, sticky=tk.W, padx=10)
        
        ttk.Label(window, text="Ruangan Biliar:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
        self.ruangan = tk.StringVar()
        self.ruangan.set("Ruangan Biliar Reguler")
        ttk.Radiobutton(window, text="Ruangan Biliar Reguler", variable=self.ruangan, value="Ruangan Biliar Reguler").grid(row=6, column=1, sticky=tk.W, padx=10)
        ttk.Radiobutton(window, text="Ruangan Biliar Premium", variable=self.ruangan, value="Ruangan Biliar Premium").grid(row=6, column=2, sticky=tk.W, padx=10)
        
        ttk.Label(window, text="Tongkat Biliar:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
        self.stick = tk.StringVar()
        self.stick.set("Tongkat Biliar Reguler")
        ttk.Radiobutton(window, text="Tongkat Biliar Reguler", variable=self.stick, value="Tongkat Biliar Reguler").grid(row=7, column=1, sticky=tk.W, padx=10)
        ttk.Radiobutton(window, text="Tongkat Biliar Premium", variable=self.stick, value="Tongkat Biliar Premium").grid(row=7, column=2, sticky=tk.W, padx=10)

        # Buat opsi untuk pembayaran
        ttk.Label(window, text="Metode Pembayaran:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
        self.payment_method = tk.StringVar()
        self.payment_method.set("Tunai")
        ttk.Radiobutton(window, text="Tunai", variable=self.payment_method, value="Tunai").grid(row=8, column=1, sticky=tk.W, padx=10)
        ttk.Radiobutton(window, text="Transfer", variable=self.payment_method, value="Transfer").grid(row=8, column=2
        , sticky=tk.W, padx=10)
        ttk.Radiobutton(window, text="Scan QR", variable=self.payment_method, value="Scan QR").grid(row=8, column=3, sticky=tk.W, padx=10)

        # Buat tombol untuk membuat reservasi
        self.make_reservation_button = ttk.Button(window, text="Buat Reservasi", command=self.make_reservation)
        self.make_reservation_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.reservation_output = tk.Text(window, width=80, height=10)
        self.reservation_output.grid(row=10, column=0, columnspan=4, padx=10, pady=10)
        self.reservation_output.config(state=tk.DISABLED)

    def display_prices(self, window):
        prices = self.get_prices()
        price_list = (f"Daftar Harga:\n"
                      f"Meja Regular: Rp{prices['Meja Regular']:.2f}\n"
                      f"Meja VIP    : Rp{prices['Meja VIP']:.2f}\n"
                      f"Ruangan Biliar Reguler   : Rp{prices['Ruangan Biliar Reguler']:.2f}\n"
                      f"Ruangan Biliar Premium   : Rp{prices['Ruangan Biliar Premium']:.2f}\n"
                      f"Tongkat Biliar Reguler: Rp{prices['Tongkat Biliar Reguler']:.2f}\n"
                      f"Tongkat Biliar Premium: Rp{prices['Tongkat Biliar Premium']:.2f}\n")

        self.price_label = ttk.Label(window, text=price_list, justify=tk.LEFT)
        self.price_label.grid(row=0, column=0, columnspan=4, sticky=tk.W, padx=10, pady=5)

    def calculate_price(self, table_type, ruangan, stick):
        price = 0.0
        if table_type == "Regular":
            price += self.regular_table_price
        elif table_type == "VIP":
            price += self.vip_table_price
        
        if ruangan == "Ruangan Biliar Premium":
            price += self.premium_ruangan_price
        else:
            price += self.reguler_ruangan_price
        
        if stick == "Tongkat Biliar Premium":
            price += self.premium_stick_price
        else:
            price += self.reguler_stick_price

        return price

    def make_reservation(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        num_players = self.num_players_entry.get()
        table_type = self.table_type.get()
        ruangan = self.ruangan.get()
        stick = self.stick.get()
        payment_method = self.payment_method.get()

        if not name or not date or not time or not num_players:
            messagebox.showerror("Error", "Harap isi semua kolom.")
            return
        
        try:
            num_players = int(num_players)
        except ValueError:
            messagebox.showerror("Error", "Jumlah pemain harus berupa angka.")
            return

        price = self.calculate_price(table_type, ruangan, stick)
        reservation = Reservation(name, date, time, num_players, table_type, ruangan, stick, price)
        self.reservations.append(reservation)
        
        self.reservation_output.config(state=tk.NORMAL)
        self.reservation_output.insert(tk.END, reservation.display() + "\n")
        self.reservation_output.config(state=tk.DISABLED)
        messagebox.showinfo("Sukses", f"Reservasi berhasil dibuat! Total harga: Rp{price:.2f}")

    def display_reservations(self, window):
        if not self.reservations:
            messagebox.showinfo("Reservasi", "Belum ada reservasi yang dibuat.")
            return

        reservations_details = ""
        for index, reservation in enumerate(self.reservations, 1):
            reservations_details += f"Reservasi {index}:\n{reservation.display()}\n"

        self.reservation_output = tk.Text(window, width=80, height=20)
        self.reservation_output.insert(tk.END, reservations_details)
        self.reservation_output.config(state=tk.DISABLED)
        self.reservation_output.grid(row=11, column=0, columnspan=4, padx=10, pady=10)

    def set_prices(self, regular_table_price, vip_table_price, reguler_ruangan_price, premium_ruangan_price, reguler_stick_price, premium_stick_price):
        self.regular_table_price = regular_table_price
        self.vip_table_price = vip_table_price
        self.reguler_ruangan_price = reguler_ruangan_price
        self.premium_ruangan_price = premium_ruangan_price
        self.reguler_stick_price = reguler_stick_price
        self.premium_stick_price = premium_stick_price

    def get_prices(self):
        return {
            "Meja Regular": self.regular_table_price,
            "Meja VIP": self.vip_table_price,
            "Ruangan Biliar Reguler": self.reguler_ruangan_price,
            "Ruangan Biliar Premium": self.premium_ruangan_price,
            "Tongkat Biliar Reguler": self.reguler_stick_price,
            "Tongkat Biliar Premium": self.premium_stick_price
        }

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationSystem(root)
    root.mainloop()
