from flask import Flask,render_template,request,redirect,url_for
import os
from ibm_watsonx_ai.foundation_models import Model

def get_credentials():
  return {
      "url": "https://us-south.ml.cloud.ibm.com",
      "apikey": "0jsxGfblp-HeuEwldAVpvsxrlNhT7Lp9y92JHFzkj0e6"
  }

model_id = "ibm/granite-13b-chat-v2"
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

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
  return render_template("home.html")

@app.route("/Project_management", methods=['POST', 'GET'])
def Project_management():
  return render_template("project_mang.html")

@app.route("/Project_idea_Evaluation", methods=['POST', 'GET'])
def Project_idea():
  prompt_input_1_n = """analyze the project idea description and respond Very good, Good, Bad, Very bad depending on its impact on environment. And if any products are listed analyze each product and classify them into very good, good and bad and sugeest their best alternative.

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
  if request.method == "POST" and 'f1' in request.form:
      response=""
      user_input = request.form.get('user_input')
      if user_input:
        # Proceed with analysis
        prompt_input_1 = prompt_input_1_n
        user_input= str(user_input)
        prompt_input_1+='Input:\n'+user_input+'\n'+'Output: '
        response = "\n" + model_1.generate_text(prompt=prompt_input_1, guardrails=True)
        return render_template('project_idea.html', response=response)
    
      
  
  return render_template("project_idea.html", response=None)

  
@app.route("/Material_choosing", methods=['POST', 'GET'])
def Material_choosing():
  return render_template("mat_cho.html")

@app.route("/Credits", methods=['POST', 'GET'])
def Credits():
  return render_template("credits.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)