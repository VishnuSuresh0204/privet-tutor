from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from datetime import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request,"index.html")

def studentreg(request):
    if request.POST:
        username=request.POST.get('username3') or request.POST.get('username8')
        email=request.POST.get('email3') or request.POST.get('email8')
        phonenumber=request.POST.get('phoneno3') or request.POST.get('phoneno8')
        password=request.POST.get('password3') or request.POST.get('password8')
        address=request.POST.get('address3') or request.POST.get('address8')
        
        if Login.objects.filter(username=email).exists():
            messages.info(request,"Already Have Registered")
        else:
            student=Login.objects.create_user(
                username=email,password=password,usertype='student',viewPassword=password,is_active=0)
            register=Student.objects.create(
                Username=username,Email=email,Phonenumber=phonenumber,Password=password,Address=address,student=student)
            register.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"studentreg.html")

def login(request):
    if request.POST:
        Email1=request.POST['email2']
        Password1=request.POST['password2']
        user=authenticate(username=Email1,password=Password1)
        if user is not None:
            if user.usertype=="admin":
                messages.info(request,"Welcome To The Admin Page")
                return redirect("/adminhome")
            elif user.usertype=="student":
                request.session['uid']=user.id
                request.session['email']=user.email
                messages.info(request,"Welcome To The Student Page")
                return redirect("/studenthome")
            elif user.usertype=="teacher":
                request.session['uid']=user.id
                request.session['email']=user.email
                request.session['type']=user.usertype
                messages.info(request,"Welcome To The Tutor Page")
                return redirect("/tutorhome")
            else:
                messages.info(request,"Invalid Username Or Password")
                return redirect("/login")
    return render(request,"login.html")

def adminhome(request):
    return render(request,"Admin/adminhome.html")

def studenthome(request):
    return render(request,"Student/studenthome.html")

def tutorhome(request):
    return render(request,"Tutor/tutorhome.html")

def addtutor(request):
    if request.POST:
        Username10=request.POST['username4']
        Email10=request.POST['email4']
        Password10=request.POST['password4']
        Subject10=request.POST['subject']
        image10=request.FILES['image4']
        Location10=request.POST['location']
        Fee10=request.POST['fee']
        if Login.objects.filter(username=Email10).exists():
            messages.info(request,"Already Have Registered")
        else:
            teacher=Login.objects.create_user(
            username=Email10,password=Password10,usertype='teacher',viewPassword=Password10)
            register3=Teacher3.objects.create(
            username5=Username10,email5=Email10,password5=Password10,image5=image10,subject5=Subject10,location5=Location10,fee=Fee10,teacher=teacher)
            register3.save()
            messages.info(request,"Successfully")
            return redirect("/viewtutorad")
    return render(request,"Admin/addtutor.html")

def viewtutor_ad(request):
    data=Teacher3.objects.all()
    return render(request,"Admin/viewtutor_ad.html",{"data":data})

def deletetutor(request):
    id=request.GET['id']
    t=Teacher3.objects.filter(id=id)        
    t.delete()
    messages.info(request,"Tutor Deleted Successfully")
    return redirect("/viewtutorad")

def viewstudent_ad(request):
    data=Student.objects.all()
    return render(request,"Admin/viewstudent_ad.html",{"data":data})

def deletestudent_ad(request):
    id=request.GET['id']
    Student.objects.filter(id=id).delete()
    messages.info(request,"Student Deleted Successfully")
    return redirect("/viewstudent_ad")

def Approve_student(request):
    status=request.GET['status']
    id=request.GET['id']
    wo=Login.objects.get(id=id)
    wo.is_active=int(status)
    wo.save()
    if status == '1':
        messages.info(request," Approved successfully")
    else:
        Login.objects.filter(id=id).delete()
        messages.info(request," Rejected successfully")
    return redirect("/viewstudent_ad")

