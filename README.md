# DetectGPT_kor

2023년 1월 스탠포드 대학교에서 발간한 DetectGPT논문을 참고하였습니다.
([DetectGPT논문](https://arxiv.org/pdf/2301.11305))

코드는 BurhanUlTayyab/DetectGPT 깃헙을 참고하였습니다.


## USAGE
코드 실행
```
python infer_cg.py
```
데이터프레임을 불러와 생성된 문장인지 아닌지를 추론하는 파일입니다.
실시간으로 탐지 결과가 데이터프레임 결과파일로 저장되도록 하였습니다.

```
model_korean.py
```
논문에서 제안한 purturbation에 활용된 t5 모델로, 한국어 오픈소스 모델인 pko-t5-base를 활용하였습니다.
확률을 구하는 모델로는 본 연구에서는 생성에 활용하였던 kullm 모델을 사용하였습니다.


## Acknowledgements
Mitchell, Eric, et al. "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature." arXiv preprint arXiv:2301.11305 (2023).
