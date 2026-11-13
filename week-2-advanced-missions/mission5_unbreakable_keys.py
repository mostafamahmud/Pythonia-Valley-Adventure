"""
📖 كتاب: مغامرة في وادي بايثونيا (الفصل 38: مفاتيح لا تُخمَّن)
✍️ تأليف: مصطفى محمود حسن

🎯 التحدي (الأمن السيبراني - الحماية من التخمين):
استخدام الأرقام العشوائية العادية لا يكفي لحماية بوابات المملكة.
نستخدم مكتبة secrets المخصصة للأمن السيبراني لتوليد مفتاح تشفير عشوائي آمن لا يمكن تخمينه.
"""

import secrets
import string

# --- الكود التطبيقي ---
def generate_secure_key(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    secure_key = "".join(secrets.choice(alphabet) for _ in range(length))
    return secure_key

print("مفتاح البوابة الآمن الأول:", generate_secure_key())
print("مفتاح البوابة الآمن الثاني:", generate_secure_key(20))

# 🔗 احصل على النسخة الكاملة من الكتاب (40 فصلاً من القصص والتحديات):
# [ضع رابط كتابك على Google Play Books هنا]
