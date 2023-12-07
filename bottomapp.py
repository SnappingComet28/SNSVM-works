from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.graphics import Color
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
import random
import dropbox as dbx
import threading as th
from time import sleep as sp
import qrcode as qr
from datetime import datetime,date
import mysql.connector

# database = mysql.connector.connect(host="localhost",user="root",password="",database="food")
# server = database.cursor()

style = '''
<DrawerClickableItem@MDNavigationDrawerItem>
MDBoxLayout:
    orientation: 'vertical'
    MDNavigationLayout:
        ScreenManager:
            id: screen         	                      			                 
            Screen:
                name: "main"
                MDBottomAppBar:
                    MDTopAppBar:
                        md_bg_color: 240/255, 67/255, 55/254, 1
                        MDIconButton:
                            icon : "home"
                            on_release:app.change_screen("main")
                            pos_hint:{"center_x":0.45}
                MDTopAppBar:
                    pos_hint: {'top': 1}
                    title: "XYZ Hospital"
                    elevation: 5
                    id: color
                    md_bg_color: 240/255, 67/255, 55/254, 1
                    center_title: True
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["heart-plus"]]
               
                MDCard:
                	padding:"20dp"
                	size_hint:None,None
                	radius:[48]
                	elevation:4
                	pos_hint:{"center_x":0.2,"center_y":0.6}
                	md_bg_color:230/255, 225/255, 225/255,1
                    size:350,300
                    on_release :app.change_screen("choose")
                    MDRelativeLayout:
	                    MDLabel:
	                    	text:"Register"
	                    	theme_text_color : "Primary"
	                    	pos_hint:{"center_x":0.8,"center_y":0.9999}
	                    Image:
	                    	source:"register.png"
	                    	pos_hint:{"center_x":0.5,"center_y":0.376}
                            size_hint : None,None
                            size:450,220
                MDCard:
                	padding:"20dp"
                	size_hint:None,None
                	radius:[48]
                	elevation:4
                	pos_hint:{"center_x":0.5,"center_y":0.6}
                	md_bg_color:230/255, 225/255, 225/255,1
                    size:350,300
                    on_release :app.change_screen("choose1")
                    MDRelativeLayout:
	                    MDLabel:
	                    	text:"Contact Doctor"
	                    	theme_text_color : "Primary"
	                    	pos_hint:{"center_x":0.7,"center_y":0.9999}
	                    Image:
	                    	source:"msg.png"
	                    	pos_hint:{"center_x":0.5,"center_y":0.376}
                MDCard:
                	padding:"20dp"
                	size_hint:None,None
                	radius:[48]
                	elevation:4
                	pos_hint:{"center_x":0.8,"center_y":0.6}
                	md_bg_color:230/255, 225/255, 225/255,1
                    size:350,300
                    on_release :app.change_screen("order")
                    MDRelativeLayout:
	                    MDLabel:
	                    	text:"Order Medicine"
	                    	theme_text_color : "Primary"
	                    	pos_hint:{"center_x":0.8,"center_y":0.9999}
	                    Image:
	                    	source:"Ord.png"
	                    	pos_hint:{"center_x":0.5,"center_y":0.39}
	                    	size_hint:None,None
	                    	size:450,220
            Screen:
                name:"order"
                MDTopAppBar:
                    left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]
                    pos_hint:{'top':1}
                    title:"Order Medicine"
                MDBottomAppBar:
                    MDTopAppBar:
                        MDIconButton:
                            icon : "home"
                            on_release:app.change_screen("main")
                            pos_hint:{"center_x":0.45}
                MDLabel:
                    text:"Fill out the details"
                    bold:True
                    halign:"center"
                    pos_hint:{"center_x":0.5,"center_y":0.84}
                MDTextField:
                    id: name
                    pos_hint:{"center_x":0.5,"center_y":0.76}
                    size_hint: (0.5, None)
                    hint_text:"Name of the Order"
                MDTextField:
                    id:address
                    pos_hint:{"center_x":0.5,"center_y":0.68}
                    size_hint: (0.5, None)
                    hint_text:"Address"
                MDTextField:
                    id:pin
                    pos_hint:{"center_x":0.5,"center_y":0.60}
                    size_hint: (0.5, None)
                    hint_text:"PinCode"
                    input_filter:"int"
                MDRaisedButton:
                    text: "Submit"
                    pos_hint:{"center_x":0.50,"center_y":0.33}
                    on_release: app.change_screen("done")
                MDTextField:
                    id: medicine name
                    pos_hint:{"center_x":0.5,"center_y":0.45}
                    size_hint: (0.5, None)
                    hint_text: "Name of the medicine"
                MDTextField:
                    id:phone
                    pos_hint:{"center_x":0.5,"center_y":0.52}
                    size_hint:(0.5,None)
                    hint_text:"Phone number (+91)"        
            Screen:
                name: "bot"
                MDBoxLayout:
                    MDTopAppBar:
                        title: "Helper Bot"
                        pos_hint: {"top": 1}
                        md_bg_color: 143/255, 81/255, 194/255, 1
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            Screen:
                name:"doctor_list"
                MDRelativeLayout:
                	md_bg_color:206/255, 235/255, 232/255,1
                	orientation:"vertical"
                	MDTopAppBar:
                		pos_hint:{"top":1}
                		title:"Doctor List"
                	    left_action_items:[["arrow-left", lambda x : app.change_screen("choose")]]
                	ScrollView:
                	    pos_hint:{"top":0.9}
                	    size_hint_y:0.9
                    	MDBoxLayout:
                    		orientation:"vertical"
                    		id:list
                    		adaptive_height:True
                    		spacing:"20dp"

            Screen:
            	name:"wait"
            	MDFloatLayout:
            		MDTopAppBar:
            			pos_hint:{"top":1}
                        left_action_items:[["arrow-left", lambda x : app.cancelreq()]]
            		MDLabel:
            			text:"Please Wait, Finding A Doctor" 
            			pos_hint:{"center_x":0.65,"center_y":0.5}
            			font_style: "H2"   
            			bold:True
                    
            Screen:
            	name:"chat_room"
	            MDBoxLayout:
				    orientation: "vertical"
				    md_bg_color : 229/255, 235/255, 148/255,1
				
				    ScrollView:
				        MDBoxLayout:
				            orientation: "vertical"
				            id: chat
				            spacing: "20dp"
				            adaptive_height: True
				    MDRelativeLayout:
				        size_hint: (1, 0.15)
				        MDTextFieldRect:
				            hint_text: "message"
				            size_hint: None, None
				            size: 1200, 60
				            id: message
				            
				            pos_hint: {"center_x": 0.5, "center_y": 0.19}
				
				        MDIconButton:
				            icon: "send"
				            theme_text_color :"Custom"
				            text_color : 1,1,1,1
				            md_bg_color:15/255, 148/255, 117/255,1
				            pos_hint: {"center_x": 0.85, "center_y": 0.19}
				            on_release: app.send()
                    		
                   
            Screen:
                name:"choose1"
                MDBottomAppBar:
                    MDTopAppBar:
                        MDIconButton:
                            icon : "home"
                            on_release:app.change_screen("main")
                            pos_hint:{"center_x":0.45}
                MDTopAppBar:
                    title:"Choose The Doctor Type"
                    pos_hint:{"top":1}
                    md_bg_color:32/255, 156/255, 132/255, 1
                    left_action_items:[["arrow-left", lambda x:app.change_screen("main")]]


                ScrollView:
                    pos_hint:{"center_y":.43,"center_x":.55}
                    
                    GridLayout:
                        cols:4
                        adaptive_height: True
                        spacing:"40dp"
                        padding:"30dp"
                        MDCard:
                            padding:"50dp"
                            md_bg_color:81/255, 219/255, 194/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "cardiac.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.8}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"Cardiologist"
                                    pos_hint :{"center_x":0.69,"center_y":0.3}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"Heart doctor"  
                                    pos_hint :{"center_x":0.7,"center_y":0.17}
                                    theme_text_color:"Secondary"
                        MDCard:
                            padding:"50dp"
                            md_bg_color:154/255, 222/255, 91/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "dentist.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.8}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"Dentist"
                                    pos_hint :{"center_x":0.69,"center_y":0.3}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"Teeth doctor"  
                                    pos_hint :{"center_x":0.6,"center_y":0.17}
                                    theme_text_color:"Secondary"                                		     
                                                            
                        MDCard:
                            padding:"50dp"
                            md_bg_color:230/255, 155/255, 76/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "eye.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.8}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"Ophthalmic"
                                    pos_hint :{"center_x":0.69,"center_y":0.3}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"Eye doctor"  
                                    pos_hint :{"center_x":0.7,"center_y":0.17}
                                    theme_text_color:"Secondary"
                                                                                            
                        MDCard:
                            padding:"50dp"
                            md_bg_color:81/255, 126/255, 232/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "stomach.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.8}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"Gastroentero"
                                    pos_hint :{"center_x":0.52,"center_y":0.23}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"Stomach doctor"  
                                    pos_hint :{"center_x":0.5,"center_y":0.13}
                                    theme_text_color:"Secondary"

                        MDCard:
                            padding:"50dp"
                            md_bg_color:90/255, 155/255, 180/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "neuro.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.8}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"Neurologist"
                                    pos_hint :{"center_x":0.69,"center_y":0.3}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"Brain doctor"  
                                    pos_hint :{"center_x":0.7,"center_y":0.17}
                                    theme_text_color:"Secondary"                                		                                	                                		                          	      	                                		                             	                                		                          	      	
                        MDCard:
                            padding:"50dp"
                            md_bg_color:235/255, 56/255, 96/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "bones.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.8}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"Orthopedic"
                                    pos_hint :{"center_x":0.69,"center_y":0.3}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"Bone doctor"  
                                    pos_hint :{"center_x":0.7,"center_y":0.17}
                                    theme_text_color:"Secondary"

                        MDCard:
                            padding:"50dp"
                            md_bg_color:187/255, 230/255, 101/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "doctor.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.82}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"general practitioner"
                                    pos_hint :{"center_x":0.69,"center_y":0.2}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"General doctor"  
                                    pos_hint :{"center_x":0.7,"center_y":0.01}
                                    theme_text_color:"Secondary"              

                        MDCard:
                            padding:"50dp"
                            md_bg_color:130/255, 230/255, 227/255,1
                            radius:[16,16,16,16]
                            on_release:app.request()
                            size_hint: None, None
                            elevation:4
                            size: "250dp", "250dp"
                            MDRelativeLayout:
                                Image:
                                    source: "kidney.jpg"
                                    pos_hint :{"center_x":0.5,"center_y":0.8}
                                    size_hint:None,None
                                    size:"150dp","150dp"
                                MDLabel:
                                    text:"nephrologist"
                                    pos_hint :{"center_x":0.69,"center_y":0.23}
                                    theme_text_color:"Custom"
                                    text_color:1,1,1,1
                                    bold:True
                                    font_style:"H6"
                                MDLabel:
                                    text:"Kidney doctor"  
                                    pos_hint :{"center_x":0.7,"center_y":0.08}
                                    theme_text_color:"Secondary"                    		
                                		
            Screen:
                name:"choose"
                MDFloatLayout:
                    md_bg_color:232/255, 230/255, 223/255,1
                    MDBottomAppBar:
                        MDTopAppBar:
                            MDIconButton:
                                icon : "home"
                                on_release:app.change_screen("main")
                                pos_hint:{"center_x":0.45}
                    MDTopAppBar:
                        title:"Choose The Doctor Type"
                        pos_hint:{"top":1}
                        md_bg_color:68/255, 156/255, 32/255, 1
                        left_action_items:[["arrow-left", lambda x:app.change_screen("main")]]
                    ScrollView:
                        pos_hint:{"center_y":.43}
                        
                        GridLayout:
                            cols:4
                            adaptive_height: True
                            spacing:"40dp"
                            padding:"30dp"
                            MDCard:
                                padding:"50dp"
                                md_bg_color:81/255, 219/255, 194/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "cardiac.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.8}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"Cardiologist"
                                		pos_hint :{"center_x":0.69,"center_y":0.3}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"Heart doctor"  
                                		pos_hint :{"center_x":0.7,"center_y":0.17}
                                		theme_text_color:"Secondary"
                            MDCard:
                                padding:"50dp"
                                md_bg_color:154/255, 222/255, 91/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "dentist.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.8}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"Dentist"
                                		pos_hint :{"center_x":0.69,"center_y":0.3}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"Teeth doctor"  
                                		pos_hint :{"center_x":0.6,"center_y":0.17}
                                		theme_text_color:"Secondary"                                		     
                                		                       
                            MDCard:
                                padding:"50dp"
                                md_bg_color:230/255, 155/255, 76/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "eye.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.8}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"Ophthalmic"
                                		pos_hint :{"center_x":0.69,"center_y":0.3}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"Eye doctor"  
                                		pos_hint :{"center_x":0.7,"center_y":0.17}
                                		theme_text_color:"Secondary"
                                	                                		                    
                            MDCard:
                                padding:"50dp"
                                md_bg_color:81/255, 126/255, 232/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "stomach.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.8}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"Gastroentero"
                                		pos_hint :{"center_x":0.52,"center_y":0.23}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"Stomach doctor"  
                                		pos_hint :{"center_x":0.5,"center_y":0.13}
                                		theme_text_color:"Secondary"

                            MDCard:
                                padding:"50dp"
                                md_bg_color:90/255, 155/255, 180/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "neuro.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.8}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"Neurologist"
                                		pos_hint :{"center_x":0.69,"center_y":0.3}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"Brain doctor"  
                                		pos_hint :{"center_x":0.7,"center_y":0.17}
                                		theme_text_color:"Secondary"                                		                                	                                		                          	      	                                		                             	                                		                          	      	
                            MDCard:
                                padding:"50dp"
                                md_bg_color:235/255, 56/255, 96/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "bones.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.8}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"Orthopedic"
                                		pos_hint :{"center_x":0.69,"center_y":0.3}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"Bone doctor"  
                                		pos_hint :{"center_x":0.7,"center_y":0.17}
                                		theme_text_color:"Secondary"
  
                            MDCard:
                                padding:"50dp"
                                md_bg_color:187/255, 230/255, 101/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "doctor.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.82}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"general practitioner"
                                		pos_hint :{"center_x":0.69,"center_y":0.2}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"General doctor"  
                                		pos_hint :{"center_x":0.7,"center_y":0.01}
                                		theme_text_color:"Secondary"              

                            MDCard:
                                padding:"50dp"
                                md_bg_color:130/255, 230/255, 227/255,1
                                radius:[16,16,16,16]
                                on_release:app.doc_list()
                                size_hint: None, None
                                elevation:4
                                size: "250dp", "250dp"
                                MDRelativeLayout:
                                	Image:
                                		source: "kidney.jpg"
                               		 pos_hint :{"center_x":0.5,"center_y":0.8}
                               		 size_hint:None,None
                               		 size:"150dp","150dp"
                               	 MDLabel:
                                		text:"nephrologist"
                                		pos_hint :{"center_x":0.69,"center_y":0.23}
                                		theme_text_color:"Custom"
                                		text_color:1,1,1,1
                                		bold:True
                                		font_style:"H6"
                                	MDLabel:
                                		text:"Kidney doctor"  
                                		pos_hint :{"center_x":0.7,"center_y":0.08}
                                		theme_text_color:"Secondary" 
            Screen:
                name:"regerror"
                MDTopAppBar:
                    pos_hint:{"top":1}
                    elevation:4
                    md_bg_color: 68/255, 156/255, 132/255, 1
                    title: "Error"
                    left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]
                MDLabel:
                    text:"Invalid Date and/or time. Please Try again "
                    pos_hint:{"center_x":0.8,"center_y":0.5}
                                                   		                                                                                                                    		                                                            
                                         
            Screen:
                name: "register"
                MDRelativeLayout:
                    MDTopAppBar:
                        size_hint_y: None
                        pos_hint:{"top":1}
                        elevation:4
                        md_bg_color: 68/255, 156/255, 132/255, 1
                        title: "Register Screen"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    MDIconButton:
                        icon: "arrow-left-bold"
                        pos_hint: {"center_x": 0.01, "top": 0.90}
                        on_release: app.change_screen("doctor_list")
                    MDLabel:
                        text: "REGISTRATION"
                        halign: "center"
                        pos_hint:{"center_x":0.5,"center_y":0.84}
                        size_hint_y: None
                        height: self.texture_size[1]
                        bold : True
                    MDTextFieldRect:
                        spacing: "40dp"
                        id: name
                        pos_hint: {"center_x": 0.5, "center_y": 0.76}
                        size_hint: (0.5, None)
                        height: "40dp"
                        hint_text: "Name"
                    MDTextFieldRect:
                        id: age
                        pos_hint: {"center_x": 0.5, "center_y": 0.66}
                        size_hint: (0.5, None)
                        height: "40dp"
                        hint_text: "Age"
                        input_filter: "int"
                    MDLabel:
                    	text:"Male"
                    	pos_hint: {"center_x": 0.8, "center_y": 0.56}
                    MDCheckbox:
                    	group: "gender"
                    	id: male
                    	ripple_scale:0
                    	size_hint:None,None
                    	pos_hint: {"center_x": 0.35, "center_y": 0.56}
                    MDLabel:
                    	text:"Female"
                    	pos_hint: {"center_x": 0.94, "center_y": 0.56}
                    MDCheckbox:
                    	group: "gender"
                    	id:female
                    	ripple_scale:0
                    	size_hint:None,None
                    	pos_hint: {"center_x": 0.5, "center_y": 0.56}
                    MDTextFieldRect:
                        id: phone
                        pos_hint: {"center_x": 0.5, "center_y": 0.46}
                        size_hint: (0.5, None)
                        height: "40dp"
                        hint_text: "Phone no"
                        input_filter: "int"
                    MDTextFieldRect:
                        id: disease
                        pos_hint: {"center_x": 0.5, "center_y": 0.36}
                        size_hint: (0.5, None)
                        height: "40dp"
                        hint_text: "Enter your disease"
                    MDRoundFlatIconButton:
                    	icon:"calendar-today"
                    	text:"Select Date"
                    	pos_hint:{"center_x":0.3,"center_y":0.26}
                    	on_release:app.datepic()
                    MDLabel:
                    	id : date
                    	text:"Selected Date: "
                    	pos_hint:{"center_x":0.75,"center_y":0.19}
                    MDRoundFlatIconButton:
                    	icon:"clock-time-eight"
                    	text:"Select starting time"
                    	pos_hint:{"center_x":0.55,"center_y":0.26}
                    	on_release:app.timepic()
                    MDRoundFlatIconButton:
                    	icon:"clock-time-eight"
                    	text:"Select ending time"
                    	pos_hint:{"center_x":0.75,"center_y":0.26}
                    	on_release:app.time1pic()
                    MDLabel:
                    	id : time
                    	text:"Selected time from _ to _ "
                    	pos_hint:{"center_x":0.95,"center_y":0.19}
                    MDRoundFlatIconButton:
                        icon: "notebook-heart"
                        text: "Register"
                        size: (200, 300)
                        pos_hint: {"center_x": 0.5, "center_y": 0.04}
                        on_release: app.info()

            Screen:
                name: "recent"
                MDBottomAppBar:
                    MDTopAppBar:
                        MDIconButton:
                            icon : "home"
                            on_release:app.change_screen("main")
                            pos_hint:{"center_x":0.45}
                MDTopAppBar:
                    title: "Recent Registrations"
                    pos_hint: {"top": 1}
                    left_action_items:[["arrow-left",lambda x : app.change_screen("main")]]
                
                ScrollView:
                    MDBoxLayout:
                        orientation: "vertical"
                        id: qr
                        spacing: 20
                        adaptive_height: True
            Screen:
                name: "done"
                MDTopAppBar:
                    pos_hint:{'top':1}
                    title:"Order Medicine"
                    left_action_items: [["arrow-left", lambda x:app.change_screen("main")]]
                MDLabel:
                    text:"We have submitted your request."
                    pos_hint:{"center_x":0.85,"center_y":0.54}
                    bold:True
                MDLabel:
                    text:"Our Service will very soon let you know for delivery."
                    pos_hint:{"center_x":0.78,"center_y":0.49}
                    bold:True
            Screen:
                name: "temp"
                MDRelativeLayout:
                    orientation: "vertical"
                    id: temp_qr
                    MDTopAppBar:
                        title: "Thanks for Registration"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        pos_hint: {'top': 1}
                    MDLabel:
                        text: "THANKS FOR REGISTRATION"
                        pos_hint: {"center_x": 0.5, "center_y": .8}
                        halign: "center"
                        bold:True
                    MDIconButton:
                        icon: "arrow-left-bold"
                        pos_hint: {"center_x": 0.01, "center_y": 0.9}
                        on_release: app.change_screen("main")
            Screen:
                name: "error"
                MDTopAppBar:
                    pos_hint:{'top':1}
                    title:"Order Medicine"
                MDLabel:
                    text:"Error! one or more Details aren't filled. Please fill it"
                    pos_hint:{"center_x":0.78,"center_y":0.55}
                    bold:True
                    #add a function here that autmoatically changes screen to 
                    #"medicine" after a delay of 5 second                       
            
        MDNavigationDrawer:
            id: nav_drawer
            md_bg_color: 208/255, 222/255, 245/255, 1
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title: "profile"
                    spacing: "50dp"
                    padding: 50
                
                 
                DrawerClickableItem:
                    padding: 13
                    text: "Recent Registration"
                    on_release: app.change_screen("recent")
'''
		
