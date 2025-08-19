{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO5Q8pgbgWjUopfJRZ2Y+NV",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Niranjana-08/AI-Ascent/blob/main/keywords.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "MEGA_KEYWORDS = {\n",
        "    \"Technology\": {\n",
        "        \"Core Software & Web Development\": 'software engineer software developer web developer full stack developer frontend developer backend developer application developer programmer coding api developer mobile developer ios developer android developer frontend engineer backend engineer app developer game developer software architect',\n",
        "        \"Data, AI & Analytics\": 'data scientist data analyst machine learning engineer ai engineer ai researcher deep learning engineer nlp engineer computer vision engineer data engineer business intelligence analyst bi developer analytics engineer ml engineer mlops engineer research scientist data science manager',\n",
        "        \"Infrastructure, Cloud & Operations\": 'devops engineer cloud engineer site reliability engineer sre infrastructure engineer platform engineer automation engineer aws azure gcp kubernetes cloud architect network engineer systems engineer',\n",
        "        \"Cybersecurity, QA & Specialized Tech\": 'cybersecurity specialist security engineer information security analyst penetration tester cyber analyst database administrator dba qa engineer test engineer automation tester',\n",
        "        \"Management & Product Leadership\": 'product manager technical lead solutions architect engineering manager technical program manager head of engineering cto'\n",
        "    },\n",
        "    \"Automotive\": {\n",
        "        \"Core Engineering & Systems\": 'automotive engineer powertrain chassis drivetrain mechanical engineer electrical engineer systems engineer validation engineer testing',\n",
        "        \"Electric & Autonomous Vehicles (EV/AV)\": 'electric vehicle ev battery systems bms autonomous adas advanced driver-assistance robotics lidar radar computer vision',\n",
        "        \"Software & Electronics\": 'embedded software firmware infotainment telematics ecu v2x connected vehicle automotive software'\n",
        "    },\n",
        "    \"Consulting & Strategy\": {\n",
        "        \"Core & Management Strategy\": 'consultant strategy advisory management consultant strategic planning business transformation associate consultant principal consultant senior consultant consulting analyst strategy analyst strategy associate engagement manager corporate strategy growth strategy business design enterprise transformation',\n",
        "        \"Major Consulting Firms\": 'mckinsey bcg bain deloitte monitor deloitte pwc ey kpmg accenture zinnov roland berger lek consulting oliver wyman',\n",
        "        \"Specialized & Domain-Specific Advisory\": 'technology consultant it advisory digital transformation financial advisory m&a advisory transaction services deals advisory operations consultant risk consultant human capital advisory organizational transformation innovation consultant business consultant strategy consulting management consulting'\n",
        "    },\n",
        "    \"Finance\": {\n",
        "        \"Corporate Finance & Financial Analysis\": 'financial analyst senior financial analyst business analyst finance associate finance manager finance director fp&a financial planning budgeting and forecasting financial reporting corporate finance controller treasury treasury analyst cost analyst financial modeling',\n",
        "        \"Accounting, Assurance & Tax\": 'accountant accounting analyst public accountant forensic accountant auditor internal auditor assurance tax associate tax analyst tax consultant tax cpa gaap ifrs',\n",
        "        \"Investment & Capital Markets\": 'investment banking investment analyst private equity venture capital equity research analyst sell-side analyst buy-side analyst hedge fund fixed income analyst quantitative analyst quant quantitative trader algo trader trading strategist trader portfolio management fund analyst asset management credit analyst risk analyst risk management wealth management derivatives analyst'\n",
        "    },\n",
        "    \"Marketing\": {\n",
        "        \"Digital & Performance Marketing\": 'digital marketing performance marketing growth marketer growth marketing manager seo search engine optimization sem ppc paid search marketing automation email marketing retargeting programmatic advertising media buyer google ads facebook ads campaign manager paid media specialist',\n",
        "        \"Content, Creative & Brand\": 'content creator content marketing copywriter ai copywriter brand manager brand strategist social media manager community manager influencer marketing manager public relations communications specialist creative director video content producer multimedia producer ugc creator storyteller scriptwriter',\n",
        "        \"Marketing Strategy & Analytics\": 'marketing manager marketing analyst product marketing manager product marketing market researcher customer insights analyst crm manager growth strategist demand generation manager performance analyst consumer behavior analyst customer experience analyst segmentation analyst marketing operations marketing data scientist marketing coordinator marketing associate marketing specialist sales manager sales director head of sales account executive'\n",
        "    },\n",
        "    \"Healthcare (Research & Admin)\": {\n",
        "        \"Research & Biotechnology\": 'bioinformatics research scientist computational biology biostatistician biotechnology genomics drug discovery clinical trial clinical data management r&d scientist',\n",
        "        \"Administration & Informatics\": 'clinical informatics healthcare analyst health informatics healthcare administration medical records health information management healthcare economics heor',\n",
        "        \"Clinical & Patient Care\": 'physician assistant registered nurse rn therapist counselor clinician clinical specialist patient care medical assistant behavior analyst acupuncturist practitioner healthcare provider physician doctor'\n",
        "    },\n",
        "\n",
        "    \"Human Resources\": {\n",
        "        \"Talent Acquisition & Recruiting\": 'recruiter technical recruiter talent acquisition sourcing recruiting coordinator campus recruiting executive search recruitment marketing candidate experience',\n",
        "        \"Core HR & Business Partnership\": 'human resources hr generalist hr manager senior hr manager director of hr hr business partner hrbp employee relations specialist employee engagement specialist people operations labor relations specialist hr compliance officer diversity and inclusion manager',\n",
        "        \"Specialized HR & Analytics\": 'hr analyst people analytics people data scientist compensation and benefits hris analyst hr technology workforce planning talent management learning and development l&d organizational development',\n",
        "    },\n",
        "    \"Supply Chain & Logistics\": {\n",
        "        \"Planning & Analytics\": 'supply chain analyst supply chain planner demand planner forecasting analyst inventory analyst inventory management supply planner materials planner logistics analyst network planner',\n",
        "        \"Logistics & Operations\": 'logistics coordinator logistics specialist warehouse manager distribution center manager operations manager transportation manager distribution manager fleet management last mile logistics route planner freight specialist shipping coordinator fulfillment specialist warehouse operations',\n",
        "        \"Procurement & Sourcing\": 'procurement procurement analyst sourcing manager strategic sourcing specialist purchasing manager category manager buyer supplier relationship manager contract manager'\n",
        "    },\n",
        "    \"Legal\": {\n",
        "        \"Practicing Roles\": 'lawyer attorney counsel legal counsel associate attorney litigation corporate counsel',\n",
        "        \"Support & Paralegal\": 'paralegal legal assistant legal secretary clerk',\n",
        "        \"Specialized & Tech\": 'legal tech e-discovery contract manager compliance officer regulatory affairs'\n",
        "    },\n",
        "    \"Design\": {\n",
        "        \"Digital Product & UX/UI\": 'product designer ux designer ui designer user experience user interface interaction designer ux researcher user researcher service designer design technologist',\n",
        "        \"Visual & Graphic Design\": 'graphic designer visual designer motion designer illustrator art director brand designer presentation designer 2d animator 3d designer',\n",
        "        \"Specialized Design Roles\": 'design system creative director design ops exhibition designer environmental designer design lead head of design design system manager'\n",
        "    },\n",
        "    \"Education & EdTech\": {\n",
        "        \"Instructional & Curriculum Design\": 'instructional designer curriculum developer learning design learning experience curriculum specialist e-learning developer',\n",
        "        \"EdTech Product & Technology\": 'edtech education technology learning technologist product manager - edtech',\n",
        "        \"Academic & Training Roles\": 'education academic trainer corporate trainer faculty teacher'\n",
        "    },\n",
        "    \"Media & Journalism\": {\n",
        "        \"Content Creation & Journalism\": 'journalist editor writer reporter copy editor content strategist columnist correspondent',\n",
        "        \"Production & Broadcasting\": 'producer video editor broadcast publisher media production',\n",
        "        \"Management & Analysis\": 'media planner managing editor editor-in-chief media analyst'\n",
        "    }\n",
        "}"
      ],
      "metadata": {
        "id": "aoyIfKSKlCBo"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}