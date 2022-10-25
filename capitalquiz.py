import tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import title
import PIL 
from PIL import ImageTk, Image
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
from PIL import Image,ImageTk

cocap = []
cocapAS = []
cocapEU = []
cocapAF = []
cocapNA = []
cocapSA = []
cocapOCE = []
flag = 0
def crList():
    global cocap,cocapAS,cocapEU,cocapAF ,cocapNA ,cocapSA ,cocapOCE 
    countries = [
    {'timezones': ['Europe/Andorra'], 'code': 'AD', 'continent': 'Europe', 'name': 'Andorra', 'capital': 'Andorra la Vella'},
    {'timezones': ['Asia/Kabul'], 'code': 'AF', 'continent': 'Asia', 'name': 'Afghanistan', 'capital': 'Kabul'},
    {'timezones': ['America/Antigua'], 'code': 'AG', 'continent': 'North America', 'name': 'Antigua and Barbuda', 'capital': "St. John's"},
    {'timezones': ['Europe/Tirane'], 'code': 'AL', 'continent': 'Europe', 'name': 'Albania', 'capital': 'Tirana'},
    {'timezones': ['Asia/Yerevan'], 'code': 'AM', 'continent': 'Asia', 'name': 'Armenia', 'capital': 'Yerevan'},
    {'timezones': ['Africa/Luanda'], 'code': 'AO', 'continent': 'Africa', 'name': 'Angola', 'capital': 'Luanda'},
    {'timezones': ['America/Argentina/Buenos_Aires', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/Tucuman', 'America/Argentina/Catamarca', 'America/Argentina/La_Rioja', 'America/Argentina/San_Juan', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Ushuaia'], 'code': 'AR', 'continent': 'South America', 'name': 'Argentina', 'capital': 'Buenos Aires'},
    {'timezones': ['Europe/Vienna'], 'code': 'AT', 'continent': 'Europe', 'name': 'Austria', 'capital': 'Vienna'},
    {'timezones': ['Australia/Lord_Howe', 'Australia/Hobart', 'Australia/Currie', 'Australia/Melbourne', 'Australia/Sydney', 'Australia/Broken_Hill', 'Australia/Brisbane', 'Australia/Lindeman', 'Australia/Adelaide', 'Australia/Darwin', 'Australia/Perth'], 'code': 'AU', 'continent': 'Oceania', 'name': 'Australia', 'capital': 'Canberra'},
    {'timezones': ['Asia/Baku'], 'code': 'AZ', 'continent': 'Asia', 'name': 'Azerbaijan', 'capital': 'Baku'},
    {'timezones': ['America/Barbados'], 'code': 'BB', 'continent': 'North America', 'name': 'Barbados', 'capital': 'Bridgetown'},
    {'timezones': ['Asia/Dhaka'], 'code': 'BD', 'continent': 'Asia', 'name': 'Bangladesh', 'capital': 'Dhaka'},
    {'timezones': ['Europe/Brussels'], 'code': 'BE', 'continent': 'Europe', 'name': 'Belgium', 'capital': 'Brussels'},
    {'timezones': ['Africa/Ouagadougou'], 'code': 'BF', 'continent': 'Africa', 'name': 'Burkina Faso', 'capital': 'Ouagadougou'},
    {'timezones': ['Europe/Sofia'], 'code': 'BG', 'continent': 'Europe', 'name': 'Bulgaria', 'capital': 'Sofia'},
    {'timezones': ['Asia/Bahrain'], 'code': 'BH', 'continent': 'Asia', 'name': 'Bahrain', 'capital': 'Manama'},
    {'timezones': ['Africa/Bujumbura'], 'code': 'BI', 'continent': 'Africa', 'name': 'Burundi', 'capital': 'Bujumbura'},
    {'timezones': ['Africa/Porto-Novo'], 'code': 'BJ', 'continent': 'Africa', 'name': 'Benin', 'capital': 'Porto-Novo'},
    {'timezones': ['Asia/Brunei'], 'code': 'BN', 'continent': 'Asia', 'name': 'Brunei Darussalam', 'capital': 'Bandar Seri Begawan'},
    {'timezones': ['America/La_Paz'], 'code': 'BO', 'continent': 'South America', 'name': 'Bolivia', 'capital': 'Sucre'},
    {'timezones': ['America/Noronha', 'America/Belem', 'America/Fortaleza', 'America/Recife', 'America/Araguaina', 'America/Maceio', 'America/Bahia', 'America/Sao_Paulo', 'America/Campo_Grande', 'America/Cuiaba', 'America/Porto_Velho', 'America/Boa_Vista', 'America/Manaus', 'America/Eirunepe', 'America/Rio_Branco'], 'code': 'BR', 'continent': 'South America', 'name': 'Brazil', 'capital': 'Brasilia'},
    {'timezones': ['America/Nassau'], 'code': 'BS', 'continent': 'North America', 'name': 'Bahamas', 'capital': 'Nassau'},
    {'timezones': ['Asia/Thimphu'], 'code': 'BT', 'continent': 'Asia', 'name': 'Bhutan', 'capital': 'Thimphu'},
    {'timezones': ['Africa/Gaborone'], 'code': 'BW', 'continent': 'Africa', 'name': 'Botswana', 'capital': 'Gaborone'},
    {'timezones': ['Europe/Minsk'], 'code': 'BY', 'continent': 'Europe', 'name': 'Belarus', 'capital': 'Minsk'},
    {'timezones': ['America/Belize'], 'code': 'BZ', 'continent': 'North America', 'name': 'Belize', 'capital': 'Belmopan'},
    {'timezones': ['America/St_Johns', 'America/Halifax', 'America/Glace_Bay', 'America/Moncton', 'America/Goose_Bay', 'America/Blanc-Sablon', 'America/Montreal', 'America/Toronto', 'America/Nipigon', 'America/Thunder_Bay', 'America/Pangnirtung', 'America/Iqaluit', 'America/Atikokan', 'America/Rankin_Inlet', 'America/Winnipeg', 'America/Rainy_River', 'America/Cambridge_Bay', 'America/Regina', 'America/Swift_Current', 'America/Edmonton', 'America/Yellowknife', 'America/Inuvik', 'America/Dawson_Creek', 'America/Vancouver', 'America/Whitehorse', 'America/Dawson'], 'code': 'CA', 'continent': 'North America', 'name': 'Canada', 'capital': 'Ottawa'},
    {'timezones': ['Africa/Kinshasa', 'Africa/Lubumbashi'], 'code': 'CD', 'continent': 'Africa', 'name': 'Democratic Republic of the Congo', 'capital': 'Kinshasa'},
    {'timezones': ['Africa/Brazzaville'], 'code': 'CG', 'continent': 'Africa', 'name': 'Republic of the Congo', 'capital': 'Brazzaville'},
    {'timezones': ['Africa/Abidjan'], 'code': 'CI', 'continent': 'Africa', 'name': "Cote d'Ivoire", 'capital': 'Yamoussoukro'},
    {'timezones': ['America/Santiago', 'Pacific/Easter'], 'code': 'CL', 'continent': 'South America', 'name': 'Chile', 'capital': 'Santiago'},
    {'timezones': ['Africa/Douala'], 'code': 'CM', 'continent': 'Africa', 'name': 'Cameroon', 'capital': 'Yaounde'},
    {'timezones': ['Asia/Shanghai', 'Asia/Harbin', 'Asia/Chongqing', 'Asia/Urumqi', 'Asia/Kashgar'], 'code': 'CN', 'continent': 'Asia', 'name': "People's Republic of China", 'capital': 'Beijing'},
    {'timezones': ['America/Bogota'], 'code': 'CO', 'continent': 'South America', 'name': 'Colombia', 'capital': 'Bogota'},
    {'timezones': ['America/Costa_Rica'], 'code': 'CR', 'continent': 'North America', 'name': 'Costa Rica', 'capital': 'San Jose'},
    {'timezones': ['America/Havana'], 'code': 'CU', 'continent': 'North America', 'name': 'Cuba', 'capital': 'Havana'},
    {'timezones': ['Atlantic/Cape_Verde'], 'code': 'CV', 'continent': 'Africa', 'name': 'Cape Verde', 'capital': 'Praia'},
    {'timezones': ['Asia/Nicosia'], 'code': 'CY', 'continent': 'Asia', 'name': 'Cyprus', 'capital': 'Nicosia'},
    {'timezones': ['Europe/Prague'], 'code': 'CZ', 'continent': 'Europe', 'name': 'Czech Republic', 'capital': 'Prague'},
    {'timezones': ['Europe/Berlin'], 'code': 'DE', 'continent': 'Europe', 'name': 'Germany', 'capital': 'Berlin'},
    {'timezones': ['Africa/Djibouti'], 'code': 'DJ', 'continent': 'Africa', 'name': 'Djibouti', 'capital': 'Djibouti City'},
    {'timezones': ['Europe/Copenhagen'], 'code': 'DK', 'continent': 'Europe', 'name': 'Denmark', 'capital': 'Copenhagen'},
    {'timezones': ['America/Dominica'], 'code': 'DM', 'continent': 'North America', 'name': 'Dominica', 'capital': 'Roseau'},
    {'timezones': ['America/Santo_Domingo'], 'code': 'DO', 'continent': 'North America', 'name': 'Dominican Republic', 'capital': 'Santo Domingo'},
    {'timezones': ['America/Guayaquil', 'Pacific/Galapagos'], 'code': 'EC', 'continent': 'South America', 'name': 'Ecuador', 'capital': 'Quito'},
    {'timezones': ['Europe/Tallinn'], 'code': 'EE', 'continent': 'Europe', 'name': 'Estonia', 'capital': 'Tallinn'},
    {'timezones': ['Africa/Cairo'], 'code': 'EG', 'continent': 'Africa', 'name': 'Egypt', 'capital': 'Cairo'},
    {'timezones': ['Africa/Asmera'], 'code': 'ER', 'continent': 'Africa', 'name': 'Eritrea', 'capital': 'Asmara'},
    {'timezones': ['Africa/Addis_Ababa'], 'code': 'ET', 'continent': 'Africa', 'name': 'Ethiopia', 'capital': 'Addis Ababa'},
    {'timezones': ['Europe/Helsinki'], 'code': 'FI', 'continent': 'Europe', 'name': 'Finland', 'capital': 'Helsinki'},
    {'timezones': ['Pacific/Fiji'], 'code': 'FJ', 'continent': 'Oceania', 'name': 'Fiji', 'capital': 'Suva'},
    {'timezones': ['Europe/Paris'], 'code': 'FR', 'continent': 'Europe', 'name': 'France', 'capital': 'Paris'},
    {'timezones': ['Africa/Libreville'], 'code': 'GA', 'continent': 'Africa', 'name': 'Gabon', 'capital': 'Libreville'},
    {'timezones': ['Asia/Tbilisi'], 'code': 'GE', 'continent': 'Asia', 'name': 'Georgia', 'capital': 'Tbilisi'},
    {'timezones': ['Africa/Accra'], 'code': 'GH', 'continent': 'Africa', 'name': 'Ghana', 'capital': 'Accra'},
    {'timezones': ['Africa/Banjul'], 'code': 'GM', 'continent': 'Africa', 'name': 'The Gambia', 'capital': 'Banjul'},
    {'timezones': ['Africa/Conakry'], 'code': 'GN', 'continent': 'Africa', 'name': 'Guinea', 'capital': 'Conakry'},
    {'timezones': ['Europe/Athens'], 'code': 'GR', 'continent': 'Europe', 'name': 'Greece', 'capital': 'Athens'},
    {'timezones': ['America/Guatemala'], 'code': 'GT', 'continent': 'North America', 'name': 'Guatemala', 'capital': 'Guatemala City'},
    {'timezones': ['America/Guatemala'], 'code': 'GT', 'continent': 'North America', 'name': 'Haiti', 'capital': 'Port-au-Prince'},
    {'timezones': ['Africa/Bissau'], 'code': 'GW', 'continent': 'Africa', 'name': 'Guinea-Bissau', 'capital': 'Bissau'},
    {'timezones': ['America/Guyana'], 'code': 'GY', 'continent': 'South America', 'name': 'Guyana', 'capital': 'Georgetown'},
    {'timezones': ['America/Tegucigalpa'], 'code': 'HN', 'continent': 'North America', 'name': 'Honduras', 'capital': 'Tegucigalpa'},
    {'timezones': ['Europe/Budapest'], 'code': 'HU', 'continent': 'Europe', 'name': 'Hungary', 'capital': 'Budapest'},
    {'timezones': ['Asia/Jakarta', 'Asia/Pontianak', 'Asia/Makassar', 'Asia/Jayapura'], 'code': 'ID', 'continent': 'Asia', 'name': 'Indonesia', 'capital': 'Jakarta'},
    {'timezones': ['Europe/Dublin'], 'code': 'IE', 'continent': 'Europe', 'name': 'Republic of Ireland', 'capital': 'Dublin'},
    {'timezones': ['Asia/Jerusalem'], 'code': 'IL', 'continent': 'Asia', 'name': 'Israel', 'capital': 'Jerusalem'},
    {'timezones': ['Asia/Calcutta'], 'code': 'IN', 'continent': 'Asia', 'name': 'India', 'capital': 'New Delhi'},
    {'timezones': ['Asia/Baghdad'], 'code': 'IQ', 'continent': 'Asia', 'name': 'Iraq', 'capital': 'Baghdad'},
    {'timezones': ['Asia/Tehran'], 'code': 'IR', 'continent': 'Asia', 'name': 'Iran', 'capital': 'Tehran'},
    {'timezones': ['Atlantic/Reykjavik'], 'code': 'IS', 'continent': 'Europe', 'name': 'Iceland', 'capital': 'Reykjavik'},
    {'timezones': ['Europe/Rome'], 'code': 'IT', 'continent': 'Europe', 'name': 'Italy', 'capital': 'Rome'},
    {'timezones': ['America/Jamaica'], 'code': 'JM', 'continent': 'North America', 'name': 'Jamaica', 'capital': 'Kingston'},
    {'timezones': ['Asia/Amman'], 'code': 'JO', 'continent': 'Asia', 'name': 'Jordan', 'capital': 'Amman'},
    {'timezones': ['Asia/Tokyo'], 'code': 'JP', 'continent': 'Asia', 'name': 'Japan', 'capital': 'Tokyo'},
    {'timezones': ['Africa/Nairobi'], 'code': 'KE', 'continent': 'Africa', 'name': 'Kenya', 'capital': 'Nairobi'},
    {'timezones': ['Asia/Bishkek'], 'code': 'KG', 'continent': 'Asia', 'name': 'Kyrgyzstan', 'capital': 'Bishkek'},
    {'timezones': ['Pacific/Tarawa', 'Pacific/Enderbury', 'Pacific/Kiritimati'], 'code': 'KI', 'continent': 'Oceania', 'name': 'Kiribati', 'capital': 'Tarawa'},
    {'timezones': ['Asia/Pyongyang'], 'code': 'KP', 'continent': 'Asia', 'name': 'North Korea', 'capital': 'Pyongyang'},
    {'timezones': ['Asia/Seoul'], 'code': 'KR', 'continent': 'Asia', 'name': 'South Korea', 'capital': 'Seoul'},
    {'timezones': ['Asia/Kuwait'], 'code': 'KW', 'continent': 'Asia', 'name': 'Kuwait', 'capital': 'Kuwait City'},
    {'timezones': ['Asia/Beirut'], 'code': 'LB', 'continent': 'Asia', 'name': 'Lebanon', 'capital': 'Beirut'},
    {'timezones': ['Europe/Vaduz'], 'code': 'LI', 'continent': 'Europe', 'name': 'Liechtenstein', 'capital': 'Vaduz'},
    {'timezones': ['Africa/Monrovia'], 'code': 'LR', 'continent': 'Africa', 'name': 'Liberia', 'capital': 'Monrovia'},
    {'timezones': ['Africa/Maseru'], 'code': 'LS', 'continent': 'Africa', 'name': 'Lesotho', 'capital': 'Maseru'},
    {'timezones': ['Europe/Vilnius'], 'code': 'LT', 'continent': 'Europe', 'name': 'Lithuania', 'capital': 'Vilnius'},
    {'timezones': ['Europe/Luxembourg'], 'code': 'LU', 'continent': 'Europe', 'name': 'Luxembourg', 'capital': 'Luxembourg City'},
    {'timezones': ['Europe/Riga'], 'code': 'LV', 'continent': 'Europe', 'name': 'Latvia', 'capital': 'Riga'},
    {'timezones': ['Africa/Tripoli'], 'code': 'LY', 'continent': 'Africa', 'name': 'Libya', 'capital': 'Tripoli'},
    {'timezones': ['Indian/Antananarivo'], 'code': 'MG', 'continent': 'Africa', 'name': 'Madagascar', 'capital': 'Antananarivo'},
    {'timezones': ['Pacific/Majuro', 'Pacific/Kwajalein'], 'code': 'MH', 'continent': 'Oceania', 'name': 'Marshall Islands', 'capital': 'Majuro'},
    {'timezones': ['Europe/Skopje'], 'code': 'MK', 'continent': 'Europe', 'name': 'Macedonia', 'capital': 'Skopje'},
    {'timezones': ['Africa/Bamako'], 'code': 'ML', 'continent': 'Africa', 'name': 'Mali', 'capital': 'Bamako'},
    {'timezones': ['Asia/Rangoon'], 'code': 'MM', 'continent': 'Asia', 'name': 'Myanmar', 'capital': 'Naypyidaw'},
    {'timezones': ['Asia/Ulaanbaatar', 'Asia/Hovd', 'Asia/Choibalsan'], 'code': 'MN', 'continent': 'Asia', 'name': 'Mongolia', 'capital': 'Ulaanbaatar'},
    {'timezones': ['Africa/Nouakchott'], 'code': 'MR', 'continent': 'Africa', 'name': 'Mauritania', 'capital': 'Nouakchott'},
    {'timezones': ['Europe/Malta'], 'code': 'MT', 'continent': 'Europe', 'name': 'Malta', 'capital': 'Valletta'},
    {'timezones': ['Indian/Mauritius'], 'code': 'MU', 'continent': 'Africa', 'name': 'Mauritius', 'capital': 'Port Louis'},
    {'timezones': ['Indian/Maldives'], 'code': 'MV', 'continent': 'Asia', 'name': 'Maldives', 'capital': 'Male'},
    {'timezones': ['Africa/Blantyre'], 'code': 'MW', 'continent': 'Africa', 'name': 'Malawi', 'capital': 'Lilongwe'},
    {'timezones': ['America/Mexico_City', 'America/Cancun', 'America/Merida', 'America/Monterrey', 'America/Mazatlan', 'America/Chihuahua', 'America/Hermosillo', 'America/Tijuana'], 'code': 'MX', 'continent': 'North America', 'name': 'Mexico', 'capital': 'Mexico City'},
    {'timezones': ['Asia/Kuala_Lumpur', 'Asia/Kuching'], 'code': 'MY', 'continent': 'Asia', 'name': 'Malaysia', 'capital': 'Kuala Lumpur'},
    {'timezones': ['Africa/Maputo'], 'code': 'MZ', 'continent': 'Africa', 'name': 'Mozambique', 'capital': 'Maputo'},
    {'timezones': ['Africa/Windhoek'], 'code': 'NA', 'continent': 'Africa', 'name': 'Namibia', 'capital': 'Windhoek'},
    {'timezones': ['Africa/Niamey'], 'code': 'NE', 'continent': 'Africa', 'name': 'Niger', 'capital': 'Niamey'},
    {'timezones': ['Africa/Lagos'], 'code': 'NG', 'continent': 'Africa', 'name': 'Nigeria', 'capital': 'Abuja'},
    {'timezones': ['America/Managua'], 'code': 'NI', 'continent': 'North America', 'name': 'Nicaragua', 'capital': 'Managua'},
    {'timezones': ['Europe/Amsterdam'], 'code': 'NL', 'continent': 'Europe', 'name': 'Kingdom of the Netherlands', 'capital': 'Amsterdam'},
    {'timezones': ['Europe/Oslo'], 'code': 'NO', 'continent': 'Europe', 'name': 'Norway', 'capital': 'Oslo'},
    {'timezones': ['Asia/Katmandu'], 'code': 'NP', 'continent': 'Asia', 'name': 'Nepal', 'capital': 'Kathmandu'},
    {'timezones': ['Pacific/Nauru'], 'code': 'NR', 'continent': 'Oceania', 'name': 'Nauru', 'capital': 'Yaren'},
    {'timezones': ['Pacific/Auckland', 'Pacific/Chatham'], 'code': 'NZ', 'continent': 'Oceania', 'name': 'New Zealand', 'capital': 'Wellington'},
    {'timezones': ['Asia/Muscat'], 'code': 'OM', 'continent': 'Asia', 'name': 'Oman', 'capital': 'Muscat'},
    {'timezones': ['America/Panama'], 'code': 'PA', 'continent': 'North America', 'name': 'Panama', 'capital': 'Panama City'},
    {'timezones': ['America/Lima'], 'code': 'PE', 'continent': 'South America', 'name': 'Peru', 'capital': 'Lima'},
    {'timezones': ['Pacific/Port_Moresby'], 'code': 'PG', 'continent': 'Oceania', 'name': 'Papua New Guinea', 'capital': 'Port Moresby'},
    {'timezones': ['Asia/Manila'], 'code': 'PH', 'continent': 'Asia', 'name': 'Philippines', 'capital': 'Manila'},
    {'timezones': ['Asia/Karachi'], 'code': 'PK', 'continent': 'Asia', 'name': 'Pakistan', 'capital': 'Islamabad'},
    {'timezones': ['Europe/Warsaw'], 'code': 'PL', 'continent': 'Europe', 'name': 'Poland', 'capital': 'Warsaw'},
    {'timezones': ['Europe/Lisbon', 'Atlantic/Madeira', 'Atlantic/Azores'], 'code': 'PT', 'continent': 'Europe', 'name': 'Portugal', 'capital': 'Lisbon'},
    {'timezones': ['Pacific/Palau'], 'code': 'PW', 'continent': 'Oceania', 'name': 'Palau', 'capital': 'Ngerulmud'},
    {'timezones': ['America/Asuncion'], 'code': 'PY', 'continent': 'South America', 'name': 'Paraguay', 'capital': 'Asuncion'},
    {'timezones': ['Asia/Qatar'], 'code': 'QA', 'continent': 'Asia', 'name': 'Qatar', 'capital': 'Doha'},
    {'timezones': ['Europe/Bucharest'], 'code': 'RO', 'continent': 'Europe', 'name': 'Romania', 'capital': 'Bucharest'},
    {'timezones': ['Europe/Kaliningrad', 'Europe/Moscow', 'Europe/Volgograd', 'Europe/Samara', 'Asia/Yekaterinburg', 'Asia/Omsk', 'Asia/Novosibirsk', 'Asia/Krasnoyarsk', 'Asia/Irkutsk', 'Asia/Yakutsk', 'Asia/Vladivostok', 'Asia/Sakhalin', 'Asia/Magadan', 'Asia/Kamchatka', 'Asia/Anadyr'], 'code': 'RU', 'continent': 'Europe', 'name': 'Russia', 'capital': 'Moscow'},
    {'timezones': ['Africa/Kigali'], 'code': 'RW', 'continent': 'Africa', 'name': 'Rwanda', 'capital': 'Kigali'},
    {'timezones': ['Asia/Riyadh'], 'code': 'SA', 'continent': 'Asia', 'name': 'Saudi Arabia', 'capital': 'Riyadh'},
    {'timezones': ['Pacific/Guadalcanal'], 'code': 'SB', 'continent': 'Oceania', 'name': 'Solomon Islands', 'capital': 'Honiara'},
    {'timezones': ['Indian/Mahe'], 'code': 'SC', 'continent': 'Africa', 'name': 'Seychelles', 'capital': 'Victoria'},
    {'timezones': ['Africa/Khartoum'], 'code': 'SD', 'continent': 'Africa', 'name': 'Sudan', 'capital': 'Khartoum'},
    {'timezones': ['Europe/Stockholm'], 'code': 'SE', 'continent': 'Europe', 'name': 'Sweden', 'capital': 'Stockholm'},
    {'timezones': ['Asia/Singapore'], 'code': 'SG', 'continent': 'Asia', 'name': 'Singapore', 'capital': 'Singapore'},
    {'timezones': ['Europe/Ljubljana'], 'code': 'SI', 'continent': 'Europe', 'name': 'Slovenia', 'capital': 'Ljubljana'},
    {'timezones': ['Europe/Bratislava'], 'code': 'SK', 'continent': 'Europe', 'name': 'Slovakia', 'capital': 'Bratislava'},
    {'timezones': ['Africa/Freetown'], 'code': 'SL', 'continent': 'Africa', 'name': 'Sierra Leone', 'capital': 'Freetown'},
    {'timezones': ['Europe/San_Marino'], 'code': 'SM', 'continent': 'Europe', 'name': 'San Marino', 'capital': 'San Marino'},
    {'timezones': ['Africa/Dakar'], 'code': 'SN', 'continent': 'Africa', 'name': 'Senegal', 'capital': 'Dakar'},
    {'timezones': ['Africa/Mogadishu'], 'code': 'SO', 'continent': 'Africa', 'name': 'Somalia', 'capital': 'Mogadishu'},
    {'timezones': ['America/Paramaribo'], 'code': 'SR', 'continent': 'South America', 'name': 'Suriname', 'capital': 'Paramaribo'},
    {'timezones': ['Africa/Sao_Tome'], 'code': 'ST', 'continent': 'Africa', 'name': 'Sao Tome and Principe', 'capital': 'Sao Tome'},
    {'timezones': ['Asia/Damascus'], 'code': 'SY', 'continent': 'Asia', 'name': 'Syria', 'capital': 'Damascus'},
    {'timezones': ['Africa/Lome'], 'code': 'TG', 'continent': 'Africa', 'name': 'Togo', 'capital': 'Lome'},
    {'timezones': ['Asia/Bangkok'], 'code': 'TH', 'continent': 'Asia', 'name': 'Thailand', 'capital': 'Bangkok'},
    {'timezones': ['Asia/Dushanbe'], 'code': 'TJ', 'continent': 'Asia', 'name': 'Tajikistan', 'capital': 'Dushanbe'},
    {'timezones': ['Asia/Ashgabat'], 'code': 'TM', 'continent': 'Asia', 'name': 'Turkmenistan', 'capital': 'Ashgabat'},
    {'timezones': ['Africa/Tunis'], 'code': 'TN', 'continent': 'Africa', 'name': 'Tunisia', 'capital': 'Tunis'},
    {'timezones': ['Pacific/Tongatapu'], 'code': 'TO', 'continent': 'Oceania', 'name': 'Tonga', 'capital': "Nuku'alofa"},
    {'timezones': ['Europe/Istanbul'], 'code': 'TR', 'continent': 'Asia', 'name': 'Turkey', 'capital': 'Ankara'},
    {'timezones': ['America/Port_of_Spain'], 'code': 'TT', 'continent': 'North America', 'name': 'Trinidad and Tobago', 'capital': 'Port of Spain'},
    {'timezones': ['Pacific/Funafuti'], 'code': 'TV', 'continent': 'Oceania', 'name': 'Tuvalu', 'capital': 'Funafuti'},
    {'timezones': ['Africa/Dar_es_Salaam'], 'code': 'TZ', 'continent': 'Africa', 'name': 'Tanzania', 'capital': 'Dodoma'},
    {'timezones': ['Europe/Kiev', 'Europe/Uzhgorod', 'Europe/Zaporozhye', 'Europe/Simferopol'], 'code': 'UA', 'continent': 'Europe', 'name': 'Ukraine', 'capital': 'Kiev'},
    {'timezones': ['Africa/Kampala'], 'code': 'UG', 'continent': 'Africa', 'name': 'Uganda', 'capital': 'Kampala'},
    {'timezones': ['America/New_York', 'America/Detroit', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Indiana/Indianapolis', 'America/Indiana/Marengo', 'America/Indiana/Knox', 'America/Indiana/Vevay', 'America/Chicago', 'America/Indiana/Vincennes', 'America/Indiana/Petersburg', 'America/Menominee', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Denver', 'America/Boise', 'America/Shiprock', 'America/Phoenix', 'America/Los_Angeles', 'America/Anchorage', 'America/Juneau', 'America/Yakutat', 'America/Nome', 'America/Adak', 'Pacific/Honolulu'], 'code': 'US', 'continent': 'North America', 'name': 'United States', 'capital': 'Washington, D.C.'},
    {'timezones': ['America/Montevideo'], 'code': 'UY', 'continent': 'South America', 'name': 'Uruguay', 'capital': 'Montevideo'},
    {'timezones': ['Asia/Samarkand', 'Asia/Tashkent'], 'code': 'UZ', 'continent': 'Asia', 'name': 'Uzbekistan', 'capital': 'Tashkent'},
    {'timezones': ['Europe/Vatican'], 'code': 'VA', 'continent': 'Europe', 'name': 'Vatican City', 'capital': 'Vatican City'},
    {'timezones': ['America/Caracas'], 'code': 'VE', 'continent': 'South America', 'name': 'Venezuela', 'capital': 'Caracas'},
    {'timezones': ['Asia/Saigon'], 'code': 'VN', 'continent': 'Asia', 'name': 'Vietnam', 'capital': 'Hanoi'},
    {'timezones': ['Pacific/Efate'], 'code': 'VU', 'continent': 'Oceania', 'name': 'Vanuatu', 'capital': 'Port Vila'},
    {'timezones': ['Asia/Aden'], 'code': 'YE', 'continent': 'Asia', 'name': 'Yemen', 'capital': "Sana'a"},
    {'timezones': ['Africa/Lusaka'], 'code': 'ZM', 'continent': 'Africa', 'name': 'Zambia', 'capital': 'Lusaka'},
    {'timezones': ['Africa/Harare'], 'code': 'ZW', 'continent': 'Africa', 'name': 'Zimbabwe', 'capital': 'Harare'},
    {'timezones': ['Africa/Algiers'], 'code': 'DZ', 'continent': 'Africa', 'name': 'Algeria', 'capital': 'Algiers'},
    {'timezones': ['Europe/Sarajevo'], 'code': 'BA', 'continent': 'Europe', 'name': 'Bosnia and Herzegovina', 'capital': 'Sarajevo'},
    {'timezones': ['Asia/Phnom_Penh'], 'code': 'KH', 'continent': 'Asia', 'name': 'Cambodia', 'capital': 'Phnom Penh'},
    {'timezones': ['Africa/Bangui'], 'code': 'CF', 'continent': 'Africa', 'name': 'Central African Republic', 'capital': 'Bangui'},
    {'timezones': ['Africa/Ndjamena'], 'code': 'TD', 'continent': 'Africa', 'name': 'Chad', 'capital': "N'Djamena"},
    {'timezones': ['Indian/Comoro'], 'code': 'KM', 'continent': 'Africa', 'name': 'Comoros', 'capital': 'Moroni'},
    {'timezones': ['Europe/Zagreb'], 'code': 'HR', 'continent': 'Europe', 'name': 'Croatia', 'capital': 'Zagreb'},
    {'timezones': ['Asia/Dili'], 'code': 'TL', 'continent': 'Asia', 'name': 'East Timor', 'capital': 'Dili'},
    {'timezones': ['America/El_Salvador'], 'code': 'SV', 'continent': 'North America', 'name': 'El Salvador', 'capital': 'San Salvador'},
    {'timezones': ['Africa/Malabo'], 'code': 'GQ', 'continent': 'Africa', 'name': 'Equatorial Guinea', 'capital': 'Malabo'},
    {'timezones': ['America/Grenada'], 'code': 'GD', 'continent': 'North America', 'name': 'Grenada', 'capital': "St. George's"},
    {'timezones': ['Asia/Almaty', 'Asia/Qyzylorda', 'Asia/Aqtobe', 'Asia/Aqtau', 'Asia/Oral'], 'code': 'KZ', 'continent': 'Asia', 'name': 'Kazakhstan', 'capital': 'Astana'},
    {'timezones': ['Asia/Vientiane'], 'code': 'LA', 'continent': 'Asia', 'name': 'Laos', 'capital': 'Vientiane'},
    {'timezones': ['Pacific/Truk', 'Pacific/Ponape', 'Pacific/Kosrae'], 'code': 'FM', 'continent': 'Oceania', 'name': 'Federated States of Micronesia', 'capital': 'Palikir'},
    {'timezones': ['Europe/Chisinau'], 'code': 'MD', 'continent': 'Europe', 'name': 'Moldova', 'capital': 'Chisinau'},
    {'timezones': ['Europe/Monaco'], 'code': 'MC', 'continent': 'Europe', 'name': 'Monaco', 'capital': 'Monaco'},
    {'timezones': ['Europe/Podgorica'], 'code': 'ME', 'continent': 'Europe', 'name': 'Montenegro', 'capital': 'Podgorica'},
    {'timezones': ['Africa/Casablanca'], 'code': 'MA', 'continent': 'Africa', 'name': 'Morocco', 'capital': 'Rabat'},
    {'timezones': ['America/St_Kitts'], 'code': 'KN', 'continent': 'North America', 'name': 'Saint Kitts and Nevis', 'capital': 'Basseterre'},
    {'timezones': ['America/St_Lucia'], 'code': 'LC', 'continent': 'North America', 'name': 'Saint Lucia', 'capital': 'Castries'},
    {'timezones': ['America/St_Vincent'], 'code': 'VC', 'continent': 'North America', 'name': 'Saint Vincent and the Grenadines', 'capital': 'Kingstown'},
    {'timezones': ['Pacific/Apia'], 'code': 'WS', 'continent': 'Oceania', 'name': 'Samoa', 'capital': 'Apia'},
    {'timezones': ['Europe/Belgrade'], 'code': 'RS', 'continent': 'Europe', 'name': 'Serbia', 'capital': 'Belgrade'},
    {'timezones': ['Africa/Johannesburg'], 'code': 'ZA', 'continent': 'Africa', 'name': 'South Africa', 'capital': 'Pretoria'},
    {'timezones': ['Europe/Madrid', 'Africa/Ceuta', 'Atlantic/Canary'], 'code': 'ES', 'continent': 'Europe', 'name': 'Spain', 'capital': 'Madrid'},
    {'timezones': ['Asia/Colombo'], 'code': 'LK', 'continent': 'Asia', 'name': 'Sri Lanka', 'capital': 'Sri Jayewardenepura Kotte'},
    {'timezones': ['Africa/Mbabane'], 'code': 'SZ', 'continent': 'Africa', 'name': 'Swaziland', 'capital': 'Mbabane'},
    {'timezones': ['Europe/Zurich'], 'code': 'CH', 'continent': 'Europe', 'name': 'Switzerland', 'capital': 'Bern'},
    {'timezones': ['Asia/Dubai'], 'code': 'AE', 'continent': 'Asia', 'name': 'United Arab Emirates', 'capital': 'Abu Dhabi'},
    {'timezones': ['Europe/London'], 'code': 'GB', 'continent': 'Europe', 'name': 'United Kingdom', 'capital': 'London'}]
    
    for i in countries:
        add1 = []
        add1.append(i["name"])
        add1.append(i["capital"])
        cocap.append(add1)
        if i ["continent"] == "Africa":
            addc = []
            addc.append(i["name"])
            addc.append(i["capital"])
            cocapAF.append(addc) 
        if i ["continent"] == "Europe":
            addc = []
            addc.append(i["name"])
            addc.append(i["capital"])
            cocapEU.append(addc)
        if i ["continent"] == "North America":
            addc = []
            addc.append(i["name"])
            addc.append(i["capital"])
            cocapNA.append(addc)
        if i ["continent"] == "South America":
            addc = []
            addc.append(i["name"])
            addc.append(i["capital"])
            cocapSA.append(addc)
        if i ["continent"] == "Oceania":
            addc = []
            addc.append(i["name"])
            addc.append(i["capital"])
            cocapOCE.append(addc)
        if i ["continent"] == "Asia":
            addc = []
            addc.append(i["name"])
            addc.append(i["capital"])
            cocapAS.append(addc)
    #print(cocap)
    #print(len(cocap))
