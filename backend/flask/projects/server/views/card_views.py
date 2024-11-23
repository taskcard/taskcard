from flask import Blueprint, request ,session ,g ,jsonify


from datetime import datetime
from server import db
from server.models import Card

bp = Blueprint('card', __name__, url_prefix='/card') #블루프린트 객체 생성

print("CARD_VIEW 진입")

@bp.route('/', methods=['GET'])
def get_cards():
    try:
        cards = Card.query.all()

        # 카드 데이터를 JSON 형식으로 변환
        card_list = []
        for card in cards:
            card_list.append({
                "id": card.id,
                "title": card.title,
                "content": card.content,
                "category": card.category,
                "create_date": card.create_date.strftime('%Y-%m-%d %H:%M:%S')
            })

        return jsonify({"cards": card_list}), 200
    except Exception as e:
        return jsonify({"error": "카드 데이터를 불러오는 중 오류가 발생했습니다.", "details": str(e)}), 500

#카드 생성 라우터
@bp.route('/create/', methods=['POST'])
def create():
    print("카드 생성 라우터 실행")
    try:
        # JSON 형식으로 입력값 받아오기
        json = request.get_json()
        
        title = json.get("title")
        content = json.get("content")
        category = json.get("category")

        # 필수 값 누락 확인
        if not title or not content or not category:
            return jsonify({"error": "필수 입력 값 누락"}), 400

        # 카드 생성
        card = Card(
            title=title,
            content=content,
            category=category,
            create_date=datetime.now()
        )
        db.session.add(card)
        db.session.commit()

        # 성공 응답
        return jsonify({
            "success": "카드 생성 완료",
            "card": {
                "id": card.id,
                "title": card.title,
                "content": card.content,
                "category": card.category,
                "create_date": card.create_date.strftime('%Y-%m-%d %H:%M:%S')
            }
        }), 201
    
    #예외 처리
    except Exception :
        db.session.rollback()  
        return jsonify({"error": "카드 생성 중 오류가 발생했습니다."}), 500

#카드 삭제 라우터
@bp.route('/delete/<int:card_id>', methods=['DELETE'])
def delete(card_id):
    try:
        print("카드 삭제 라우터 실행")
        # 카드 조회
        card = Card.query.get_or_404(card_id)

        # 카드 삭제
        db.session.delete(card)
        db.session.commit()

        return jsonify({"success": "카드 삭제 완료", "card_id": card_id}), 200
    except Exception :
        db.session.rollback()  # 오류 발생 시 롤백
        return jsonify({"error": "카드 삭제 중 오류가 발생"}), 500
    
#카드 수정 라우터
@bp.route('/modify/<int:card_id>', methods=['POST'])
def modify(card_id):
    print("카드 수정 라우터 실행")
    # 데이터베이스에서 해당 카드 가져오기
    card = Card.query.get_or_404(card_id)
    
    
    # JSON 형식으로 입력값 받아오기
    json = request.get_json()
    
    title = json.get("title")
    content = json.get("content")
    category = json.get("category")

    # 필수 값 검증
    if not title or not content or not category:
        return jsonify({"error": "필수 입력 값 누락"}), 400
    
    

    try:
        # 카드 정보 업데이트
        card.title = title
        card.content = content
        card.category = category
        card.modify_date = datetime.now()  # 수정 시간 저장

        # 데이터베이스 커밋
        db.session.commit()

        return jsonify({
            "success": "카드 수정 완료",
            "card": {
                "id": card.id,
                "title": card.title,
                "content": card.content,
                "category": card.category,
                "modify_date": card.modify_date.strftime('%Y-%m-%d %H:%M:%S')
            }
        }), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "카드 수정 중 오류가 발생했습니다."}), 500