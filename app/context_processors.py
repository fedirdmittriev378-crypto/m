"""
Context processors для глобальных переменных в шаблонах
"""
from .models import Notification

def inject_unread_notifications():
    """Добавляет количество непрочитанных уведомлений во все шаблоны"""
    try:
        unread_count = Notification.query.filter_by(is_read=False).count()
        return {'unread_count': unread_count}
    except:
        return {'unread_count': 0}