def addbook(request):
    if request.POST:
        subject=request.POST['subject8']
        bookname=request.POST['bookname1']
        image=request.FILES['image1']
        description=request.POST['description1'] 
        link=request.POST['link']
        data=Book.objects.create(subject1=subject,link=link,Bookname=bookname,Image=image,Description=description)
        data.save()
        messages.info(request,"Book Added successfully")
        return redirect("/viewbookad")
    return render(request,"Admin/addebooks.html")

def viewbook_ad(request):
    data=Book.objects.all()
    return render(request,"Admin/viewbook_ad.html",{"data":data})

def viewbook_stu(request):
    data=Book.objects.all()
    return render(request,"Student/viewebook_stu.html",{"data":data})

def book_delete(request):
    id=request.GET['id']
    Book.objects.filter(id=id).delete()
    messages.info(request,"Book Deleted Successfully")
    return redirect("/viewbookad")

def edit_book(request):
    id = request.GET.get('id')
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        subject = request.POST['subject8']
        bookname = request.POST['bookname1']
        description = request.POST['description1']
        link = request.POST['link']
        
        book.subject1 = subject
        book.Bookname = bookname
        book.Description = description
        book.link = link
        
        if 'image1' in request.FILES:
            book.Image = request.FILES['image1']
            
        book.save()
        messages.info(request, "Book Updated Successfully")
        return redirect("/viewbookad")
        
    return render(request, "Admin/editbook.html", {"book": book})

#def viewparent(request):
#    data=Parent.objects.all()
#    return render(request,"Tutor/viewparents.html",{"data":data})

def actionstudent(request):
    id=request.GET['id']
    d=Student.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewstudent_ad")

def deletestudent(request):
    id=request.GET.get('id')
    bbb=Student.objects.filter(id=id).delete()
    bao=Login.objects.filter(id=id).delete()
    messages.info(request,"deleted successfully")
    return redirect("/viewstudent_ad")

def viewtutor_pa(request):
    data=Teacher3.objects.all()
    return render(request,"Student/viewtutor_stu.html",{"data":data})

def addreview(request):
    uid = request.session['uid']
    student = Student.objects.get(student=uid)
    tutor_id=request.GET.get('id')
   # id=request.GET.get('id')
   # teacher=Teacher3.objects.get(id=id)
    # tutor_data = Teacher3.objects.all() 
    if request.POST:
        rating = request.POST.get('rating1')
        review = request.POST.get('review1')
        # tutor_id = request.POST['tutors']
        teacher = get_object_or_404(Teacher3, id=tutor_id)
        if rating and review:
            review = Review.objects.create(rating=rating, review=review, teacher=teacher, student=student)  
            review.save()
            messages.info(request,"Review Added successfully")
            teacher.reviews_count = Review.objects.filter(teacher=teacher).count()

            total_ratings = sum(review.rating for review in Review.objects.filter(teacher=teacher))
            teacher.average_rating = total_ratings / teacher.reviews_count if teacher.reviews_count > 0 else 0

            teacher.save()
    return render(request, "Student/addreview_tutor.html")

def calculate_average_rating(reviews):
    if not reviews:
        return 0
    total_ratings = sum(review.rating for review in reviews)
    return total_ratings/len(reviews)

def deletereview(request):
    id=request.GET['id']
    o=Review.objects.filter(id=id)        
    o.delete()
    messages.info(request,"Review Deleted Successfully")
    return redirect("/viewreview")

