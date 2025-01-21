COMPANY = {
    "Google": "https://deepmind.google/discover/blog/",
    "Socar": "https://tech.socarcorp.kr/tags/#ai",
    "당근 마켓": "https://medium.com/daangn/machine-learning/home",
    "Nexon intelligencelabs": "https://www.intelligencelabs.tech/machinelearning",
    "Kakao": "https://tech.kakao.com/tag/ai",
    "Kakao Bank": "https://tech.kakaobank.com/tags/ai/",
    "화해": "https://blog.hwahae.co.kr/category/all/tech",
    "컬리": "https://helloworld.kurly.com/",
    "쿠팡 엔지니어링": "https://medium.com/coupang-engineering/tagged/ai",
    "SKT" : "https://devocean.sk.com/",
    "스마일게이트": "https://smilegate.ai/recent/",
    "Naver D2": "https://d2.naver.com/home",
    "LINE": "https://techblog.lycorp.co.jp/ko",
    "우아한 형제들": "https://techblog.woowahan.com/",
    "Hyperconnect": "https://hyperconnect.github.io/",
    "Meta": "https://ai.meta.com/blog/?page=1",
    "Watcha": "https://medium.com/watcha",
    "Netflix": "https://netflixtechblog.com/",
    "uber": "https://www.uber.com/en-KR/blog/engineering/",
    "AWS": "https://aws.amazon.com/ko/blogs/machine-learning/",
    "LG AI": "https://www.lgresearch.ai/blog",
    "LG C&S": "https://www.lgcns.com/blog/",
    "Samsung": "https://techblog.samsung.com/blog",
    "채널톡": "https://channel.io/ko/blog/tag/tech",
    "스캐터랩": "https://tech.scatterlab.co.kr/",
    "NCSoft": "https://ncsoft.github.io/ncresearch/",
    "Dable": "https://dabletech.oopy.io/",
    "무신사": "https://medium.com/musinsa-tech",
    "원티드": "https://medium.com/wantedjobs",
    "토스": "https://toss.tech/tech",
    "Airbnb": "https://medium.com/airbnb-engineering",
    "Open AI": "https://openai.com/news/research/",
    "MicroSoft": "https://devblogs.microsoft.com/",
    "LinkedIn": "https://www.linkedin.com/blog/engineering/artificial-intelligence",
    "Towards Data Science": "https://towardsdatascience.com/",
    "Tensorflow": "https://blog.tensorflow.org/",
    "Apple": "https://machinelearning.apple.com/",
    "NVIDIA": "https://developer.nvidia.com/blog/",
    "업스테이지": "https://www.content.upstage.ai/blog",
    "CLOVA": "https://engineering.clova.ai/",
    "달파": "https://app.dalpha.so/blog/",
    "Adobe": "https://blog.developer.adobe.com/",
    "Databricks": "https://www.databricks.com/kr/blog",
    "C3.ai": "https://c3.ai/blog/",
    "H2O.ai": "https://h2o.ai/blog/",
    "Anthrophic": "https://www.anthropic.com/news",
    "RunWay": "https://runwayml.com/research",
    "HuggingFace": "https://huggingface.co/blog",
    "네이버 페이": "https://medium.com/naverfinancial",
}

COMMUNITY = {
    "모두의연구소": "https://modulabs.co.kr/blog/",
    "가짜연구소": "https://pseudolab.github.io/",
    "Analytics Vidhya": "https://www.analyticsvidhya.com/blog/",
    "KDnuggets": "https://www.kdnuggets.com/",
    "Berkeley AI Research": "https://bair.berkeley.edu/blog/",
    "MIT news": "https://news.mit.edu",
    "FastML": "https://fastml.com/"
}

company = sorted(COMPANY.items())
community = sorted(COMMUNITY.items())

description = "**수정 / 추가 해야할 내용 있다면 언제든 이슈에 남겨주세요**"

with open("README.md", "w") as f:
    f.write(
"""# ai-tech-blog

### AI tech blog 
"""
    )
    f.write("|**Company**|**URL**|\n")
    f.write("|---|---|\n")
    for k, v in company:
        f.write(f"|{k}|{v}|\n")
        
    f.write("\n\n|**Name**|**URL**|\n")
    f.write("|---|---|\n")
    for k, v in community:
        f.write(f"|{k}|{v}|\n")
        
    f.write("\n---\n")

    f.write(f"{description}")