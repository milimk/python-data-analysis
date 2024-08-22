# %%
import csv
import matplotlib.pyplot as plt


def generate_user_dict_from_csv(filename):
  output = {}

  # Generate user dictionary from CSV file
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
      continent = line['Entity']
      year = line['Year']
      users = line['Number of Internet users']

      if continent not in output:
        output[continent] = {'Number of Internet users': [], 'Year': []}

      # Create data structure for each continent to be used in Plot
      output[continent]['Number of Internet users'].append(int(users))
      output[continent]['Year'].append(int(year))

  return output


def generate_plot_from_user_dict(user_dict):
  for continent in user_dict:
    # Data variables to create the Plot
    user = user_dict[continent]['Number of Internet users']
    year = user_dict[continent]['Year']

    plt.plot(year, user, label=continent, marker="o", alpha=0.5)

  plt.title("Internet Users per continent")
  plt.xlabel("Year")
  plt.ylabel("Internet Users (in billions)")
  plt.legend()

  plt.grid(True)
  plt.show()


filename = 'number-of-internet-users.csv'
user_per_continent = generate_user_dict_from_csv(filename)
generate_plot_from_user_dict(user_per_continent)

# %%
