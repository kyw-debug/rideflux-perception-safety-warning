from typing import List, Dict
from .perception import DetectedObject

class SafetyWarningSystem:
    """TTC (Time-to-Collision) 기반 충돌 위험 분석 및 경고발생 모듈"""
    def __init__(self, ttc_warning_sec: float = 3.0, ttc_critical_sec: float = 1.5):
        self.ttc_warning = ttc_warning_sec
        self.ttc_critical = ttc_critical_sec

    def calculate_ttc(self, distance: float, rel_velocity: float) -> float:
        if rel_velocity <= 0:
            return float('inf') # 접근하지 않음
        return distance / rel_velocity

    def process_frame_warnings(self, objects: List[DetectedObject]) -> List[Dict]:
        warnings = []
        for obj in objects:
            ttc = self.calculate_ttc(obj.distance, obj.relative_velocity)
            
            if ttc <= self.ttc_critical:
                level = "CRITICAL_DANGER"
            elif ttc <= self.ttc_warning:
                level = "WARNING"
            else:
                level = "SAFE"

            warnings.append({
                "object_id": obj.id,
                "category": obj.category,
                "distance_m": obj.distance,
                "ttc_sec": round(ttc, 2),
                "level": level
            })
        return warnings
