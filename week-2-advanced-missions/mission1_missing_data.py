"""
📖 كتاب: مغامرة في وادي بايثونيا (الفصل 26: فانوس القيم الناقصة)
✍️ تأليف: مصطفى محمود حسن

🎯 التحدي (تحليل البيانات):
أثناء مسح سجلات الطاقة في وادي بايثونيا، تسبب ظل النقص المفاجئ في فقدان بعض القراءات (None).
مهمتك هي تنظيف البيانات وتعويض القيم الناقصة بالمتوسط الحسابي للقراءات السليمة.
"""

# --- الكود التطبيقي ---
energy_readings = [80, None, 90, 70, None, 100]

# 1. استخراج القيم السليمة فقط لحساب المتوسط
valid_readings = [x for x in energy_readings if x is not None]
average_energy = sum(valid_readings) / len(valid_readings)

# 2. تعويض القيم الناقصة بالمتوسط
cleaned_data = [x if x is not None else average_energy for x in energy_readings]

print("البيانات الأصلية:", energy_readings)
print("المتوسط المحسوب:", average_energy)
print("البيانات النظيفة:", cleaned_data)

# 🔗 احصل على النسخة الكاملة من الكتاب (40 فصلاً من القصص والتحديات):
# [ضع رابط كتابك على Google Play Books هنا]
