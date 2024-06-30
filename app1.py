from flask import Flask, render_template, request
import os
from ibm_watsonx_ai.foundation_models import Model

app = Flask(__name__)

# Define your credentials and other configurations
def get_credentials():
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": "0jsxGfblp-HeuEwldAVpvsxrlNhT7Lp9y92JHFzkj0e6"
    }

model_id = "ibm/granite-13b-chat-v2"
parameters_0 = {
    "decoding_method": "greedy",
    "max_new_tokens": 2,
    "repetition_penalty": 1
}
parameters_1 = {
    "decoding_method": "greedy",
    "max_new_tokens": 100,
    "repetition_penalty": 1
}
parameters_2 = {
    "decoding_method": "greedy",
    "max_new_tokens": 80,
    "repetition_penalty": 1
}

model_0 = Model(
    model_id=model_id,
    params=parameters_0,
    credentials=get_credentials(),
    project_id="b357c08e-c45b-4721-8e03-ffb9c3fa4924",
    #space_id=space_id
)

model_1 = Model(
    model_id=model_id,
    params=parameters_1,
    credentials=get_credentials(),
    project_id="b357c08e-c45b-4721-8e03-ffb9c3fa4924",
    #space_id=space_id
)

model_2 = Model(
    model_id=model_id,
    params=parameters_2,
    credentials=get_credentials(),
    project_id="b357c08e-c45b-4721-8e03-ffb9c3fa4924",
    #space_id=space_id
)


