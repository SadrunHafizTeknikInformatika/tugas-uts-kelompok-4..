from abc import ABC, abstractmethod
from typing import List

class PapaSignatureMixin:
    def __init__(self, signature_level: int = 100):
        self.signature_level = signature_level

    def get_papa_info(self) -> str:
        return f"PAPA SIGNATURE ACTIVATED! Level: {self.signature_level}% 🍰"

class Product(ABC):
    def __init__(self, name: str, price: float, stock: int, category: str):
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__category = category
        self.__cost_price = price * 0.6

    @property
    def name(self): return self.__name
    @property
    def price(self): return self.__price
    @property
    def stock(self): return self.__stock

    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Stok tidak boleh negatif!")
        self.__stock = value

    @property
    def category(self): return self.__category

    def sell(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Kuantitas harus positif!")
        if quantity > self.__stock:
            raise ValueError("Stok tidak cukup!")
        self.stock -= quantity
        return self.price * quantity

    @abstractmethod
    def get_product_type(self) -> str: pass

    def _get_cost_price(self):
        return self.__cost_price

class CakeProduct(Product):
    def __init__(self, name: str, price: float, stock: int, flavor: str):
        super().__init__(name, price, stock, "Kue")
        self.flavor = flavor
    def get_product_type(self) -> str:
        return "Cake Product"

class BreadProduct(Product):
    def __init__(self, name: str, price: float, stock: int, bread_type: str):
        super().__init__(name, price, stock, "Roti")
        self.bread_type = bread_type
    def get_product_type(self) -> str:
        return "Bread Product"

class PastryProduct(Product):
    def __init__(self, name: str, price: float, stock: int, pastry_type: str):
        super().__init__(name, price, stock, "Pastry")
        self.pastry_type = pastry_type
    def get_product_type(self) -> str:
        return "Pastry Product"

class PapaSignatureProduct(CakeProduct, PapaSignatureMixin):
    def __init__(self, name: str, price: float, stock: int, flavor: str, signature_level: int = 150):
        CakeProduct.__init__(self, name, price, stock, flavor)
        PapaSignatureMixin.__init__(self, signature_level)
    def get_product_type(self) -> str:
        return "Papa Signature Product (Limited)"

class PapaBakery:
    def __init__(self):
        self.__products: List[Product] = []
        self.__transactions: List[dict] = []

    def add_product(self, product: Product):
        self.__products.append(product)

    def sell_item(self, product_name: str, quantity: int) -> float:
        for p in self.__products:
            if p.name == product_name:
                total = p.sell(quantity)
                self.__transactions.append({"product": product_name, "qty": quantity, "total": total})
                return total
        raise ValueError("Barang tidak ditemukan!")

    def generate_stock_report(self) -> str:
        report = "=== Laporan Stok Papa Bakery ===\n"
        for p in self.__products:
            report += f"{p.name} ({p.get_product_type()}): {p.stock} pcs\n"
        return report

    def generate_sales_report(self) -> str:
        report = "=== Laporan Transaksi Papa Bakery ===\n"
        for t in self.__transactions:
            report += f"{t['product']} x{t['qty']} = Rp {t['total']:,}\n"
        return report

# ================== DEMO (INI YANG BARU) ==================
if __name__ == "__main__":
    print("🚀 Papa Bakery System Started!\n")
    
    bakery = PapaBakery()
    
    # Tambah produk
    redvelvet = PapaSignatureProduct("Red Velvet Cake", 185000, 20, "Red Velvet")
    croffle = PastryProduct("Croffle Original", 35000, 50, "Croffle")
    bakery.add_product(redvelvet)
    bakery.add_product(croffle)
    
    print("✅ Produk berhasil ditambahkan:")
    print(bakery.generate_stock_report())
    
    # Transaksi
    print("\n💰 Melakukan transaksi...")
    total = bakery.sell_item("Red Velvet Cake", 3)
    print(f"Terjual Red Velvet Cake x3 → Total: Rp {total:,}")
    
    print("\n📊 Laporan Stok Terbaru:")
    print(bakery.generate_stock_report())
    
    print("\n📋 Laporan Transaksi:")
    print(bakery.generate_sales_report())
    
    print("\n✅ Sistem Papa Bakery berjalan dengan baik!")
