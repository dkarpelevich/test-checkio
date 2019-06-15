import sendgrid
from SendGrid import API_KEY
import json

sg = sendgrid.SendGridAPIClient(api_key=API_KEY)

def best_country(str_date):
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })
    data = response.body
#     data = [{
#     'date': '2016-01-01',
#     'stats': [
#         {
#          'type': 'country',
#          'name': 'AT',
#          'metrics': {'clicks': 1, 'opens': 1, 'unique_clicks': 1, 'unique_opens': 1}
#         },
#         {
#          'type': 'country',
#          'name': 'AU',
#          'metrics': {'clicks': 0, 'opens': 31, 'unique_clicks': 0, 'unique_opens': 22}
#         }
#     ]
# }]
    print(data)
    if not response.to_dict:
        print('AU')
    #max_data = max(data[0]['stats'], key=lambda a: a['metrics']['unique_clicks'])
    #print(max_data['name'])


if __name__ == '__main__':
    best_country('2019-06-09')