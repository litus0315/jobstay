# import requests
# from models import City
#
# from domain.job import job_schema
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmakera
#
# # 데이터베이스 연결 URL 정의 (예: SQLite 사용 시)
# DATABASE_URL = "sqlite:///./myapi.db"  # 사용하는 데이터베이스에 맞게 조정
#
# # 데이터베이스 엔진 생성
# engine = create_engine(DATABASE_URL)
#
# # 세션 생성을 위한 세션 팩토리 구성
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # 세션 인스턴스 생성
# db = SessionLocal()
#
#
#
#
#
#
#
# url = "https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000"
# response = requests.get(url)
# sido_list = response.json()['regcodes']
#
# city = job_schema.City
# for sido in sido_list:
#     sido_code = sido['code'][0:2]
#     sido_name = sido['name']
#     print(sido_name)
#     city.sido = sido_name
#
#     url = "https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=" + sido_code + "*00000"
#     response = requests.get(url)
#     gugun_list = response.json()['regcodes']
#     for gugun in gugun_list:
#         gugun_name = gugun['name']
#         city.gugun = gugun_name
#
#         db_city = City(sido=city.sido, gugun=city.gugun)
#
#         db.add(db_city)
#
#     db.commit()
