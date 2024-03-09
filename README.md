# 사업자 정보 확인 함수

[공공데이터포털](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15081808)에서 API키를 발급 받아야 사용가능합니다.

한번에 최대 100개까지 조회 가능합니다.

## 사업자 정보 확인
```
print( validate( [ ["사업자등록번호", "대표자명", "개업일자", "상호명"] ] ) )
```

## 사업자 상태 확인
```
print( status( ["사업자등록번호"] ) )
```
