from dataclasses import dataclass
from typing import List

@dataclass
class DetectedObject:
    id: int
    category: str       # Vehicle, Pedestrian, Bike
    distance: float     # meters
    relative_velocity: float # m/s (양수: 접근 중)
    confidence: float   # 0.0 ~ 1.0
    sensor_type: str    # Camera, LiDAR, Radar

class PerceptionModule:
    """카메라·LiDAR·Radar 센서 인식 데이터를 처리하는 모듈"""
    def __init__(self, min_confidence_threshold: float = 0.5):
        self.min_confidence = min_confidence_threshold

    def parse_sensor_frame(self, raw_data: List[dict]) -> List[DetectedObject]:
        objects = []
        for obj in raw_data:
            detected = DetectedObject(
                id=obj['id'],
                category=obj['category'],
                distance=obj['distance'],
                relative_velocity=obj['relative_velocity'],
                confidence=obj['confidence'],
                sensor_type=obj['sensor_type']
            )
            objects.append(detected)
        return objects
