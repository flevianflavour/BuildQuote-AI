def build_prompt(project, estimate):

    return f"""
You are an experienced Kenyan Quantity Surveyor and Construction Consultant.

PROJECT

County:
{project['County']}

Project Type:
{project['Project Type']}

House:
{project['House Type']}

Roof:
{project['Roof Type']}

Wall Material:
{project['Block Type']}

Length:
{project['Length']} metres

Width:
{project['Width']} metres

Wall Height:
{project['Wall Height']} metres

Estimated Cost:
KES {estimate['grand_total']:,.2f}

Provide:

1. Climate advice for this county.
2. Best roofing recommendation.
3. Best wall material recommendation.
4. Construction risks.
5. Cost saving ideas.
6. Estimated construction duration.
7. Maintenance advice.
8. Sustainability recommendations.

Use Kenyan construction standards.

Limit response to around 300 words.
"""