crList()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("quiz-366218-3820a30d3b6b.json",scope)
client = gspread.authorize(creds)
mode = 0
prev =''
prevc =''
img = None
qna = cocap
#qna=[[1,'who wants it'],['Andorra', 'Andorra la Vella'], ['Afghanistan', 'Kabul'], ['Antigua and Barbuda', "St. John's"], ['Albania', 'Tirana'], ['Armenia', 'Yerevan'], ['Angola', 'Luanda'], ['Argentina', 'Buenos Aires'], ['Austria', 'Vienna'], ['Australia', 'Canberra'], ['Azerbaijan', 'Baku'], ['Barbados', 'Bridgetown'], ['Bangladesh', 'Dhaka'], ['Belgium', 'Brussels'], ['Burkina Faso', 'Ouagadougou'], ['Bulgaria', 'Sofia'], ['Bahrain', 'Manama'], ['Burundi', 'Bujumbura'], ['Benin', 'Porto-Novo'], ['Brunei Darussalam', 'Bandar Seri Begawan'], ['Bolivia', 'Sucre'], ['Brazil', 'Brasilia'], ['Bahamas', 'Nassau'], ['Bhutan', 'Thimphu'], ['Botswana', 'Gaborone'], ['Belarus', 'Minsk'], ['Belize', 'Belmopan'], ['Canada', 'Ottawa'], ['Democratic Republic of the Congo', 'Kinshasa'], ['Republic of the Congo', 'Brazzaville'], ["Cote d'Ivoire", 'Yamoussoukro'], ['Chile', 'Santiago'], ['Cameroon', 'Yaounde'], ["People's Republic of China", 'Beijing'], ['Colombia', 'Bogota¡'], ['Costa Rica', 'San Jose'], ['Cuba', 'Havana'], ['Cape Verde', 'Praia'], ['Cyprus', 'Nicosia'], ['Czech Republic', 'Prague'], ['Germany', 'Berlin'], ['Djibouti', 'Djibouti City'], ['Denmark', 'Copenhagen'], ['Dominica', 'Roseau'], ['Dominican Republic', 'Santo Domingo'], ['Ecuador', 'Quito'], ['Estonia', 'Tallinn'], ['Egypt', 'Cairo'], ['Eritrea', 'Asmara'], ['Ethiopia', 'Addis Ababa'], ['Finland', 'Helsinki'], ['Fiji', 'Suva'], ['France', 'Paris'], ['Gabon', 'Libreville'], ['Georgia', 'Tbilisi'], ['Ghana', 'Accra'], ['The Gambia', 'Banjul'], ['Guinea', 'Conakry'], ['Greece', 'Athens'], ['Guatemala', 'Guatemala City'], ['Haiti', 'Port-au-Prince'], ['Guinea-Bissau', 'Bissau'], ['Guyana', 'Georgetown'], ['Honduras', 'Tegucigalpa'], ['Hungary', 'Budapest'], ['Indonesia', 'Jakarta'], ['Republic of Ireland', 'Dublin'], ['Israel', 'Jerusalem'], ['India', 'New Delhi'], ['Iraq', 'Baghdad'], ['Iran', 'Tehran'], ['Iceland', 'Reykjavik'], ['Italy', 'Rome'], ['Jamaica', 'Kingston'], ['Jordan', 'Amman'], ['Japan', 'Tokyo'], ['Kenya', 'Nairobi'], ['Kyrgyzstan', 'Bishkek'], ['Kiribati', 'Tarawa'], ['North Korea', 'Pyongyang'], ['South Korea', 'Seoul'], ['Kuwait', 'Kuwait City'], ['Lebanon', 'Beirut'], ['Liechtenstein', 'Vaduz'], ['Liberia', 'Monrovia'], ['Lesotho', 'Maseru'], ['Lithuania', 'Vilnius'], ['Luxembourg', 'Luxembourg City'], ['Latvia', 'Riga'], ['Libya', 'Tripoli'], ['Madagascar', 'Antananarivo'], ['Marshall Islands', 'Majuro'], ['Macedonia', 'Skopje'], ['Mali', 'Bamako'], ['Myanmar', 'Naypyidaw'], ['Mongolia', 'Ulaanbaatar'], ['Mauritania', 'Nouakchott'], ['Malta', 'Valletta'], ['Mauritius', 'Port Louis'], ['Maldives', 'Male'], ['Malawi', 'Lilongwe'], ['Mexico', 'Mexico City'], ['Malaysia', 'Kuala Lumpur'], ['Mozambique', 'Maputo'], ['Namibia', 'Windhoek'], ['Niger', 'Niamey'], ['Nigeria', 'Abuja'], ['Nicaragua', 'Managua'], ['Kingdom of the Netherlands', 'Amsterdam'], ['Norway', 'Oslo'], ['Nepal', 'Kathmandu'], ['Nauru', 'Yaren'], ['New Zealand', 'Wellington'], ['Oman', 'Muscat'], ['Panama', 'Panama City'], ['Peru', 'Lima'], ['Papua New Guinea', 'Port Moresby'], ['Philippines', 'Manila'], ['Pakistan', 'Islamabad'], ['Poland', 'Warsaw'], ['Portugal', 'Lisbon'], ['Palau', 'Ngerulmud'], ['Paraguay', 'Asuncion'], ['Qatar', 'Doha'], ['Romania', 'Bucharest'], ['Russia', 'Moscow'], ['Rwanda', 'Kigali'], ['Saudi Arabia', 'Riyadh'], ['Solomon Islands', 'Honiara'], ['Seychelles', 'Victoria'], ['Sudan', 'Khartoum'], ['Sweden', 'Stockholm'], ['Singapore', 'Singapore'], ['Slovenia', 'Ljubljana'], ['Slovakia', 'Bratislava'], ['Sierra Leone', 'Freetown'], ['San Marino', 'San Marino'], ['Senegal', 'Dakar'], ['Somalia', 'Mogadishu'], ['Suriname', 'Paramaribo'], ['Sao Tome and Principe', 'Sao Tome'], ['Syria', 'Damascus'], ['Togo', 'Lome'], ['Thailand', 'Bangkok'], ['Tajikistan', 'Dushanbe'], ['Turkmenistan', 'Ashgabat'], ['Tunisia', 'Tunis'], ['Tonga', 'Nukualofa'], ['Turkey', 'Ankara'], ['Trinidad and Tobago', 'Port of Spain'], ['Tuvalu', 'Funafuti'], ['Tanzania', 'Dodoma'], ['Ukraine', 'Kiev'], ['Uganda', 'Kampala'], ['United States', 'Washington, D.C.'], ['Uruguay', 'Montevideo'], ['Uzbekistan', 'Tashkent'], ['Vatican City', 'Vatican City'], ['Venezuela', 'Caracas'], ['Vietnam', 'Hanoi'], ['Vanuatu', 'Port Vila'], ['Yemen', "Sana'a"], ['Zambia', 'Lusaka'], ['Zimbabwe', 'Harare'], ['Algeria', 'Algiers'], ['Bosnia and Herzegovina', 'Sarajevo'], ['Cambodia', 'Phnom Penh'], ['Central African Republic', 'Bangui'], ['Chad', "N'Djamena"], ['Comoros', 'Moroni'], ['Croatia', 'Zagreb'], ['East Timor', 'Dili'], ['El Salvador', 'San Salvador'], ['Equatorial Guinea', 'Malabo'], ['Grenada', "St. George's"], ['Kazakhstan', 'Astana'], ['Laos', 'Vientiane'], ['Federated States of Micronesia', 'Palikir'], ['Moldova', 'ChiÅ\x9finÄ\x83u'], ['Monaco', 'Monaco'], ['Montenegro', 'Podgorica'], ['Morocco', 'Rabat'], ['Saint Kitts and Nevis', 'Basseterre'], ['Saint Lucia', 'Castries'], ['Saint Vincent and the Grenadines', 'Kingstown'], ['Samoa', 'Apia'], ['Serbia', 'Belgrade'], ['South Africa', 'Pretoria'], ['Spain', 'Madrid'], ['Sri Lanka', 'Sri Jayewardenepura Kotte'], ['Swaziland', 'Mbabane'], ['Switzerland', 'Bern'], ['United Arab Emirates', 'Abu Dhabi'], ['United Kingdom', 'London']]
ScoreAdd = []
def randomq():
    n = random.randrange(0, len(qna))
    x = qna[n]
    y = qna[0]
    qna.remove(x)
    #print(qna)
    return x
