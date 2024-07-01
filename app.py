from flask import Flask,render_template,request,redirect,url_for,session
from flask.sessions import SecureCookieSessionInterface
import os
from ibm_watsonx_ai.foundation_models import Model

final_mat=[]

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

parameters_3 = {
    "decoding_method": "greedy",
    "max_new_tokens": 8,
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

model_3 = Model(
   model_id = model_id,
   params = parameters_3,
   credentials = get_credentials(),
   project_id="b357c08e-c45b-4721-8e03-ffb9c3fa4924",
    #space_id=space_id
)

app = Flask(__name__)

app.secret_key = 'final_pi'


@app.route("/", methods=['POST', 'GET'])
def home():
  return render_template("home.html")

@app.route("/Project_management", methods=['POST', 'GET'])
def Project_management():
  return render_template("project_mang.html")

@app.route("/Project_idea_Evaluation", methods=['POST', 'GET'])
def Project_idea():
   prompt_input_1_n = """Analyze the following project idea and categorize it into very good, good, bad, and very bad depending on its impact on the environment. Provide a description of why the idea is classified as such. Also, classify each listed product into good or bad and suggest corresponding best alternatives.

  Example 1:
  Project Idea: Installing solar panels in a community to provide clean and renewable energy.
  Impact: Very Good
  Description: This project significantly reduces reliance on fossil fuels, decreases greenhouse gas emissions, and promotes the use of renewable energy. Solar energy is a sustainable source with minimal environmental impact once installed.
  Products:
  1. Solar Panels
     - Classification: Good
     - Alternative: Continued use of high-efficiency panels to reduce space and material usage.
  2. Lithium-ion Batteries
     - Classification: Good
     - Alternative: Solid-state batteries or other advanced storage technologies with lower environmental impact.
  3. Plastic Mounting Brackets
     - Classification: Bad
     - Alternative: Metal or recycled composite mounting brackets to reduce plastic waste.

  Example 2:
  Project Idea: Setting up a large-scale distribution network for plastic bottled water.
  Impact: Very Bad
  Description: This project increases plastic waste, contributes to pollution, and has a high carbon footprint due to transportation. It is detrimental to the environment due to the non-biodegradable nature of plastic and the emissions from distribution.
  Products:
  1. Plastic Water Bottles
     - Classification: Bad
     - Alternative: Refillable water bottles made from stainless steel or glass.
  2. Distribution Trucks
     - Classification: Bad
     - Alternative: Electric delivery vehicles or bicycles for local distribution to reduce emissions.
  3. Plastic Packaging
     - Classification: Bad
     - Alternative: Biodegradable or compostable packaging materials.

  Example 3:
  Project Idea: Creating urban green spaces and parks in a city.
  Impact: Very Good
  Description: Urban green spaces improve air quality, reduce urban heat islands, and enhance biodiversity. They provide recreational areas for the community and promote environmental sustainability.
  Products:
  1. Native Trees and Plants
     - Classification: Good
     - Alternative: N/A, native species are the best choice.
  2. Eco-friendly Benches
     - Classification: Good
     - Alternative: Benches made from recycled materials or sustainably sourced wood.
  3. Compost Bins
     - Classification: Good
     - Alternative: N/A, compost bins are essential for managing organic waste sustainably.

  Example 4:
  Project Idea: Constructing high-density housing units in an urban area.
  Impact: Good
  Description: High-density housing reduces urban sprawl and promotes efficient land use. However, the construction materials can have a significant environmental impact, which needs to be managed carefully.
  Products:
  1. Concrete
     - Classification: Bad
     - Alternative: Green concrete or other sustainable building materials.
  2. Steel
     - Classification: Bad
     - Alternative: Recycled steel or alternative materials with lower environmental impact.
  3. Energy-efficient Appliances
     - Classification: Good
     - Alternative: Continued innovation in energy-efficient technologies to reduce energy consumption.

  Example 6:
  Input: The project aims to plant thousands of trees in urban areas across the city. By creating green corridors and expanding green spaces, it will enhance urban biodiversity, provide shade, improve air quality, and reduce the urban heat island effect. Additionally, the project will engage local communities through educational programs about the benefits of trees.
  Output: Very good. This project will improve air quality, reduce urban heat islands, and increase biodiversity in cities. Planting trees also sequesters carbon, helping mitigate climate change.

  Example 7:
  Input: This initiative seeks to deploy solar-powered water purification units in rural and remote areas. These systems use renewable solar energy to purify contaminated water sources, providing clean drinking water to communities without access to safe water.
  Output: Very good. This project uses renewable solar energy to provide clean drinking water, reducing reliance on fossil fuels and decreasing waterborne diseases without emitting pollutants.

  Example 8:
  Input: The project involves replacing traditional lighting in public buildings with energy-efficient LED lights. This upgrade aims to reduce energy consumption and lower the buildings' carbon footprint.
  Output: Good. This project will reduce energy consumption and lower carbon emissions, though it does not address renewable energy sources.

  Example 9:
  Input: This project proposes installing green roofs on commercial buildings in the downtown area. Green roofs will help reduce stormwater runoff, provide insulation, and create green spaces in urban environments.
  Output: Good. Green roofs offer multiple environmental benefits, including reduced stormwater runoff and improved insulation, though their impact is limited to specific buildings.

  Example 10:
  Input: The project proposes constructing a new highway to alleviate traffic congestion in the city. The highway will cut through several natural habitats and require significant land clearing.
  Output: Bad. Constructing a new highway will destroy natural habitats, increase pollution, and encourage more car use, contributing negatively to the environment.

  Example 11:
  Input: This project aims to develop a large shopping mall in a suburban area, which will include vast parking spaces and attract heavy traffic. It promises economic growth and job creation.
  Output: Bad. Developing a large shopping mall in suburban areas increases urban sprawl, traffic congestion, and pollution, negatively impacting the environment.

  Example 12:
  Input: The project seeks to start oil drilling operations in a marine protected area, arguing that it will boost the local economy and energy independence. The drilling site is home to several endangered marine species.
  Output: Very bad. Oil drilling in a marine protected area endangers marine life, risks oil spills, and contributes to climate change, causing significant environmental harm.

  Example 13:
  Input: This project aims to establish a large-scale industrial mining operation in a pristine forest region rich in minerals. It promises significant economic benefits and job creation for the local community.
  Output: Very bad. Large-scale mining in a pristine forest leads to deforestation, habitat destruction, and pollution of water sources, with devastating environmental impacts.


  Instructions:
  1. Analyze the given below project idea.
  2. Classify the project's impact on the environment into very good, good, bad and very bad.
  3. Describe why the project is classified in that category.
  4. if and only if any products are listed analyze each product and classify them onto very good, good, bad and very bad. If and only if any products are bad or very bad suggest its beast alternatives and suggest why they are best and if the product is good or very good describe why they are so suitable for the sustainability.
  5. if and only if no products are listed suggest the best sustainable products that can be used in the project and give a brief describtion.

  Use the format provided in the examples to structure your response.

  """
   response=""
   if request.method == "POST" and 'f1' in request.form:
      user_input = request.form.get('user_input')
      if user_input:
        # Proceed with analysis
        prompt_input_1 = prompt_input_1_n
        user_input= str(user_input)
        prompt_input_1+='Input:\n'+user_input+'\n'+'Output: '
        response = "\n" + model_1.generate_text(prompt=prompt_input_1, guardrails=True)
        session['final_pi'] = response
        return render_template('project_idea.html', response=response)
   #if request.method == "POST" and 'f2' in request.form:
      
      
  
   return render_template("project_idea.html", response=None)

  
@app.route("/Material_choosing", methods=['POST', 'GET'])
def Material_choosing():
  prompt_input_2_n = """Analyze the given input material, object, or process and classify it as a good choice or a bad choice based on its sustainability outlook. 
  Examples:

  Input: Plastic used for making bottles
  Output: 
  1. BAD CHOICE.
  2. A better alternative is stainless steel bottles. Stainless steel bottles are better because they are durable, reusable, and do not leach harmful chemicals into the water. They also reduce plastic waste in landfills and oceans.

  Input: Styrofoam for packaging
  Output:
  1. BAD CHOICE.
  2. A better alternative is biodegradable packaging made from cornstarch. Cornstarch packaging is better because it breaks down naturally in the environment without leaving toxic residues, reducing pollution and waste.

  Input: Conventional Diesel Engines for cars
  Output: 
  1. BAD CHOICE.
  2. A good alternative is electric engines. Electric engines are better because they produce zero emissions, reducing air pollution and greenhouse gas emissions, contributing to cleaner air and combating climate change.

  Input: Synthetic Fertilizers instead of Organic fertilizers
  Output: 
  1. BAD CHOICE.
  2. A good alternative is compost or organic fertilizers. Organic fertilizers are better because they improve soil health, promote biodiversity, and do not cause chemical run-off that can harm waterways and aquatic life.

  Input: Single-Use Plastic Straws
  Output: 
  1. BAD CHOICE.
  2. A better alternative is reusable metal straws. Metal straws are better because they can be used repeatedly, reducing plastic waste and environmental pollution. They are also easy to clean and durable.

  Input: Bamboo for making furniture
  Output: 
  1. GOOD CHOICE.
  2. Bamboo is already a good choice. It is a highly sustainable material that grows rapidly without the need for pesticides or fertilizers. Bamboo is also biodegradable and has a lower environmental impact compared to traditional wood or plastic.

  Input: Recycled Paper
  Output: 
  1. GOOD CHOICE.
  2. Recycled paper is already a good choice. It reduces the need for virgin wood pulp, conserving trees and natural habitats. It also uses less energy and water during production and reduces landfill waste.

  Input: LED Lighting
  Output: 
  1. GOOD CHOICE.
  2. LED lighting is already a good choice. It is highly energy-efficient, using up to 80% less energy than traditional incandescent bulbs. LED lights also have a longer lifespan, reducing the need for frequent replacements and reducing waste.

  Input: Solar Panels
  Output: 
  1. GOOD CHOICE.
  2. Solar panels are already a good choice. They generate clean, renewable energy from the sun, reducing reliance on fossil fuels and decreasing greenhouse gas emissions. Solar panels also help in reducing electricity bills and promoting energy independence.

  Input: Electric Bicycles
  Output: 
  1. GOOD CHOICE.
  2. Electric bicycles are already a good choice. They provide an eco-friendly mode of transportation, reducing the reliance on cars and lowering carbon emissions. Electric bicycles also promote physical activity and can help alleviate traffic congestion.

  Input: Styrofoam container for ice cream
  Output: 
  1. BAD CHOICE.
  2. A better alternative is biodegradable containers made from plant-based materials. Plant-based containers are better because they break down naturally in the environment without leaving toxic residues, reducing pollution and waste.

  Instructions:
  1. Classify the given input material, object, or process as a good choice or a bad choice based on its sustainability outlook.
  2. If it is a bad choice, suggest a better alternative and explain why it is more sustainable.
  3. If it is a good choice, explain why it is sustainable.


  """
  prompt_input_3 = '''Extract the specific alternative product name from the given input text. The input text will contain an analysis of a material, object, or process, classified as either a good or bad choice based on sustainability. If it is a bad choice, an alternative product will be suggested. Extract only the specific name of the alternative product from the text.

   Examples 1:
   Input: BAD CHOICE. A better alternative is stainless steel bottles. Stainless steel bottles are better because they are durable, reusable, and do not leach harmful chemicals into the water. They also reduce plastic waste in landfills and oceans.
   Output: stainless steel bottles

   Examples 2:
   Input: BAD CHOICE. A better alternative is biodegradable packaging made from cornstarch. Cornstarch packaging is better because it breaks down naturally in the environment without leaving toxic residues, reducing pollution and waste.
   Output: cornstarch packaging

   Examples 3:
   Input: BAD CHOICE. A good alternative is electric engines. Electric engines are better because they produce zero emissions, reducing air pollution and greenhouse gas emissions, contributing to cleaner air and combating climate change.
   Output: electric engines

   Examples 4:
   Input: BAD CHOICE. A good alternative is compost or organic fertilizers. Organic fertilizers are better because they improve soil health, promote biodiversity, and do not cause chemical run-off that can harm waterways and aquatic life.
   Output: compost or organic fertilizers

   Examples 5:
   Input: BAD CHOICE. A better alternative is reusable metal straws. Metal straws are better because they can be used repeatedly, reducing plastic waste and environmental pollution. They are also easy to clean and durable.
   Output: reusable metal straws

   Examples 6:
   Input: GOOD CHOICE. Bamboo is already a good choice. It is a highly sustainable material that grows rapidly without the need for pesticides or fertilizers. Bamboo is also biodegradable and has a lower environmental impact compared to traditional wood or plastic.
   Output:

   Examples 7:
   Input: GOOD CHOICE. Recycled paper is already a good choice. It reduces the need for virgin wood pulp, conserving trees and natural habitats. It also uses less energy and water during production and reduces landfill waste.
   Output:

   Examples 8:
   Input: GOOD CHOICE. LED lighting is already a good choice. It is highly energy-efficient, using up to 80% less energy than traditional incandescent bulbs. LED lights also have a longer lifespan, reducing the need for frequent replacements and reducing waste.
   Output:

   Examples 9:
   Input: GOOD CHOICE. Solar panels are already a good choice. They generate clean, renewable energy from the sun, reducing reliance on fossil fuels and decreasing greenhouse gas emissions. Solar panels also help in reducing electricity bills and promoting energy independence.
   Output:

   Examples 10:
   Input: GOOD CHOICE. Electric bicycles are already a good choice. They provide an eco-friendly mode of transportation, reducing the reliance on cars and lowering carbon emissions. Electric bicycles also promote physical activity and can help alleviate traffic congestion.
   Output:

   Examples 11:
   Input: BAD CHOICE. A better alternative is biodegradable containers made from plant-based materials. Plant-based containers are better because they break down naturally in the environment without leaving toxic residues, reducing pollution and waste.
   Output: biodegradable containers made from plant-based materials

   Instructions:
   1. Read the given input text.
   2. If the text mentions a bad choice and suggests an alternative, extract the specific name of the alternative product.
   3. If the text mentions a good choice, leave the output blank.

   Use the format provided in the examples to structure your response.

   '''

  if request.method == "POST" :
    response=""
    user_input = request.form.get('user_input')
    if user_input:
      # Proceed with analysis
      prompt_input_2 = prompt_input_2_n
      user_input= str(user_input)
      prompt_input_2+='Input:\n'+user_input+'\n'+'Output: '
      response = model_1.generate_text(prompt=prompt_input_2, guardrails=True)
      prompt_input_5 = prompt_input_3 +'\n' + response+'\n'+'Output: '
      response_ne = model_3.generate_text(prompt=prompt_input_5, guardrails=True)
      return render_template('mat_cho.html', response=response, new_mat=response_ne)
  return render_template("mat_cho.html")

@app.route("/Credits", methods=['POST', 'GET'])
def Credits():
  return render_template("credits.html")

@app.route("/Project_summary", methods=['POST','GET'])
def Project_summary():
  final_pi = session.get('final_pi', 'Empty')
  return render_template("project_summ.html", final_pi=final_pi,final_mat=final_mat)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)