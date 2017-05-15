# def addup(df, item):
#     sample = []
#     for i in range(int((len(df[item])-1)/7)):
#         sum=0
#         for j in range(7):
#             sum += int(df['servings'][i*7+j])*int(df[item][i*7+j])
#         sample.append(sum)
#     return sample
#
# protein = addup(new_df, 'protein')
# cals = addup(new_df,'cals')
# fat = addup(new_df,'fat')
# carbs =addup(new_df,'carbs')
#
# working_df = pandas.DataFrame(
#     {'protein':protein,
#      'cals':cals,
#      'fat':fat,
#      'carbs':carbs,
#      'change':change
# })
# print(working_df)
