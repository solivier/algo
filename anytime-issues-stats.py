from statistics import median

import gitlab
import datetime as dt

#be careful for issue count the project is number 10
gl = gitlab.Gitlab('https://anylab.anytime.tools/', private_token='dHhBkbmiQgTx5-k-3XnT')


project = gl.projects.get(152, lazy=True)

result = {}

all_time_to_resole_in_sec = []
all_open_tickets_per_month = 0

# issues = project.issues.list(all=True, labels=['Bug'])
#
#
# for issue in issues:
#     datetime_created_at = dt.datetime.strptime(issue.created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
#     created_at = datetime_created_at.strftime('%Y-%m')
#     closed_at = None
#     all_open_tickets_per_month += 1
#
#     if issue.closed_at is not None:
#         datetime_closed_at = dt.datetime.strptime(issue.closed_at, '%Y-%m-%dT%H:%M:%S.%fZ')
#         closed_at = datetime_closed_at.strftime('%Y-%m')
#         all_time_to_resole_in_sec.append((datetime_created_at - datetime_closed_at).seconds)
#
#     if created_at in result:
#         result[created_at]['open'] += 1
#         if closed_at is not None:
#             result[created_at]['closed'] += 1
#
#         result[created_at]['ratio'] = result[created_at]['closed'] - result[created_at]['open']
#     else:
#         result[created_at] = {'open': 0, 'closed': 0, 'ratio': 0}
#         result[created_at]['open'] = 1
#
# print(result)
# print('Average time to resolve bug (hours): ' + str(round(sum(all_time_to_resole_in_sec)/len(issues)/60/60)))
# print('Median time to resolve bug (hours): ' + str(round(median(all_time_to_resole_in_sec)/60/60)))
# print('Average bug tickets open per month: ' + str(round(all_open_tickets_per_month/len(result))))
#
# releases = project.releases
# releases_stats = {}
# for release in releases.list(all=True):
#     if release.name[:7] not in releases_stats:
#         releases_stats[release.name[:7]] = 0
#     releases_stats[release.name[:7]] += 1
#
# print('Average release(s) per months: ' + str(round(sum(releases_stats.values())/len(releases_stats))))
# print('Average release(s) per weeks: ' + str(round(sum(releases_stats.values())/len(releases_stats)/4.345)))
# print('Average release(s) per days: ' + str(round(sum(releases_stats.values())/len(releases_stats)/4.345/7)))
#
#
# # get average ci time
#
# pipelines = project.pipelines.list(all=True, status='success')
#
# avg = 0
# avg_per_months = {}
#
# for i in pipelines:
#     avg += project.pipelines.get(i.id).duration
#     month = dt.datetime.strptime(i.created_at, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m')
#
#     if month in avg_per_months:
#         avg_per_months[month] ={'sum': avg_per_months[month]['sum'] + project.pipelines.get(i.id).duration, 'nbr': avg_per_months[month]['nbr'] + 1, 'avg': (avg_per_months[month]['sum']/avg_per_months[month]['nbr'] + 1)/60}
#     else:
#         avg_per_months[month] = {'sum': project.pipelines.get(i.id).duration, 'nbr': 1, 'avg': 0}
#
#
# print(avg_per_months)
# print('Average Ci time in minute: ' + str(round((avg/len(pipelines))/60)))

mr = project.mergerequests.list(all=True, state='merged')

print(len(mr))

for i in mr:
    print(i)
    print(i.diffs.list(all=True)[0])
    break
