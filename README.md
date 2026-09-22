# rideflux-perception-safety-warning
# RideFlux 자율주행 AI Model Engineer 포트폴리오

> **RideFlux 2026 하반기 엔지니어 모집 공고 기반**
> 카메라·LiDAR·Radar 센서 데이터 수집부터 신뢰성 검증, TTC 기반 충돌 경고 및 정량 평가 파이프라인 구현 프로젝트입니다.

---

## 1. 채용 공고 요약 및 요구사항 매핑

* **채용 공고**: [RideFlux 2026 하반기 엔지니어 모집](https://inthiswork.com/archives/393239)
* **목표**: 자율주행 인식(Perception) 모듈부터 데이터 신뢰성(Reliability) 평가 및 안전 경고(Safety Warning) 시스템까지의 엔드투엔드 파이프라인 구축

| 공고 요구사항 (Job Requirements) | 구현 항목 및 증거 (GitHub Evidence) | 대응 파일 / 모듈 |
| :--- | :--- | :--- |
| **1. 카메라·LiDAR·Radar 센서 데이터 분석** | 다중 센서 객체(위치, 상대속도, Confidence) 데이터 구조 정의 및 파싱 | `src/perception.py` |
| **2. 학습/인식 데이터 구축 및 관리** | 35개 합성 센서 테스트 시나리오 데이터셋 자동 생성 | `evaluate.py` |
| **3. Perception 모델 개발 및 검증** | 센서별 Confidence Threshold 기반 객체 검출 및 노이즈 필터링 | `src/perception.py` |
| **4. Data Reliability (신뢰성) 검증** | 센서 이상치(음수 거리 등) 필터링 및 프레임별 신뢰도 점수 산출 | `src/reliability.py` |
| **5. Safety Warning (안전 경고) 시스템** | TTC (Time-to-Collision) 기반 실시간 충돌 위험도 3단계 경고 발송 | `src/safety_warning.py` |
| **6. 정량 평가 및 지표 리포팅** | 35개 테스트 세트 대상 Latency, Precision 자동 측정 및 `metrics.json` 출력 | `evaluate.py` |

---

## 2. 프로젝트 아키텍처

```text
  ┌──────────────────────────────┐
  │  Multi-Sensor Raw Data       │ (Camera, LiDAR, Radar)
  └──────────────┬───────────────┘
                 │
                 ▼
  ┌──────────────────────────────┐
  │  1. Perception Module        │ -> Parse Distance, Rel-Velocity, Confidence
  └──────────────┬───────────────┘
                 │
                 ▼
  ┌──────────────────────────────┐
  │  2. Reliability Evaluator    │ -> Filter low-confidence & Noise data
  └──────────────┬───────────────┘
                 │
                 ▼
  ┌──────────────────────────────┐
  │  3. Safety Warning System    │ -> Calculate TTC (Time-to-Collision)
  └──────────────┬───────────────┘ -> Trigger (SAFE / WARNING / CRITICAL_DANGER)
                 │
                 ▼
  ┌──────────────────────────────┐
  │  4. Automated Evaluation     │ -> Output 'evaluation/metrics.json'
  └──────────────────────────────┘
