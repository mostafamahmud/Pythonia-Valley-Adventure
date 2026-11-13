"""
📖 كتاب: مغامرة في وادي بايثونيا (الفصل 32: ميزان الصلاحيات)
✍️ تأليف: مصطفى محمود حسن

🎯 التحدي (الأمن السيبراني - إدارة الصلاحيات):
لحماية سجلات المملكة من المتسللين، نحتاج إلى نظام يتحقق من رتبة المستخدم وصلاحياته (RBAC)
قبل السماح له بتنفيذ أوامر حساسة مثل تعديل محرك بايثونيا.
"""

# --- الكود التطبيقي ---
roles_permissions = {
    "visitor": ["read_map"],
    "guardian": ["read_map", "scan_bugs"],
    "admin": ["read_map", "scan_bugs", "restart_engine"]
}

def check_access(user_role, action):
    allowed_actions = roles_permissions.get(user_role, [])
    if action in allowed_actions:
        return f"✅ مسموح: الرتبة ({user_role}) تملك صلاحية ({action})."
    return f"⛔ مرفوض: محاولة غير مصرح بها من ({user_role}) لتنفيذ ({action})!"

print(check_access("guardian", "scan_bugs"))
print(check_access("guardian", "restart_engine"))

# 🔗 احصل على النسخة الكاملة من الكتاب (40 فصلاً من القصص والتحديات):
# [ضع رابط كتابك على Google Play Books هنا]
