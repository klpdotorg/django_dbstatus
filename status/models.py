from django.db import models


class SchoolsInBoundary(models.Model):
    class Meta(object):
        db_table =  "tb_boundary_schoolcount"
    count = models.IntegerField()


class StudentsInBoundary(models.Model):
    class Meta(object):
        db_table =  "tb_boundary_studentcount"
    scount = models.IntegerField()
    stucount = models.IntegerField()


class AssessmentCountInBoundary(models.Model):
    class Meta(object):
        db_table =  "tb_boundary_assessmentcount"
    progname = models.CharField(max_length=300)
    assessname = models.CharField(max_length=300)
    school_mapped_count = models.IntegerField()
    school_assess_count = models.IntegerField()
    student_assess_count = models.IntegerField()


class StudentsInSchool(models.Model):
    class Meta(object):
        db_table =  "tb_schoolstudentcount"
    studentcount = models.IntegerField()


class StudentsInClass(models.Model):
    class Meta(object):
        db_table =  "tb_classstudentcount"
    sid = models.IntegerField()
    klass = models.CharField(max_length=20, blank=True, null=True)
    section = models.CharField(max_length=10)
    studentcount = models.IntegerField(blank=True, null=True)


class CurrentPrograms(models.Model):
    class Meta(object):
        db_table =  "tb_currentprograms"
    progname = models.CharField(max_length=300)

    
class SchoolAssessments(models.Model):
    class Meta(object):
        db_table =  "tb_schoolassessmentcount"
    progname = models.CharField(max_length=300)
    assessname = models.CharField(max_length=300)
    student_assess_count = models.IntegerField(null=True, blank=True)


class ClassAssessments(models.Model):
    class Meta(object):
        db_table =  "tb_classassessmentcount"
    sid = models.IntegerField()
    klass = models.CharField(max_length=20, null=True)
    section = models.CharField(max_length=10, null=True)
    progname = models.CharField(max_length=300)
    assessname = models.CharField(max_length=300)
    student_assess_count = models.IntegerField()


class StatusInfo(models.Model):
    class Meta(object):
        db_table =  "tb_statusinfo"
    updatedtime = models.DateTimeField()

# 
# CREATE OR REPLACE VIEW vw_boundary as
#        select * from dblink('host=localhost dbname=klp_production user=klprepl password=password', 'select * from schools_boundary')
#        as t1 (id integer,
#               parent_id integer,
#               name varchar(300),
#               boundary_category_id integer,
#               boundary_type_id integer,
#               active integer);
# 
# CREATE OR REPLACE VIEW vw_school as
#        select * from dblink('host=localhost dbname=klp_production user=klprepl password=password', 'select id,boundary_id,name,cat_id from schools_institution')
#        as t1 (id integer,
#               boundary_id integer,
#               name varchar(300),
#               cat_id integer);
# 
# CREATE OR REPLACE VIEW vw_sslc_sch_agg as
#        select * from dblink('host=localhost dbname=sslc_dataagg user=klp password=password','select dist.dist_name,agg.ayid,agg.is_govt,agg.moi,agg.sch_count,agg.tot_stu_count,agg.pass_stu_count from tb_sslc_sch_agg agg,tb_district dist where agg.dist_code=dist.dist_code and agg.ayid=102')
#        as t1 (district varchar(32),
#               ayid integer,
#               is_govt varchar(3),
#               moi varchar(3),
#               sch_count integer,
#               tot_stu_count integer,
#               pass_stu_count integer);
# 
# 