def viewreview_tutor(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    data=Review.objects.filter(teacher=teacher)
    return render(request,"Tutor/viewreview.html",{"data":data})

def addbooking_tutor(request):
    tid=request.GET.get('id')
    teacher=Teacher3.objects.get(id=tid)
    uid=request.session['uid']
    student=Student.objects.get(student=uid)
    if request.method == 'POST':
        booking_type2 = request.POST.get('booking')
        booking_time2 = request.POST.get('time')
        booking = Booking1(booking_type1=booking_type2, booking_time1=booking_time2,student=student,teacher=teacher)
        booking.save()
        messages.info(request,"Book Tutor successfully")
        return redirect("/viewbooking_pa")
    return render(request,"Student/bookingtutor.html")

def viewbooking_tutor(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    data=Booking1.objects.filter(teacher=teacher)
    
    # Enrich data with notes status
    enriched_data = []
    for booking in data:
        booking.has_notes = Note.objects.filter(booking=booking).exists()
        enriched_data.append(booking)
        
    return render(request,"Tutor/viewbookingtutor.html",{"data":enriched_data})

def viewbooking_student(request):
    uid=request.session['uid']
    student = Student.objects.get(student=uid)
    data=Booking1.objects.filter(student=student)
    
    # Enrich data with paid/reviewed status
    enriched_data = []
    for booking in data:
        r = Review.objects.filter(booking=booking).first()
        booking.has_review = r is not None
        booking.review_id = r.id if r else None
        booking.has_paid = Payment.objects.filter(student=student, teacher=booking.teacher, status="paid").exists()
        booking.has_notes = Note.objects.filter(booking=booking).exists()
        enriched_data.append(booking)
        
    return render(request,"Student/viewbookingtutor1.html",{"data":enriched_data})

def actionbooking(request):
    id=request.GET['id']
    n=Booking1.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewbooking")

def deletebooking(request):
    id=request.GET.get('id')
    mbn=Booking1.objects.filter(id=id).delete()
    mnb=Login.objects.filter(id=id).delete()
    messages.info(request,"deleted successfully")
    return redirect("/viewbooking")

def booking_tutor_st(request):
    tid=request.GET.get('id')
    teacher=Teacher3.objects.get(id=tid)
    uid=request.session['uid']
    student=Student.objects.get(student=uid)
    if request.method == 'POST':
        booking_type3 = request.POST.get('booking1')
        booking_time3 = request.POST.get('time1')
        booking1 = Booking1(booking_type1=booking_type3, booking_time1=booking_time3,student=student,teacher=teacher)
        booking1.save()
        messages.info(request,"Book Tutor successfully")
        return redirect("/viewbooking_st")
    return render(request,"Student/bookingtutor_st.html")


def select_tutor(request):
    data=Teacher3.objects.all()
    return render(request,"Student/selecttutor.html",{"data":data})

def viewbooking_stu(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    data=Booking1.objects.filter(teacher=teacher)
    
    # Enrich data with notes status
    enriched_data = []
    for booking in data:
        booking.has_notes = Note.objects.filter(booking=booking).exists()
        enriched_data.append(booking)
        
    return render(request,"Tutor/viewbooking_stu.html",{"data":enriched_data})

def actionbooking_st(request):
    id=request.GET['id']
    i=Booking1.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewbookingst")

def deletebooking_st(request):
    id=request.GET.get('id')
    mpn=Booking1.objects.filter(id=id).delete()
    mpb=Login.objects.filter(id=id).delete()
    messages.info(request,"deleted successfully")
    return redirect("/viewbookingst")

def request_democlass(request):
    id=request.GET.get("id")
    Booking1.objects.filter(id=id).update(status='Request_demo')
    messages.info(request,"Request demo class Successfully")
    return redirect("/viewbooking_stu")

def request_democlass_st(request):
    id=request.GET.get("id")
    j=Booking1.objects.filter(id=id).update(status='Request_demo')
    messages.info(request,"Request demo class Successfully")
    return redirect("/viewbooking_st")

def addrequest_demo(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    vid=request.GET.get('id')
    booking=Booking1.objects.get(id=vid)
    if request.method == 'POST':
        video1 = request.FILES['video']
        requestdemo = Requestdemo(Video=video1,teacher=teacher,booking=booking)
        requestdemo.save()
        Booking1.objects.filter(id=vid).update(status='Uploaded')
        messages.info(request,"class uploaded successfully")
        return redirect('/viewbooking')
    return render(request,"Tutor/requestdemo.html")

def viewrequest_demo(request):
    id=request.GET.get('id')
    b=Booking1.objects.get(id=id)
    data=Requestdemo.objects.filter(booking=b)
    return render(request,"Student/viewrequestdemo.html",{"data":data})

def add_notes(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    bid=request.GET.get('id')
    booking=Booking1.objects.get(id=bid)
    if request.method == 'POST':
        note_file = request.FILES['notes']
        note = Note(booking=booking, NoteFile=note_file, teacher=teacher, student=booking.student)
        note.save()
        messages.info(request,"Notes uploaded successfully")
        return redirect('/viewbookingst')
    return render(request,"Tutor/add_notes.html",{"booking":booking})

def view_notes_stu(request):
    bid=request.GET.get('id')
    booking=Booking1.objects.get(id=bid)
    data=Note.objects.filter(booking=booking)
    return render(request,"Student/view_notes_stu.html",{"data":data, "booking":booking})

def view_notes_tutor(request):
    bid=request.GET.get('id')
    booking=Booking1.objects.get(id=bid)
    data=Note.objects.filter(booking=booking)
    return render(request,"Tutor/view_notes_tutor.html",{"data":data, "booking":booking})

def edit_note(request):
    nid = request.GET.get('id')
    note = Note.objects.get(id=nid)
    if request.method == 'POST':
        if 'notes' in request.FILES:
            note.NoteFile = request.FILES['notes']
            note.save()
            messages.info(request, "Note updated successfully")
            return redirect(f'/view_notes_tutor?id={note.booking.id}')
    return render(request, "Tutor/edit_note.html", {"note": note})

def delete_note(request):
    nid = request.GET.get('id')
    note = Note.objects.get(id=nid)
    bid = note.booking.id
    note.delete()
    messages.info(request, "Note deleted successfully")
    return redirect(f'/view_notes_tutor?id={bid}')

def viewrequest_demo_st(request):
    id=request.GET.get('id')
    b=Booking1.objects.get(id=id)
    data=Requestdemo.objects.filter(booking=b)
    return render(request,"Student/viewrequestdemo.html",{"data":data})

def viewprofile(request):
    uid=request.session['uid']
    data=Teacher3.objects.filter(teacher=uid)
    return render(request,"Tutor/viewprofile.html",{"data":data})

def studentchat(request):
    id = request.GET.get("id")
    remail = request.GET.get("email")
    uid_id = Teacher3.objects.get(id=id)
    semail = request.session.get("email")
    uid = request.session["uid"]
    student_id = Student.objects.get(student=uid)
    time = datetime.now().time()
    date = datetime.now().date()
    formatted_time = time.strftime("%I:%M %p")
    formatted_date = date.strftime("%B %d")

    chats = Message.objects.filter(sender=student_id,receiver=uid_id)

    if request.POST:
        message = request.POST["message"]
        sendMsg = Message.objects.create(
            message=message,
            date=formatted_date,
            time=formatted_time,
            type="student",
            sender=student_id,
            receiver=uid_id,
            senderemail=semail,
            reciveremail=remail,
        )
        sendMsg.save()
    return render(request, "Student/chat.html", {"chats": chats})


def teacherchat(request):
    pid = request.GET.get("id")
    print(pid)
    remail = request.GET.get("email")
    print(remail)
    student_id = Student.objects.get(id=pid)
    uid = request.session["uid"]
    Uidd = Teacher3.objects.get(teacher=uid)
    print("id", Uidd)
    semail = request.session["email"]
    type = request.session["type"]

    time = datetime.now().time()
    date = datetime.now().date()
    formatted_time = time.strftime("%I:%M %p")
    formatted_date = date.strftime("%B %d")

    chats = Message.objects.filter(sender=student_id,receiver=Uidd)

    if request.POST:
        message = request.POST["message"]

        sendMsg = Message.objects.create(
            message=message,
            date=formatted_date,
            time=formatted_time,
            type="teacher",
            sender=student_id,
            receiver=Uidd,
            senderemail=semail,
            reciveremail=remail,
        )
        sendMsg.save()
    return render(request, "Tutor/chat.html", {"chats": chats})

def addreview_student(request):
    uid = request.session['uid']
    student = Student.objects.get(student=uid)
    booking_id = request.GET.get('booking_id')
    booking = get_object_or_404(Booking1, id=booking_id)
    
    # Check if review already exists for this booking
    if Review.objects.filter(booking=booking).exists():
        messages.info(request, "You have already submitted feedback for this booking.")
        return redirect("/viewreview_stu")
        
    if request.POST:
        rating = request.POST.get('rating1')
        review_text = request.POST.get('review1')
        teacher = booking.teacher
        
        if rating and review_text:
            new_review = Review.objects.create(
                rating=rating, 
                review=review_text, 
                teacher=teacher, 
                student=student,
                booking=booking
            )  
            new_review.save()
            
            # Update teacher stats
            teacher.reviews_count = Review.objects.filter(teacher=teacher).count()
            total_ratings = sum(r.rating for r in Review.objects.filter(teacher=teacher))
            teacher.average_rating = total_ratings / teacher.reviews_count if teacher.reviews_count > 0 else 0
            teacher.save()
            
            messages.info(request,"Review Added successfully")
            return redirect("/viewreview_stu")
            
    return render(request, "Student/rate_tutor.html", {"booking": booking})

def edit_review_student(request):
    review_id = request.GET.get('id')
    review_obj = get_object_or_404(Review, id=review_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating1')
        review_text = request.POST.get('review1')
        
        review_obj.rating = rating
        review_obj.review = review_text
        review_obj.save()
        
        # Recalculate teacher stats
        teacher = review_obj.teacher
        teacher.reviews_count = Review.objects.filter(teacher=teacher).count()
        total_ratings = sum(r.rating for r in Review.objects.filter(teacher=teacher))
        teacher.average_rating = total_ratings / teacher.reviews_count if teacher.reviews_count > 0 else 0
        teacher.save()
        
        messages.info(request, "Review Updated Successfully")
        return redirect("/viewreview_stu")
        
    return render(request, "Student/rate_tutor.html", {"review": review_obj, "edit_mode": True})

def delete_review_student(request):
    review_id = request.GET.get('id')
    review_obj = get_object_or_404(Review, id=review_id)
    teacher = review_obj.teacher
    review_obj.delete()
    
    # Recalculate teacher stats
    teacher.reviews_count = Review.objects.filter(teacher=teacher).count()
    total_ratings = sum(r.rating for r in Review.objects.filter(teacher=teacher))
    teacher.average_rating = total_ratings / teacher.reviews_count if teacher.reviews_count > 0 else 0
    teacher.save()
    
    messages.info(request, "Review Deleted Successfully")
    return redirect("/viewreview_stu")

def calculate_average_rating(reviews):
    if not reviews:
        return 0
    total_ratings = sum(review.rating for review in reviews)
    return total_ratings/len(reviews)

def view_review_student(request):
    uid=request.session["uid"]
    data=Review.objects.filter(student__student=uid)
    return render(request,'Student/viewreview_stu.html',{'data':data})

def addpayment_student(request):
    uid = request.session['uid']
    student = Student.objects.get(student=uid)
    teacher_id = request.GET.get("id")
    teacher = get_object_or_404(Teacher3, id=teacher_id)
    
    # Check if already paid for this teacher
    if Payment.objects.filter(student=student, teacher=teacher, status="paid").exists():
        messages.info(request, "You have already paid for this tutor.")
        return redirect("/viewbooking_stu")
        
    if request.method == 'POST':
        payment = Payment(student=student, teacher=teacher, status="paid")
        payment.save()
        messages.info(request, "Payment successful")
        return redirect("/viewbooking_stu")
    return render(request, "Student/addpayment.html", {"teacher": teacher})

def viewpayment_ad(request):
    data=Payment.objects.all()
    return render(request,"Admin/viewpayment_ad.html",{"data":data})



  