db=dbx.Dropbox("sl.BqBZszXdRrDTOcUaC8duoMxf2uvDx0qzoZMGqARfhNRUbbPrKPOs_sY2IIaKP4pTwyLJaOuwZIBwq4_LqeU5aTN9BZNZJqNN4UOJzHR8r3eEeoAkD0uXR")
file_path = "/test/ppl2.txt"
qrcode=[]
class MyApp(MDApp):

    def build(self):
        return Builder.load_string(style)

    def change_screen(self, screen_name):
        self.root.ids.screen.current = screen_name
    def datepic(self):
        date1 = MDDatePicker()
        date1.bind(on_save=self.date_saved)
        date1.open()
    def seperatestr(self):
        value = str(value)
        year,month,date = value.split("-")
        return year,month,date
        #comeplete invalid date system
    def date_saved(self, instance, value, date_range):
        self.root.ids.date.text = f"Selected Date: {value}"
        if date.today() >= datetime(self.seperatestr()):
            pass
        else:
            self.change_screen("regerror")
        self.value = value

    def timepic(self):
        t = MDTimePicker()
        t.bind(on_save=self.t1_save)
        t.open()

    def t1_save(self, instance, value1):
        self.value1 = value1
        self.root.ids.time.text = f"Selected time from {value1} to _"
    def time1pic(self):
        t2 = MDTimePicker()
        t2.bind(on_save=self.t3_save)
        t2.open()

    def t3_save(self, instance, value2):
        v1 = self.value1
        self.root.ids.time.text = f"Selected time from {v1} to {value2}"    
        self.value2 = value2
    def info(self):
        gender = None
        if self.root.ids.male.state == 'down':
            gender = "male"
        elif self.root.ids.female.state == "down":
            gender = "female"
        name = self.root.ids["name"].text
        age = self.root.ids["age"].text
        phone = self.root.ids["phone"].text
        disease = self.root.ids["disease"].text
        text1 = f" name: {name} \n age: {age}\n gender : {gender}\n phone no: {phone}\n disease: {disease}\n Date :{self.value} \nTiming : from {self.value1} to {self.value2}  "
        img_path = f"qr{len(qrcode) + 1}.png"
        with open("file.txt", "a") as file:
            file.write(text1 + "\n")
        self.change_screen("temp")
        img = qr.make(text1)
        img.save(img_path)
        card = MDCard(size_hint=(None, None), size=(700, 500), pos_hint={"center_x": 0.5 , "center_y": 0.8}, elevation=4)
        current_date = datetime.now().strftime("%d %b %Y")
        text2 = MDLabel(text=text1, pos_hint={"center_x": 0.4}, shorten=False)
        date8 = MDLabel(text=current_date, pos_hint={"center_x": 0.2, "center_y": .90}, theme_text_color="Primary")
        img2 = Image(source=img_path, size_hint=(2, 1))
        card.add_widget(img2)
        card.add_widget(text2)
        card.add_widget(date8)
        self.root.ids.qr.add_widget(card)

    def doc_list(self):
        for i in range(1, 20):
            doct = MDCard(
                size_hint=(None, None),
                size=(900, 500),
                elevation=4,
                pos_hint={"center_x": .5, "center_y": 0.3},
                md_bg_color=(212/255, 214/255, 205/255, 1),
                radius=[35],
                size_hint_y=None,
                on_release=lambda a: self.change_screen("register")
            )
            doc_photo = Image(
                source="doc.jpg",
                pos_hint={"center_x": 0.4, "center_y": 0.5},
                size_hint=(None, None),
                size=(400, 400)
            )
            gen = ["Male","Female"]
            n = MDLabel(
                text=f"Name : Doctor {i} \n\nGENDER : {random.choice(gen)} \n\nAge : {random.randint(30,50)}\n\nAreas of specialization : abc... \n\nExperience: {random.randint(5,15)} years",
                size_hint_y=None,
                theme_text_color=("Custom"),
                text_color=(0, 0, 0, 1),
                pos_hint={"right": 0.9, "center_y": 0.7},
                padding=(15, 10),
                bold=True
            )
            doct.add_widget(n)
            doct.add_widget(doc_photo)
            self.root.ids.list.add_widget(doct)

        self.change_screen("doctor_list")


    def reading(self):
        try:
            metadata, response = db.files_download("/test/dropbox.txt")
            content = response.content
            msg1 = content.decode('utf-8')
            letter2 = 1
            for letter3 in msg1:
                if letter3.isalpha() or letter3.isspace():
                    letter2 += 1
                if letter2 < 23:
                    height = 80
                if letter2 > 23:
                    height = (letter2) * 2
                if msg1:
                    msg2 = MDLabel(text=msg1, size_hint_y=None, theme_text_color=("Custom"), text_color=(1, 1, 1, 1),
                                   pos_hint={"center_x": .2, "center_y": 0.5}, padding=(15, 10))
                    current_time = datetime.now().strftime("%I : %M %p ")
                    current_time1 = MDLabel(text=current_time, theme_text_color="Secondary",
                                            pos_hint={"center_x": 1.4, "center_y": 0.4}, size_hint=(1, 1))
                    chat_box = self.root.ids.chat
                    chat1 = MDCard(
                        size_hint=(None, None),
                        size=(500, height),
                        elevation=4,
                        pos_hint={"left": .98, "center_y": 0.3},
                        md_bg_color=(66/255, 154/255, 227/255, 1),
                        radius=[30],
                        size_hint_y=None
                    )
                    chat1.add_widget(msg2)
                    chat_box.add_widget(chat1)
                    chat_box.add_widget(current_time1)
                    return msg1
                elif msg1 == "":
                    pass
        except dbx.exceptions.HttpError as e:
            pass
    def cancelreq(self):
        db.files_upload("_NoNe_".encode("utf-8"), "/requests/file.txt",mode=dbx.files.WriteMode("overwrite"))
        self.change_screen("choose1")

    def send(self, msg):
        msg = self.root.ids["message"].text
        letter1 = 1
        for letter in msg:
            if letter.isalpha() or letter.isspace():
                letter1 += 1
            if letter1 < 23:
                height = 80
            if letter1 > 23:
                height = (letter1) * 2
        if msg:
            msg1 = MDLabel(text=msg, size_hint_y=None, theme_text_color=("Custom"), text_color=(1, 1, 1, 1),
                           pos_hint={"center_x": .2, "center_y": 0.5}, padding=(15, 10))
            current_time = datetime.now().strftime("%I : %M %p ")
            current_time1 = MDLabel(text=current_time, theme_text_color="Secondary",
                                    pos_hint={"center_x": 1.4, "center_y": 0.4}, size_hint=(1, 1))
            chat_box = self.root.ids.chat
            chat1 = MDCard(
                size_hint=(None, None),
                size=(500, height),
                elevation=4,
                pos_hint={"right": .98, "center_y": 0.3},
                md_bg_color=(66/255, 154/255, 227/255, 1),
                radius=[30],
                size_hint_y=None
            )
            chat1.add_widget(msg1)
            chat_box.add_widget(chat1)
            chat_box.add_widget(current_time1)

            try:
                new_content = msg
                db.files_upload(new_content.encode('utf-8'), "/test/dropbox.txt", mode=dbx.files.WriteMode('overwrite'))
                self.root.ids["message"].text = ""
            except dbx.exceptions.HttpError as e:
                pass

        elif msg == "":
            pass 
    def request(self):
        self.change_screen("wait")
        try:
                req = "ReQuEsT"                
                db.files_upload(req.encode('utf-8'), "/request/dropbox.txt", mode=dbx.files.WriteMode('overwrite'))
                
        except dbx.exceptions.HttpError as e:
         	pass
        try:
                while True:
                	metadata, response = db.files_download("/request/dropbox.txt")
                	content2 = response.content
                	msg1 = content2.decode('utf-8')
                	if msg1 =="AcCpEt":
                		self.change_screen("chat_room")
                		read = th.Thread(target=self.reading(),args=(self,))
                		read.start()
                		break
                	else:
                		pass
        except:
        	pass
    def save(self):
        name = self.root.ids["name"].text
        phone= self.root.ids["phone"].text
        address = self.root.ids["address"].text
        pin = self.root.ids["pin"].text
        medicine = self.root.ids["medicine name"].text
        if name and phone and address and pin and medicine:
            pass
        else:
            self.root.ids.screen.current = "error"
            sleep(5)
            self.root.ids.screen.current = "medicine"
        dict = {}
        dict["name"] = name
        dict["phone"] = phone
        dict["address"] = address
        dict["pincode"] = pin
        dict["medicine"] = medicine
        with open("medicine.txt","wt") as file:
            for key,value in dict.items():
                file.write(f"{key} : {value}\n")
        	           
MyApp().run() 