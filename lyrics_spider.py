import scrapy



class LyricsSpider(scrapy.Spider):
    name = 'rap'

    urls = []
    artists = '3030 1kilo adl-mcs afro-x azzy baco-exu-do-blues bin bk black-alien bnegao c4bal cacife-clandestino cartel-mcs choice chris cone-crew-diretoria coruja-bc1 costa-gold criolo cynthia-luz dalsin delacruz de-leve dfideliz diomedes-chinaski djonga don-l drik-barbosa dudu-mc emicida fabio-brazza faccao-central felp22 flora-matos froid gaab gabriel-pensador gloria-groove haikaiss hungria-hip-hop jaya-luuck je-santiago kamau karol-conka kayua kiaz l7nnon luccas-carlos makalister-renton mano-brown marcelo-d2 matue mc-hariel-sp mc-marechal mc-orochi mr-thug mv-bill nabrisa-tonett negra-li nill nill ogi oriente pele-milflows projota quinto-andar racionais-mcs rael rappin-hood rashid ret rincon-sapiencia sabotage sant shawlin sidoka slim-rimografia speed-freaks tulio-dek ucl xama'.split()
    for artist in artists:
        urls.append(f'https://www.letras.mus.br/{artist}/')
    
    start_urls = urls

    def parse_author(self, response):
        song_page_links = response.css('a.song-name')
        yield from response.follow_all(song_page_links, self.parse_song)

        #pagination_links = response.css('li.next a')
        #yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):

        yield {
            'song': response.css("h1::text").get(),
            'artist': response.css("h2 a span::text").get(),
            'lyrics': response.css("div.cnt-letra p::text").getall(),
        }