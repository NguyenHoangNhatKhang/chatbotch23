import json

otemae_university_info = {
    "name": "大手前大学",
    "romaji": "Otemae University",
    "vietnamese_name": "Đại học Otemae",
    "type": "私立大学 (Trường đại học tư lập)",
    "founded": 1946,
    "established_as_university": 1966,
    "founder": "大手前学園 (Otemae Gakuen Educational Foundation)",
    "president": "嘉宏義弘 (Yoshihiro Kaneko)",
    "motto": "未来への扉を開く、個性を育てる (Mở cánh cửa tới tương lai, nuôi dưỡng cá tính)",
    "philosophy_vi": "Đại học Otemae hướng đến việc đào tạo những con người có tri thức, đạo đức và sáng tạo — phát huy cá tính để đóng góp cho xã hội toàn cầu.",
    "symbol": {
        "color": "青 (xanh dương)",
        "flower": "桜 (hoa anh đào)",
        "meaning": "Tượng trưng cho tri thức, hy vọng và sự phát triển bền vững"
    },
    "overview_vi": "Đại học Otemae là trường tư thục hàng đầu khu vực Kansai, Nhật Bản, nổi tiếng với môi trường học hiện đại, thân thiện và cởi mở với sinh viên quốc tế. Trường có các ngành học đa dạng từ Kinh doanh, Xã hội học, Nghệ thuật, Kiến trúc đến Điều dưỡng, với cơ sở vật chất tiên tiến và đội ngũ giảng viên tận tâm.",
    
    "statistics": {
        "student_population": 6000,
        "international_students": 680,
        "countries_represented": ["Việt Nam", "Nepal", "Trung Quốc", "Myanmar", "Hàn Quốc", "Thái Lan"],
        "employment_rate": "94.2%",
        "male_to_female_ratio": "45:55",
        "average_tuition_per_year_yen": 1300000
    },

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
                "看護実習センター",
                "キャリアサポート室",
                "ジム・トレーニングルーム",
                "保健センター"
            ],
            "specializations": ["看護学部", "現代社会学部"],
            "description_vi": "Khuôn viên Itami tập trung vào Điều dưỡng và Xã hội học, với trang thiết bị thực hành hiện đại, môi trường học tập thoải mái, yên tĩnh."
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
                "グローバル交流ラウンジ",
                "ラーニングコモンズ",
                "スタジオ・デザイン室"
            ],
            "specializations": ["国際日本学部", "経営学部", "建築・芸術学部"],
            "description_vi": "Sakura Shukugawa Campus là khuôn viên chính của trường, nổi tiếng với cảnh quan đẹp, gần Kobe và Osaka, có khu học xá hiện đại và trung tâm giao lưu quốc tế."
        }
    ],

    "academic_programs": {
        "undergraduate": ["現代社会学部", "国際日本学部", "経営学部", "看護学部", "建築・芸術学部"],
        "graduate": ["現代社会研究科", "経営学研究科", "看護学研究科"],
        "language_courses": {
            "japanese_preparatory": "Khóa học tiếng Nhật dành cho du học sinh (6 tháng – 1 năm)",
            "topics": ["会話 (giao tiếp)", "文法 (ngữ pháp)", "読解 (đọc hiểu)", "ビジネスマナー (nghi thức doanh nghiệp)"]
        },
        "short_term_programs": [
            "Khóa học ngắn hạn về văn hóa Nhật Bản",
            "Chương trình trải nghiệm kinh doanh Kansai",
            "Workshop thiết kế sáng tạo"
        ]
    },

    "scholarships": [
        "成績優秀者奨学金 (Học bổng thành tích học tập xuất sắc)",
        "留学生特別奨学金 (Học bổng đặc biệt cho du học sinh, giảm 30-50% học phí)",
        "経済支援奨学金 (Hỗ trợ tài chính)",
        "地域社会貢献奨学金 (Học bổng cống hiến xã hội)",
        "研究助成金 (Hỗ trợ nghiên cứu)"
    ],

    "international_exchange": {
        "partner_universities": [
            "ハノイ大学（ベトナム）",
            "韓国・ソウル女子大学",
            "タイ・チュラロンコン大学",
            "アメリカ・オレゴン州立大学",
            "マレーシア・サンウェイ大学"
        ],
        "student_exchange_rate": "12% sinh viên có kinh nghiệm du học hoặc trao đổi",
        "program_types": [
            "短期語学研修（アメリカ・韓国・ベトナム）",
            "交換留学プログラム (1 học kỳ – 1 năm)",
            "海外インターンシップ"
        ]
    },

    "career_support": {
        "employment_rate": "94%",
        "major_employers": ["三菱UFJ銀行", "楽天グループ", "JTB", "ANA", "神戸市役所"],
        "services": [
            "就職相談・面接練習",
            "インターンシップ紹介",
            "企業説明会",
            "履歴書・ES添削"
        ],
        "career_center_portal": "https://career.otemae.ac.jp"
    },

    "facilities": {
        "library": {
            "books": 300000,
            "digital_access": True,
            "features": ["自習スペース", "貸出予約システム", "オンラインデータベース"]
        },
        "cafeteria": {
            "menu": ["和食", "洋食", "ベジタリアンメニュー", "アレルギー対応食"],
            "price_range_yen": "300–600円"
        },
        "sports": [
            "屋内体育館",
            "サッカーグラウンド",
            "トレーニングジム"
        ],
        "dormitories": [
            "男子寮（Itami）",
            "女子寮（Shukugawa）",
            "国際学生寮（Osaka）"
        ]
    },

    "community_engagement": [
        "地域清掃活動 (Hoạt động làm sạch khu vực)",
        "子供向け教育ボランティア (Tình nguyện dạy học cho trẻ em)",
        "環境保護キャンペーン (Chiến dịch bảo vệ môi trường)",
        "災害復興支援 (Hỗ trợ phục hồi sau thiên tai)"
    ],

    "alumni": [
        {"name": "山田太郎", "career": "政治家 (Chính trị gia)", "achievement": "Đóng góp cải cách giáo dục vùng Kansai"},
        {"name": "佐藤花子", "career": "作家 (Tác giả)", "achievement": "Tác giả cuốn sách '未来への扉'"},
        {"name": "鈴木一郎", "career": "企業家 (Doanh nhân)", "achievement": "Sáng lập startup công nghệ xã hội tại Osaka"}
    ],

    "faq": [
        {"question": "Otemae có học bổng cho du học sinh không?", "answer": "Có, học bổng giảm học phí 30–50% tùy theo thành tích và hoàn cảnh."},
        {"question": "Trường có ký túc xá riêng cho sinh viên quốc tế không?", "answer": "Có, ký túc xá quốc tế với quản lý 24/7 và khu sinh hoạt chung."},
        {"question": "Tôi có thể làm thêm khi học tại Otemae không?", "answer": "Có, du học sinh được phép làm thêm 28 giờ/tuần theo luật Nhật."}
    ],

    "fun_facts": [
        "Tên 'Otemae' bắt nguồn từ cổng Otemon của Lâu đài Himeji.",
        "Trường có linh vật riêng tên là 'おおてまるくん'.",
        "Khuôn viên Sakura Shukugawa từng được chọn làm địa điểm quay phim truyền hình Nhật.",
        "Tỉ lệ sinh viên nữ cao hơn nam – thể hiện tinh thần đa dạng giới."
    ],

    "website": "https://www.otemae.ac.jp",
    "contact": {
        "address": "〒664-0861 兵庫県伊丹市稲野町2丁目2番地",
        "phone": "072-770-6334",
        "email": "info@otemae.ac.jp",
        "admission_office": "入試広報部 (Admissions Office)",
        "admission_email": "nyushi@otemae.ac.jp"
    },
    "social_media": {
        "facebook": "https://www.facebook.com/otemae.university",
        "twitter": "https://twitter.com/otemae_univ",
        "instagram": "https://www.instagram.com/otemae_university/",
        "youtube": "https://www.youtube.com/user/otemaeuniversity"
    },
     "departments_overview": [
        {
            "name": "現代社会学部 (Khoa Xã hội đương đại)",
            "focus": "Nghiên cứu xã hội, truyền thông, chính trị, văn hóa hiện đại.",
            "courses": [
                {"name": "社会学入門", "vietnamese_name": "Nhập môn xã hội học", "credits": 2, "description": "Tìm hiểu cơ cấu và vấn đề của xã hội hiện đại."},
                {"name": "メディア論", "vietnamese_name": "Lý luận truyền thông", "credits": 2, "description": "Phân tích vai trò của truyền thông trong xã hội toàn cầu."},
                {"name": "心理学基礎", "vietnamese_name": "Cơ sở tâm lý học", "credits": 2, "description": "Nghiên cứu tâm lý con người trong bối cảnh xã hội."},
                {"name": "地域社会研究", "vietnamese_name": "Nghiên cứu cộng đồng địa phương", "credits": 2, "description": "Tìm hiểu sự phát triển của xã hội địa phương Nhật Bản."}
            ]
        },
        {
            "name": "国際日本学部 (Khoa Nhật Bản học quốc tế)",
            "focus": "Giảng dạy tiếng Nhật, văn hóa, giao lưu quốc tế và nghiên cứu Nhật Bản.",
            "courses": [
                {"name": "日本語表現", "vietnamese_name": "Diễn đạt tiếng Nhật", "credits": 2, "description": "Luyện kỹ năng viết và nói trong tiếng Nhật học thuật."},
                {"name": "日本文化史", "vietnamese_name": "Lịch sử văn hóa Nhật Bản", "credits": 2, "description": "Nghiên cứu sự phát triển của văn hóa truyền thống Nhật Bản."},
                {"name": "国際関係論", "vietnamese_name": "Quan hệ quốc tế", "credits": 2, "description": "Hiểu về mối quan hệ giữa Nhật Bản và các nước khác."},
                {"name": "異文化コミュニケーション", "vietnamese_name": "Giao tiếp đa văn hóa", "credits": 2, "description": "Thực hành kỹ năng giao tiếp trong môi trường đa văn hóa."}
            ]
        },
        {
            "name": "経営学部 (Khoa Kinh doanh)",
            "focus": "Đào tạo kiến thức về quản trị, marketing, kế toán và khởi nghiệp.",
            "courses": [
                {"name": "経営学原論", "vietnamese_name": "Nguyên lý quản trị kinh doanh", "credits": 2, "description": "Khái quát nền tảng của lý thuyết quản trị hiện đại."},
                {"name": "マーケティング入門", "vietnamese_name": "Nhập môn marketing", "credits": 2, "description": "Phân tích hành vi người tiêu dùng và chiến lược tiếp thị."},
                {"name": "会計基礎", "vietnamese_name": "Cơ sở kế toán", "credits": 2, "description": "Giới thiệu nguyên tắc ghi sổ và báo cáo tài chính."},
                {"name": "起業論", "vietnamese_name": "Khởi nghiệp học", "credits": 2, "description": "Phát triển ý tưởng kinh doanh và kỹ năng khởi nghiệp."}
            ]
        },
        {
            "name": "建築・芸術学部 (Khoa Kiến trúc & Nghệ thuật)",
            "focus": "Đào tạo kỹ năng thiết kế, nghệ thuật thị giác, kiến trúc bền vững.",
            "courses": [
                {"name": "建築設計基礎", "vietnamese_name": "Cơ sở thiết kế kiến trúc", "credits": 2, "description": "Nghiên cứu cấu trúc, không gian và thiết kế công trình."},
                {"name": "デジタルデザイン", "vietnamese_name": "Thiết kế kỹ thuật số", "credits": 2, "description": "Học cách sử dụng công cụ đồ họa hiện đại trong thiết kế."},
                {"name": "アート理論", "vietnamese_name": "Lý luận nghệ thuật", "credits": 2, "description": "Phân tích các trường phái nghệ thuật cổ điển và hiện đại."},
                {"name": "環境デザイン", "vietnamese_name": "Thiết kế môi trường", "credits": 2, "description": "Tạo dựng không gian sống bền vững và thân thiện môi trường."}
            ]
        },
        {
            "name": "看護学部 (Khoa Điều dưỡng)",
            "focus": "Đào tạo y tá chuyên nghiệp, kỹ năng chăm sóc, và y tế cộng đồng.",
            "courses": [
                {"name": "基礎看護学", "vietnamese_name": "Điều dưỡng cơ bản", "credits": 2, "description": "Hiểu nguyên tắc và kỹ thuật điều dưỡng cơ bản."},
                {"name": "臨床実習", "vietnamese_name": "Thực tập lâm sàng", "credits": 4, "description": "Thực hành chăm sóc bệnh nhân tại bệnh viện đối tác."},
                {"name": "解剖生理学", "vietnamese_name": "Giải phẫu – sinh lý học", "credits": 2, "description": "Học cấu trúc và chức năng cơ thể người."},
                {"name": "医療倫理", "vietnamese_name": "Đạo đức y học", "credits": 2, "description": "Rèn luyện ý thức nghề nghiệp và đạo đức y khoa."}
            ]
        }
    ],
}

# Ghi ra file
with open("ex.json", "w", encoding="utf-8") as f:
    json.dump(otemae_university_info, f, ensure_ascii=False, indent=4)


print("✅ Đã tạo file otemae_university_full.json thành công!")
