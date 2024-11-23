
# Kutubxona boshqaruv tizimi

Bu loyiha Django REST Framework (DRF) yordamida yaratilgan bo‘lib, kutubxona kitoblarini boshqarish, foydalanuvchilarni ro‘yxatdan o‘tkazish va kitoblarni vaqtinchalik berish jarayonlarini boshqarish uchun mo‘ljallangan.

---

## Loyiha maqsadi

Loyiha quyidagi asosiy funksiyalarni amalga oshirishni maqsad qiladi:

1. **Kitoblarni boshqarish:**
   - Kitoblarni qo‘shish, o‘chirish va tahrirlash.
   - Kitoblar ro‘yxatini ko‘rish.
2. **Foydalanuvchilarni boshqarish:**
   - Foydalanuvchilarni ro‘yxatdan o‘tkazish va ularning ma’lumotlarini boshqarish.
3. **Kitoblarni vaqtinchalik berish va qaytarish:**
   - Foydalanuvchilarga kitoblarni vaqtinchalik olish imkonini berish.
   - Kitoblarni qaytarib olish jarayonini boshqarish.

---

## Asosiy tamoyillar

Loyihada **SOLID** tamoyillari asosida quyidagicha yondashuv ishlatilgan:

### 1. Single Responsibility Principle (SRP):
- Har bir model (User, Book, BorrowRecord) faqat bitta vazifani bajaradi.
- Har bir model uchun alohida serializer va view yaratilgan.

### 2. Open/Closed Principle (OCP):
- Yangi kitob turlari (Fiction, NonFiction) qo‘shilganda mavjud kodni o‘zgartirish shart emas.

### 3. Liskov Substitution Principle (LSP):
- Kitob modeli va uning voris modellarini almashtirib ishlatish mumkin.
- Admin va oddiy foydalanuvchilar bir xil funksiyalarni bajaradi.

### 4. Interface Segregation Principle (ISP):
- Kitoblar, foydalanuvchilar va jarayonlar uchun alohida endpoint’lar yozilgan.

### 5. Dependency Inversion Principle (DIP):
- Ma’lumotlarni saqlash uchun abstraksiyalardan foydalanilgan (masalan, StorageService).

---

## API Endpointlari

Quyida loyihaning API marshrutlari va ularning vazifalari keltirilgan:

| Endpoint           | Metod      | Tavsif                           |
|---------------------|------------|----------------------------------|
| `/api/books/`       | GET        | Kitoblar ro‘yxatini ko‘rish.    |
| `/api/books/`       | POST       | Yangi kitob qo‘shish.           |
| `/api/books/{id}/`  | PUT        | Kitobni tahrirlash.             |
| `/api/books/{id}/`  | DELETE     | Kitobni o‘chirish.              |
| `/api/users/`       | GET        | Foydalanuvchilar ro‘yxatini ko‘rish. |
| `/api/borrow/`      | POST       | Kitobni vaqtinchalik olish.     |
| `/api/borrow/{id}/` | PUT        | Kitobni qaytarish.              |

---

## O‘rnatish bo‘yicha qo‘llanma

Quyidagi qadamlar orqali loyihani o‘rnatib foydalanishni boshlang:

### 1. Loyihani klonlash:
```bash
git clone https://github.com/mirmakhmudoff/astrum-library-project.git
cd astrum-library-project
```

### 2. Virtual muhitni yaratish va faollashtirish:
```bash
python -m venv venv
source venv/bin/activate  # Windows uchun: venv\Scriptsctivate
```

### 3. Talablarni o‘rnatish:
```bash
pip install -r requirements.txt
```

### 4. Ma’lumotlar bazasini sozlash:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Admin foydalanuvchini yaratish:
```bash
python manage.py createsuperuser
```

### 6. Serverni ishga tushirish:
```bash
python manage.py runserver
```

### 7. Admin panelga kirish:
Admin panelga kirish uchun brauzerda quyidagi manzilni oching:
```
http://127.0.0.1:8000/admin/
```

---

## Hujjatlar

Loyihaga tegishli API hujjatlari Swagger yoki Postman orqali tekshirilishi mumkin. DRF bilan integratsiya qilingan Swagger UI orqali hujjatlarga kirish mumkin:
```
http://127.0.0.1:8000/swagger/
```
