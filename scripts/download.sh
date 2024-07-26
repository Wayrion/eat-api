# get from entities.py
canteen_id='414'
month='08'
year='2024'

# url needs two digits
for day in {01..31}; do
    wget "https://www.studierendenwerk-muenchen-oberbayern.de/mensa/speiseplan/speiseplan_${year}-${month}-${day}_${canteen_id}_-de.html" -O "${year}-${month}-${day}.html"
done
