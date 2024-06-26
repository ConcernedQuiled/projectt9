import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cponsjpr01qiv403hrr0cponsjpr01qiv403hrrg")

    news = finnhub_client.general_news('general', min_id=0)

    return news
