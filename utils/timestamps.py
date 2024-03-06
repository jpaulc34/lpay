from datetime import datetime

def set_timestamps(data):
    data.created_at = datetime.utcnow()
    data.updated_at = data.created_at

def set_updated_at(data):
    if hasattr(data, 'created_at'):
        del data.created_at
    data.updated_at = datetime.utcnow()