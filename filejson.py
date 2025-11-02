import json 
otemae_university_info ={
    "name": "大手前大学",
    "romaji": "Otemae University",
    "vietnamese_name": "Đại học Otemae",
    "type": "私立大学 (Trường đại học tư lập)",
    "founded": 1946,
    "established_as_university": 1966,
    "motto": "未来への扉を開く、個性を育てる (Mở cánh cửa tới tương lai, nuôi dưỡng cá tính)",
    "symbol": {
        "color": "青 (xanh dương)",
        "flower": "桜 (hoa anh đào)",
        "meaning": "Tượng trưng cho sự phát triển, học hỏi, và tinh thần tự do"
    },
    "overview_vi": "Đại học Otemae là trường tư thục tại tỉnh Hyogo, Nhật Bản, nổi tiếng với môi trường học hiện đại, thân thiện và có nhiều chương trình hỗ trợ sinh viên quốc tế. Trường đặc biệt chú trọng giáo dục toàn diện, kết hợp giữa học thuật, kỹ năng thực tế và sáng tạo cá nhân.",
    "locations": [
        {
            "campus": "伊丹キャンパス (Itami Campus)",
            "address": "〒664-0861 兵庫県伊丹市稲野町2丁目2番地",
            "city": "伊丹市 (Itami)",
            "prefecture": "兵庫県 (Hyogo)",
            "access": "阪急稲野駅から徒歩2分",
            "facilities": [
                "学生食堂（C棟・G棟）",
                "図書館（約30万冊蔵書）",
                "キャリアサポート室",
                "コンピュータ室",
                "実習室・看護実験室",
                "ジム・トレーニングルーム"
            ],
            "specializations": ["看護学部", "現代社会学部"],
            "campus_description_vi": "Khuôn viên Itami là trung tâm đào tạo về Xã hội học và Điều dưỡng. Nơi đây có cơ sở vật chất hiện đại, thư viện lớn, và nhiều phòng thực hành cho sinh viên y tế."
        },
        {
            "campus": "さくら夙川キャンパス (Sakura Shukugawa Campus)",
            "address": "〒662-8552 兵庫県西宮市御茶家所町6番42号",
            "city": "西宮市 (Nishinomiya)",
            "prefecture": "兵庫県 (Hyogo)",
            "access": "阪急夙川駅から徒歩7分、JRさくら夙川駅から徒歩10分",
            "facilities": [
                "カフェテリア",
                "メディアセンター",
                "留学生支援オフィス",
                "グローバル交流ラウンジ",
                "ラーニングコモンズ"
            ],
            "specializations": ["国際日本学部", "経営学部", "建築・芸術学部"],
            "campus_description_vi": "Sakura Shukugawa Campus nằm gần Kobe và Osaka, mang phong cách hiện đại, có nhiều sinh viên quốc tế và là trung tâm giao lưu văn hóa – kinh doanh quốc tế."
        },
        {
            "campus": "大阪大手前キャンパス (Osaka Otemae Campus)",
            "address": "大阪府大阪市中央区大手前2丁目1-88",
            "city": "大阪市 (Osaka)",
            "prefecture": "大阪府 (Osaka)",
            "access": "地下鉄天満橋駅から徒歩5分",
            "facilities": [
                "情報処理センター",
                "講義棟",
                "交流スペース",
                "学生相談室"
            ],
            "campus_description_vi": "Khuôn viên Otemae tại Osaka chủ yếu dùng cho các lớp học chuyên ngành về CNTT, truyền thông và các chương trình học ngắn hạn."
        }
    ],
    "departments": [
        {"name": "現代社会学部", "description": "社会・メディア・教育を中心に学ぶ"},
        {"name": "国際日本学部", "description": "日本文化・国際交流・外国語教育"},
        {"name": "経営学部", "description": "ビジネス・会計・マーケティングを実践的に学ぶ"},
        {"name": "看護学部", "description": "看護実習・医療コミュニケーションを重視"},
        {"name": "建築・芸術学部", "description": "建築デザイン、空間構成、ビジュアルアート"}
    ],
    "tuition": [
        {"department": "現代社会学部", "amount_yen": 1200000},
        {"department": "経営学部", "amount_yen": 1300000},
        {"department": "看護学部", "amount_yen": 1500000},
        {"department": "国際日本学部", "amount_yen": 1250000},
        {"department": "建築・芸術学部", "amount_yen": 1350000}
    ],
    "graduate_school": {
        "name": "大手前大学大学院",
        "majors": ["現代社会研究科", "経営学研究科", "看護学研究科"],
        "description_vi": "Chương trình sau đại học tập trung vào nghiên cứu ứng dụng xã hội, quản trị và y tế, với các khóa học bán thời gian dành cho người đi làm."
    },
    "international_relations": {
        "partner_universities": [
            "ハノイ大学（ベトナム）",
            "タイ・チュラロンコン大学",
            "韓国・ソウル女子大学",
            "アメリカ・オレゴン州立大学",
            "マレーシア・サンウェイ大学"
        ],
        "exchange_programs": [
            "短期語学研修（アメリカ・韓国・ベトナム）",
            "ダブルディグリー制度",
            "オンライン国際交流プログラム"
        ],
        "support_for_international_students": [
            "留学生チューター制度",
            "日本語補習クラス",
            "生活ガイダンス・ビザ相談",
            "奨学金案内・就職支援"
        ]
    },
    "scholarships": [
        "成績優秀者向け奨学金",
        "経済支援奨学金",
        "留学生特別奨学金（授業料30〜50％免除）",
        "研究奨学金（文化・看護・経営系）",
        "地域貢献活動奨学金"
    ],
    "career_support": {
        "employment_rate": "約94％ (2024年度卒業生)",
        "major_employers": ["三菱UFJ銀行", "ANA", "神戸市役所", "楽天グループ"],
        "services": [
            "就職相談・面接指導",
            "インターンシップの紹介",
            "企業セミナー・合同説明会",
            "履歴書添削やESサポート"
        ],
        "portal": "https://career.otemae.ac.jp"
    },
    "library": {
        "location": "伊丹キャンパス",
        "books": 300000,
        "digital_resources": "電子書籍・データベース・学術論文アクセス可",
        "facilities": ["自習スペース", "グループ学習室", "オンライン検索", "貸出予約システム"]
    },
    "cafeteria": {
        "locations": ["C棟1階", "G棟1階"],
        "features": [
            "多様なメニューを低価格で提供",
            "ベジタリアン・アレルギー対応あり",
            "学生割引適用"
        ]
    },
    "dormitory": {
        "name": "大手前学生寮",
        "rent_yen_per_month": 35000,
        "facilities": ["Wi-Fi完備", "共用キッチン", "ランドリー", "セキュリティシステム", "自習スペース"],
        "rules_vi": "Ký túc xá riêng biệt nam/nữ, giờ giới nghiêm 23:00, có quản lý hỗ trợ du học sinh 24/7."
    },
    "student_life": {
        "clubs": ["サッカー部", "茶道部", "吹奏楽団", "写真サークル", "ボランティアクラブ", "IT研究会", "アニメ研究部"],
        "events": ["新入生歓迎祭", "文化祭（Otemae Festival）", "スポーツ大会", "オープンキャンパス"],
        "support_systems": ["留学生相談室", "メンタルケア", "チューター制度"]
    },
    "research": {
        "institutes": ["教育研究センター", "看護研究所", "地域共生研究室"],
        "topics": ["持続可能な社会", "地域活性化", "医療技術教育", "文化交流"]
    },
    "highlights": [
        "留学生が多く国際的な雰囲気",
        "ICTを活用したハイブリッド授業",
        "地域連携プロジェクト多数",
        "女性教員の比率が高く、多様性に富む",
        "学生の満足度が高い大学として評価"
    ],
    "fun_facts": [
        "「大手前」の名前は姫路城の大手前門に由来",
        "教育理念は『未来への扉を開く、個性を育てる』",
        "公式マスコットキャラクター『おおてまるくん』が存在",
        "卒業生の中には著名なアナウンサーやYouTuberもいる"
    ],
    "contact": {
        "address": "〒664-0861 兵庫県伊丹市稲野町2丁目2番地",
        "phone": "072-770-6334",
        "email": "info@otemae.ac.jp",
        "admission_office": "入試広報部 (Admissions Office)",
        "admission_email": "nyushi@otemae.ac.jp"
    }
}


with open("ex.json","w") as file:
    json.dump(otemae_university_info,file)