Score = 0
def frameplay_func():
    frame.destroy()
    frameplay.pack()
def framecont_func():
    frameplay.destroy()
    framecont.pack()


def Inst():
    inst = tk.Toplevel()
    inst.geometry("1280x720")
    cover = ImageTk.PhotoImage(Image.open("RULESS.jpg"))
    #RULES = ImageTk.PhotoImage(Image.open("19doll.png"))
    label1 = tk.Label(inst, image= cover)
    label1.image = cover
    label1.place(x = 640,y = 360,anchor="center")

def gameframeAS():
    global mode
    global qna
    global flag
    flag = 1
    mode = "Asia"
    qna = cocapAS
    
    gameframe()
def gameframeAF():
    global mode
    global flag
    flag = 1
    global qna
    mode = "Africa"
    qna = cocapAF
    gameframe()
def gameframeNA():
    global mode
    global flag
    flag = 1
    global qna
    mode = "North America"
    qna = cocapNA
    gameframe()
def gameframeSA():
    global mode
    global flag
    flag = 1
    global qna
    mode = "South America"
    qna = cocapSA
    gameframe()
def gameframeOCE():
    global mode
    global qna
    global flag
    flag = 1
    mode = "Oceania"
    qna = cocapOCE
    gameframe()
def gameframeEU():
    global mode
    global qna
    global flag
    flag = 1
    mode = "Europe"
    qna = cocapEU
    gameframe()

