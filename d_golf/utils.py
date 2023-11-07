from .models import FiveScores


def initial(gname):
	FiveScores.objects.create(
			name_id= gname,

			score1= 0,
			score2=0,
			score3=0,
			score4=0,
			score5=0,
			total_score=0)

	
def update(gid, score, round_no):
	#FiveScores.objects.filter(name_id = gid).update(score1 = score)

	obj = FiveScores.objects.get(name=gid)

	# Add new score to relevent round
	if round_no == 1:
		obj.score1 = score
	if round_no == 2:
		obj.score2 = score
	if round_no == 3:
		obj.score3 = score
	if round_no == 4:
		obj.score4 = score
	if round_no == 5:
		obj.score5 = score

		# Create a list of scores for this golfer 
	score_list = []
	score_list.append(obj.score1)
	score_list.append(obj.score2)
	score_list.append(obj.score3)
	score_list.append(obj.score4)
	score_list.append(obj.score5)

	 # find largest
	largest = max(score_list)
	# remove from list
	score_list.remove(largest)
	# second largest
	largest2 = max(score_list)
	# remove from list
	score_list.remove(largest2)
	# third largest
	largest3 = max(score_list)
    
	obj.total_score = (largest+largest2+largest3)
    	
	# Write the scores and total score to the database
	obj.save()	


