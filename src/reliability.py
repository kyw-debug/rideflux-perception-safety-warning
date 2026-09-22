from typing import List, Tuple
from .perception import DetectedObject

class ReliabilityEvaluator:
    """Perception 데이터 신뢰도 평가 및 센서 노이즈 필터링 모듈"""
    def __init__(self, confidence_cutoff: float = 0.6):
        self.confidence_cutoff = confidence_cutoff

    def evaluate_reliability(self, objects: List[DetectedObject]) -> Tuple[List[DetectedObject], float]:
        valid_objects = []
        total_conf = 0.0

        for obj in objects:
            # 1. 신뢰도 임계값 검증
            if obj.confidence < self.confidence_cutoff:
                continue
            
            # 2. 비정상 데이터 필터링 (음수 거리 등 노이즈 제거)
            if obj.distance <= 0:
                continue

            valid_objects.append(obj)
            total_conf += obj.confidence

        reliability_score = (total_conf / len(objects)) if objects else 1.0
        return valid_objects, round(reliability_score, 4)