def gameframe2():
    global mode
    global qna
    mode = '10countries'
    print(mode)
    random.shuffle(qna)
    qna = qna[:11]
    gameframe()

def restart():
    gameframe()

def gameframe():
    global mode
    global qna
    global Score
    global sm
    def createlist():

        if mode == '10countries':
            username = usern_var.get()
            if username == '':
                quit
            else:
                global ScoreAdd
                ScoreAdd = [username,'-',Score,'-','-','-','-','-','-']
                add(ScoreAdd)
        elif mode == 'Asia':
            username = usern_var.get()
            if username == '':
                quit
            else:
        
                ScoreAdd = [username,'-','-',Score,'-','-','-','-','-']
                add(ScoreAdd)
        elif mode == 'Africa':
            username = usern_var.get()
            if username == '':
                quit
            else:
                
                ScoreAdd = [username,'-','-','-',Score,'-','-','-','-']
                add(ScoreAdd)
        elif mode == 'North America':
            username = usern_var.get()
            if username == '':
                quit
            else:
                
                ScoreAdd = [username,'-','-','-','-',Score,'-','-','-']
                add(ScoreAdd)  
        elif mode == 'South America':
            username = usern_var.get()
            if username == '':
                quit
            else:
                
                ScoreAdd = [username,'-','-','-','-','-',Score,'-','-']
                add(ScoreAdd)  
        
                add(ScoreAdd)
        elif mode == 'Europe':
            username = usern_var.get()
            if username == '':
                quit
            else:
                
                ScoreAdd = [username,'-','-','-','-','-','-',Score,'-']
                add(ScoreAdd)              
        elif mode == 'Oceania':
            username = usern_var.get()
            if username == '':
                quit
            else:
                
                ScoreAdd = [username,'-','-','-','-','-','-','-',Score]
                add(ScoreAdd)
        else:
            username = usern_var.get()
            if username == '':
                quit
            else:
                ScoreAdd = [username,Score]
                add(ScoreAdd)

    ans_var = tk.StringVar()
    qlist = randomq()
    frameplay.destroy()
    if flag == 1:
        framecont.destroy()
    frame1 = Frame(sm,width=1280, height=720,bg="black")
    frame1.pack()
    def check():
        
        global Score
        answer = ans_var.get()
        
        if answer.lower() == qlist[1].lower():
            Score = Score + 1
            frame1.destroy()
            global prev
            global prevc
            prev = qlist[1]
            prevc = qlist[0]
            restart()
        elif answer.lower() != qlist[1].lower():
            
            prev = qlist[1]
            prevc = qlist[0]
            frame1.destroy()
            restart()
        
        if qna == []:
            usern_var = tk.StringVar()
            frame1.destroy()
            frame3 = Frame(sm,width=1280, height=720,bg="black")
            frame3.pack()
            canvas2 = tk.Canvas(frame3, bg="black", height=720, width=1280)
            canvas2.pack()
            usern = tk.Entry(canvas2,textvariable = usern_var, font=('calibre',10,'normal'),bg = "white",fg = "black")
            usern.place(x = 640, y = 300 + 100,anchor=CENTER)
            label1 = tk.Label(canvas2,text='Enter name here ->',fg="white",bg="black")
            label1.place(x=500,y=400, anchor = CENTER )
            butA = tk.Button(canvas2,text ="Add score",bg = "white",command = createlist)
            butA.place(x =640,y = 300 + 100 + 50, anchor = CENTER,width = 150, height = 45)
            canvas2.create_text(640, 360, fill="darkred", text='game over, your final score is: '+str(Score),font=("Times",20),anchor=CENTER)
        

    if qlist[0] == 1:
        global img
        canvas = tk.Canvas(frame1, bg="white", height=300, width=600)
        canvas.place(x = 640, y = 200, anchor = CENTER)
        ans = tk.Entry(frame1,textvariable = ans_var, font=('calibre',10,'normal'),bg = "white",fg = "black")
        ans.place(x = 640, y = 300 + 100,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("19doll.png"))
        canvas.create_text(320, 30, fill="darkblue", text='19 dollar fortnite card',font=("Times",20),anchor="center")
        canvas.create_image(320,50,image = img,anchor=N)
        label1 = tk.Label(frame1,text='Enter answer here ->',fg="white",bg="black")
        label1.place(x=500,y=400, anchor = CENTER )
        butA = tk.Button(frame1,text ="Answer",bg = "white",command = check)
        butA.place(x =640,y = 300 + 100 + 50, anchor = CENTER,width = 150, height = 45)
    
    
    else:
        canvas = tk.Canvas(frame1, bg="white", height=300, width=600)
        canvas.place(x = 640, y = 200, anchor = CENTER)
        ans = tk.Entry(frame1,textvariable = ans_var, font=('calibre',10,'normal'),bg = "white",fg = "black")
        ans.place(x = 640, y = 300 + 100,anchor=CENTER)
        
        canvas.create_text(300, 150, fill="darkblue", text=qlist[0],font=("Times",20),anchor=CENTER)
        label1 = tk.Label(frame1,text='Enter answer here ->',fg="white",bg="black")
        label1.place(x=500,y=400, anchor = CENTER )
        butA = tk.Button(frame1,text ="Answer",bg = "white",command = check)
        butA.place(x =640,y = 300 + 100 + 50, anchor = CENTER,width = 150, height = 45)
        if prev != '':
            canvas.create_text(300, 250, fill="darkred", text= 'Previous country: '+ prevc ,font=("Times",10),anchor=CENTER)
            canvas.create_text(300, 270, fill="darkred", text= ' Capital: '+ prev,font=("Times",10),anchor=CENTER)

    '''canvas = tk.Canvas(frame1, bg="white", height=300, width=600)
    canvas.place(x = 640, y = 200, anchor = CENTER)
    ans = tk.Entry(frame1,textvariable = ans_var, font=('calibre',10,'normal'),bg = "white",fg = "black")
    ans.place(x = 640, y = 300 + 100,anchor=CENTER)
    
    canvas.create_text(300, 150, fill="darkblue", text=qlist[0],font=("Times",20),anchor=CENTER)
    label1 = tk.Label(frame1,text='Enter answer here ->',fg="white",bg="black")
    label1.place(x=500,y=400, anchor = CENTER )
    butA = tk.Button(frame1,text ="Answer",bg = "white",command = check)
    butA.place(x =640,y = 300 + 100 + 50, anchor = CENTER,width = 150, height = 45)'''

    if qna == []:
        usern_var = tk.StringVar()
        frame1.destroy()
        frame3 = Frame(sm,width=1280, height=720,bg="black")
        frame3.pack()
        canvas2 = tk.Canvas(frame3, bg="black", height=720, width=1280)
        canvas2.pack()
        usern = tk.Entry(canvas2,textvariable = usern_var, font=('calibre',10,'normal'),bg = "white",fg = "black")
        usern.place(x = 640, y = 300 + 100,anchor=CENTER)
        label1 = tk.Label(canvas2,text='Enter name here ->',fg="white",bg="black")
        label1.place(x=500,y=400, anchor = CENTER )
        butA = tk.Button(canvas2,text ="Add score",bg = "white",command = createlist)
        butA.place(x =640,y = 300 + 100 + 50, anchor = CENTER,width = 150, height = 45)
        canvas2.create_text(640, 360, fill="darkred", text='game over, your final score is: '+str(Score),font=("Times",20),anchor=CENTER)
        label2 = tk.Label(canvas2,text='Link for highscores ->',fg="white",bg="black")
        label2.place(x=220,y=600, anchor = CENTER )
        link = ("https://docs.google.com/spreadsheets/d/18b_8diTA4ozjI7E9bIagzYoURqHkLvNeJsiVP5WMwec/edit?usp=sharing")
        link1 = tk.Text(canvas2, font=('calibre',10,'normal'),bg = "white",fg = "black" , width =100, height = 2)
        link1.place(x = 640, y = 600,anchor=CENTER)
        link1.insert(END, link)
        
