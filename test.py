
import json
import pandas as pd
import sys

#metrics_df = pd.DataFrame(columns=['GUID', 'MAE', 'VAL LOSS', 'DROPOUT', 'PREV PERIODS'])
rows_list = []

with open('results.json', 'r') as f:
   json_obj = json.load(f)
  
   for m in json_obj:
      if len (m['metrics']) > 0:
          for l in m['metrics'][-2:]:
             if l['phase'] == 'test':
                last_metric = l
                break
          for h in m['hyper_parameters']:
             if h['name'] == 'dropout_rate':
                dropout_rate = h['double_value']
             else:
                prev_periods = h['int_value']
          for v in last_metric['values']:
             if v['name'] == 'val_loss':
                val_loss = v['value']
             else :
                val_mae = v['value']
          one_row = [m['training_guid'],  last_metric['phase'], val_mae, val_loss, dropout_rate,  prev_periods]
          rows_list.append(one_row)
            
   metrics_df = pd.DataFrame(rows_list,columns=['GUID', 'PHASE', 'MAE', 'VAL LOSS', 'DROPOUT', 'PREV PERIODS'])
   metrics_df.to_csv(sys.stdout)
   best_run_df = metrics_df.nsmallest(1, 'MAE')
   print('Best run')
   best_run_df.to_csv(sys.stdout)
   