import pandas as pd
import seaborn as sb

column_names = ["state",
          "acccount_length",
          "area_code",
          "phone_number",
          "international_plan",
          "voice_mail_plan",
          "number_vmail_messages",
          "total_day_minutes",
          "total_day_calls",
          "total_day_charge",
          "total_eve_minutes",
          "total_eve_calls",
          "total_eve_charge",
          "total_night_minutes",
          "total_night_calls",
          "total_night_charge",
          "total_intl_minutes",
          "total_intl_calls",
          "total_intl_charge",
          "number_customer_service_calls",
          "churned"]

continuousish_cols = ["acccount_length", "number_vmail_messages", "total_day_minutes", "total_day_calls", "total_day_charge",
                      "total_eve_minutes", "total_eve_calls", "total_eve_charge", "total_night_minutes", "total_night_calls",
                      "total_intl_minutes", "total_intl_calls", "total_intl_charge"]
                      
id_cols = ["area_code", "phone_number"]
categorical_cols = ["state", "international_plan", "voice_mail_plan"]

raw_data = pd.read_csv('data/churn.all', names=column_names)

#Make Plots
sb.distplot(raw_data['number_customer_service_calls'], kde=False)
plt.savefig('img/cust_service_calls_dist.png')

continuous_data = raw_data[["total_day_minutes", "total_day_calls", "churned"]]
sb.pairplot(continuous_data, hue="churned")
plt.savefig('img/related_data.png')

limited_cols = ["acccount_length", "number_vmail_messages", "number_customer_service_calls","total_day_calls",
                "total_night_calls", "total_eve_calls", "total_intl_calls", "churned"]
sb.pairplot(raw_data[limited_cols], hue="churned", palette='husl')
plt.savefig('img/pairwise_relations.png')

def make_box_plot(col_name):
  sb.boxplot(x="churned", y=col_name, data=raw_data)
  plt.savefig("img/boxplot/" + col_name + ".png")
  plt.clf()
  
def make_violin_plot(col_name):
  sb.violinplot(x="churned", y=col_name, data = raw_data)
  plt.savefig("img/violinplot/" +  col_name + ".png")
  plt.clf()

[make_box_plot(col) for col in continuousish_cols]
[make_violin_plot(col) for col in continuousish_cols]