def add(x):
    sheet = client.open("pycodE").sheet1   
    data = sheet.get_all_records() 
    pp(data)
    length = len(data)
    sheet.insert_row(x,length+2)
    print("The row has been added")

sm = tk.Tk()
sm.geometry("1280x720")
frame = Frame(sm, width=1280, height=720,bg="white" )
butplay = Button(frame, text="Play", width=50, height=5,command=frameplay_func,bg="black",fg="white")

butplay.place(x = 640-360-50, y = 460,anchor=CENTER)
but3 = Button(frame, text="Instructions and Rules", width=50, height=5,command=Inst,bg="black",fg="white")
but3.place(x = 640-25, y = 460,anchor=CENTER)
'''but4 = Button(frame, text="does nothing", width=50, height=5,command=lambda:None,bg="black",fg="white")
but4.place(x = 640-25, y = 600,anchor=CENTER)'''
but3 = Button(frame, text="does nothing", width=50, height=5,command=lambda:None,bg="black",fg="white")
but3.place(x = 640+360, y = 460,anchor=CENTER)
gamemodeimage = ImageTk.PhotoImage(Image.open("WORLD.png"))
gamemodelabel1 = tk.Label(frame,image=gamemodeimage)
gamemodelabel1.image = gamemodeimage
gamemodelabel1.place(x=0,y=0)
frameplay = tk.Frame(sm,width=1280, height=720,bg="black")
framecont = tk.Frame(sm,width=1280, height=720,bg="black")
but2 = Button(frameplay, text="Play for 10 countries", width=50, height=5,command=gameframe2,bg="black",fg="white")
but2.place(x = 640-25, y = 360,anchor=CENTER)
but1 = Button(frameplay, text="Play for all countries", width=50, height=5,command=gameframe,bg="black",fg="white")
but1.place(x = 640-360-50, y = 360,anchor=CENTER)
but4 = Button(frameplay, text="Play according to continent", width=50, height=5,command=framecont_func,bg="black",fg="white")
but4.place(x = 640+360, y = 360,anchor=CENTER)
butAS = Button(framecont, text="Asia", width=50, height=5,command=gameframeAS,bg="black",fg="white")
butAS.place(x = 640-360-50, y = 360,anchor=CENTER)
butAF = Button(framecont, text="Africa", width=50, height=5,command=gameframeAF,bg="black",fg="white")
butAF.place(x = 640-25, y = 360,anchor=CENTER)
butNA = Button(framecont, text="North America", width=50, height=5,command=gameframeNA,bg="black",fg="white")
butNA.place(x = 640+360, y = 360,anchor=CENTER)
butEU = Button(framecont, text="Europe", width=50, height=5,command=gameframeEU,bg="black",fg="white")
butEU.place(x = 640+360, y = 460,anchor=CENTER)
butSA = Button(framecont, text="South America", width=50, height=5,command=gameframeSA,bg="black",fg="white")
butSA.place(x = 640-25, y = 460,anchor=CENTER)
butOCE = Button(framecont, text="Oceania", width=50, height=5,command=gameframeOCE,bg="black",fg="white")
butOCE.place(x = 640-360-50, y = 460,anchor=CENTER)
gamemodeimage = ImageTk.PhotoImage(Image.open("gamemode.jpg"))
gamemodelabel1 = tk.Label(frameplay,image=gamemodeimage,borderwidth=0, highlightthickness=0)
gamemodelabel1.image = gamemodeimage
gamemodelabel1.place(x=0,y=0)
continentimage = ImageTk.PhotoImage(Image.open("continent.jpg"))
continentlabel1 = tk.Label(framecont,image=continentimage,borderwidth=0, highlightthickness=0)
continentlabel1.image = continentimage
continentlabel1.place(x=0,y=0)
frame.pack()
sm.update()
#print(but1.winfo_height(),but1.winfo_width())
sm.mainloop()














    
    

