from flask import Blueprint, render_template, redirect, url_for, request, flash, g, session
from flask_login import current_user
from .models import Community
from . import db
import sqlite3



community = Blueprint('community', __name__)

@community.route('/create_community', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        
    	# If not logged in, flash message
        if current_user.get_id() is None:
            flash('You must be logged in to create a community!')
            return redirect(url_for('community.create'))
            
        community_name = request.form.get('community_name')
        nsfw_flag = request.form.get('nsfw_flag')
        if nsfw_flag == "on":
            nsfw_flag = 1
        new_community = Community(community_name=community_name, nsfw_flag=nsfw_flag)
        
        db.session.add(new_community)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('create_community.html')

@community.route('/view_community', methods=['GET'])
def view_community():
    community_id = request.args.get('community_id')
    community = Community.query.filter_by(community_id=community_id).first()
    g.db = sqlite3.connect("redidit/db.sqlite")
    cur = g.db.execute(("SELECT * FROM post WHERE community_id=? LIMIT 5"), [community_id])
    posts = [dict(id=row[0], title=row[7], body=row[1], upvotes=row[2], downvotes=row[3],
        author=row[4], creation_datetime=row[5], nsfw_flag=row[6], community_id=row[8])
        for row in cur.fetchall()]
    g.db.close()
    return render_template('community.html', community=community, posts=posts)