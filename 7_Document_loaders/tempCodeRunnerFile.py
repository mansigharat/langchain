from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/Apple-MacBook-Laptop-18%E2%80%91core-40%E2%80%91core/dp/B0GR1LB81D/ref=sr_1_1_sspa?adgrpid=1322714098160313&dib=eyJ2IjoiMSJ9.xJjdcUHZhSkw41sr_ipfCtc3y390NkBpZxykhNzWYi7jXcYFLuvDkjGjyt9KcmuqvwU2s447YzAkdBOHt-KsJhZ-L-iRwGi8kMDj5V4REj-2fqdA-tqplaWtwx6eocXoXh4BK2Mf4U3GnVUQNGyvsYXBUtNZgIHfUHYz54kD00UOjSe70jtoK0-RHaTrHhOeOTs8tmciHZS6zg91qDdNlYVRBFryRsJOYTBjKK2odms.xjkVMkJ6GuLtypPpJx5IphUBgQo-rYfRQzSacLqNjKM&dib_tag=se&hvadid=82669902128852&hvbmt=be&hvdev=c&hvlocphy=259485&hvnetw=o&hvqmt=e&hvtargid=kwd-82670516595518%3Aloc-90&hydadcr=26949_2800346&keywords=apple%2Bmac%2Bbook&mcid=cf633135cb6938c2a1aae88a95f0077d&msclkid=2e55fd8ee1401867bdb2970e79efeb2b&qid=1786812597&sr=8-1-spons&aref=Mvt6fHtidz&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

loader = WebBaseLoader(url)

docs = loader.load()
print(len(docs))
print(docs[0].page_content)
