from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = ChatGroq(
    groq_api_key='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',
    model="llama-3.1-70b-versatile",
    temperature=0.0,
    max_retries=2,
)
def gen_res_name_and_menu(cuissine):
    res_name = PromptTemplate(
        input_variables=['cussine'],
        template="i want to open a resturant for {cussine} food, suggest me a only one fancy name.")
    chain1 = LLMChain(llm=llm, prompt=res_name, output_key='resturant_name')
    menu_name = PromptTemplate(
        input_variables=['resturant_name'],
        template="suggest me some menu items for {resturant_name}.return it as comma seperated list""")
    chain2 = LLMChain(llm=llm, prompt=menu_name, output_key='menu')

    chain = SequentialChain(chains=[chain1, chain2],
                            input_variables=['cussine'],
                            output_variables=['resturant_name', 'menu'])
    response = chain({'cussine': cuissine})
    return response
if __name__ == '__main__':
    re = gen_res_name_and_menu('indian')
    print(re)