@app.route('/', methods=['GET','POST'])
def home():
    prompt_input_0 = """analyze the input text and respond 1, 2. If input describes about a project idea then respond 1, if input is asking whether a material is good or not then respond 2

    Input: The project aims to plant thousands of trees in urban areas across the city. By creating green corridors and expanding green spaces, it will enhance urban biodiversity, provide shade, improve air quality, and reduce the urban heat island effect. Additionally, the project will engage local communities through educational programs about the benefits of trees.
    Output: 1

    Input: The project involves replacing traditional lighting in public buildings with energy-efficient LED lights. This upgrade aims to reduce energy consumption and lower the buildings' carbon footprint.
    Output: 1

    Input: The project proposes constructing a new highway to alleviate traffic congestion in the city. The highway will cut through several natural habitats and require significant land clearing.
    Output: 1

    Input: The project seeks to start oil drilling operations in a marine protected area, arguing that it will boost the local economy and energy independence. The drilling site is home to several endangered marine species.
    Output: 1

    Input: I would like to use plastic to make the container.
    Output: 2

    Input: Is Styrofoam good for making the padding.
    Output: 2

    Input: Is bamboo a good choice of material.
    Output: 2


    """
    prompt_input_1 = """analyze the project idea description and respond Very good, Good, Bad, Very bad depending on its impact on environment. And if any products are listed analyze each product and classify them into very good, good and bad and sugeest their best alternative.

    Input: The project aims to plant thousands of trees in urban areas across the city. By creating green corridors and expanding green spaces, it will enhance urban biodiversity, provide shade, improve air quality, and reduce the urban heat island effect. Additionally, the project will engage local communities through educational programs about the benefits of trees.
    Output: Very good. This project will improve air quality, reduce urban heat islands, and increase biodiversity in cities. Planting trees also sequesters carbon, helping mitigate climate change.

    Input: This initiative seeks to deploy solar-powered water purification units in rural and remote areas. These systems use renewable solar energy to purify contaminated water sources, providing clean drinking water to communities without access to safe water.
    Output: Very good. This project uses renewable solar energy to provide clean drinking water, reducing reliance on fossil fuels and decreasing waterborne diseases without emitting pollutants.

    Input: The project involves replacing traditional lighting in public buildings with energy-efficient LED lights. This upgrade aims to reduce energy consumption and lower the buildings' carbon footprint.
    Output: Good. This project will reduce energy consumption and lower carbon emissions, though it does not address renewable energy sources.

    Input: This project proposes installing green roofs on commercial buildings in the downtown area. Green roofs will help reduce stormwater runoff, provide insulation, and create green spaces in urban environments.
    Output: Good. Green roofs offer multiple environmental benefits, including reduced stormwater runoff and improved insulation, though their impact is limited to specific buildings.

    Input: The project proposes constructing a new highway to alleviate traffic congestion in the city. The highway will cut through several natural habitats and require significant land clearing.
    Output: Bad. Constructing a new highway will destroy natural habitats, increase pollution, and encourage more car use, contributing negatively to the environment.

    Input: This project aims to develop a large shopping mall in a suburban area, which will include vast parking spaces and attract heavy traffic. It promises economic growth and job creation.
    Output: Bad. Developing a large shopping mall in suburban areas increases urban sprawl, traffic congestion, and pollution, negatively impacting the environment.

    Input: The project seeks to start oil drilling operations in a marine protected area, arguing that it will boost the local economy and energy independence. The drilling site is home to several endangered marine species.
    Output: Very bad. Oil drilling in a marine protected area endangers marine life, risks oil spills, and contributes to climate change, causing significant environmental harm.

    Input: This project aims to establish a large-scale industrial mining operation in a pristine forest region rich in minerals. It promises significant economic benefits and job creation for the local community.
    Output: Very bad. Large-scale mining in a pristine forest leads to deforestation, habitat destruction, and pollution of water sources, with devastating environmental impacts.

    Input: The project focuses on developing packaging materials made from biodegradable and compostable substances, such as plant-based plastics and recycled paper. This eco-friendly packaging will replace traditional plastic packaging used by local businesses.
    Output: Very good. This project aims to create biodegradable and compostable packaging materials, reducing plastic waste and pollution in landfills and oceans.

    Input: This project involves expanding the city's public transportation network by adding new bus and rail lines, improving service frequency, and enhancing accessibility for all residents. It aims to encourage more people to use public transportation instead of private cars.
    Output: Very good. Improving public transportation reduces the number of individual car trips, lowering greenhouse gas emissions and decreasing traffic congestion.

    Input: The project proposes building a new airport in a wetland area to accommodate increasing air travel demands. The wetlands are crucial habitats for numerous bird species and play a vital role in flood control.
    Output: Very bad. Constructing an airport in a wetland area destroys critical habitats, disrupts ecosystems, and increases pollution, severely impacting the environment.

    Input: The project involves expanding a chemical plant's production capacity near a residential area. The plant has a history of toxic emissions and chemical spills, raising health and safety concerns.
    Output: Very bad. Expanding a chemical plant near residential areas increases the risk of toxic emissions and chemical spills, endangering public health and the environment.

    Input: The project involves expanding the capacity of an existing coal-fired power plant to meet growing energy demands. This expansion will increase coal consumption and associated emissions.
    Output: Bad. Expanding a coal-fired power plant will significantly increase carbon emissions and air pollution, harming the environment and public health.

    """
    prompt_input_2 = """suggest the best alternative of the input material or object or process and explain how is it better. If it is already sustainable then just tell its a good choice and explain why. Give a sustainability  outlook of the input material

    Input: Is Plastic used for making bottles a good idea
    Output: BAD CHOICE ,A good alternative is stainless steel bottles. Stainless steel bottles are better because they are durable, reusable, and do not leach harmful chemicals into the water. They also reduce plastic waste in landfills and oceans.

    Input: Is using Styrofoam for Packaging good
    Output:  BAD CHOICE ,A good alternative is biodegradable packaging made from cornstarch. Cornstarch packaging is better because it breaks down naturally in the environment without leaving toxic residues, reducing pollution and waste.

    Input: Conventional Diesel Engines for making a car
    Output: BAD CHOICE ,A good alternative is electric engines. Electric engines are better because they produce zero emissions, reducing air pollution and greenhouse gas emissions, contributing to cleaner air and combating climate change.

    Input: Synthetic Fertilizers used instead of Organic fertilizers
    Output: BAD CHOICE ,A good alternative is compost or organic fertilizers. Organic fertilizers are better because they improve soil health, promote biodiversity, and do not cause chemical run-off that can harm waterways and aquatic life.

    Input: Single-Use Plastic Straws
    Output: BAD CHOICE ,A good alternative is reusable metal straws. Metal straws are better because they can be used repeatedly, reducing plastic waste and environmental pollution. They are also easy to clean and durable.

    Input: Bamboo for making chair
    Output: GOOD CHOICE ,Bamboo is already a good choice. It is a highly sustainable material that grows rapidly without the need for pesticides or fertilizers. Bamboo is also biodegradable and has a lower environmental impact compared to traditional wood or plastic.

    Input: Recycled Paper
    Output: GOOD CHOICE ,Recycled paper is already a good choice. It reduces the need for virgin wood pulp, conserving trees and natural habitats. It also uses less energy and water during production and reduces landfill waste.

    Input: LED Lighting
    Output: GOOD CHOICE ,LED lighting is already a good choice. It is highly energy-efficient, using up to 80% less energy than traditional incandescent bulbs. LED lights also have a longer lifespan, reducing the need for frequent replacements and reducing waste.

    Input: Solar Panels
    Output: GOOD CHOICE ,Solar panels are already a good choice. They generate clean, renewable energy from the sun, reducing reliance on fossil fuels and decreasing greenhouse gas emissions. Solar panels also help in reducing electricity bills and promoting energy independence.

    Input: Electric Bicycles
    Output: GOOD CHOICE ,Electric bicycles are already a good choice. They provide an eco-friendly mode of transportation, reducing the reliance on cars and lowering carbon emissions. Electric bicycles also promote physical activity and can help alleviate traffic congestion.

    Input: Styrofoam container for ice cream
    Output:  A bad option but there isn't really any alternatives since this type if package specifically designed fo hold cold items like Icecreams etc.. However one could choose non disposable options such as bowls/cup which would still use some form o Packing materials though reduced significantly compare dto styros

    """
    if request.method == 'POST':
        user_input = request.form['user_input']
        prompt_input_0+='Input: '+user_input+'\n'+'Output: '
        generated_response = model_0.generate_text(prompt=prompt_input_0, guardrails=True)
        response = generated_response
        #return render_template('index.html',response=response)
        if generated_response=='\n1':
            project_name = 'Project Idea'
            prompt_input_1 = prompt_input_1
            prompt_input_1+='Input:\n'+user_input+'\n'+'Output: '
            response = project_name + "\n" + model_1.generate_text(prompt=prompt_input_1, guardrails=True)
            return render_template('index.html',response=response)
        elif generated_response=='\n2':
            project_name = 'Product'
            prompt_input_2 = prompt_input_2
            prompt_input_2+='Input: '+user_input+'\n'+'Output: '
            response = project_name + "\n" + model_2.generate_text(prompt=prompt_input_2, guardrails=True)
            return render_template('index.html',response=response)
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)