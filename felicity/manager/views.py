from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from num2words import num2words
import json

from .models import  SelfInfo, Buyer, Invoice, Challan, Entry, ChallanEntry, User


# Create your views here.
@login_required(login_url='login')
def index(request):
    #invoices = Invoice.objects.all()
    invoices = Invoice.objects.all().order_by('-id')[:10:-1]
    challans = Challan.objects.all().order_by('-id')[:20:-1]
    return render(request, "index.html", {
        "invoices": invoices,
        "challans": challans,
    })     

@login_required(login_url='login')
def createInvoice(request):
    if request.method == "GET":
        buyers = Buyer.objects.all()
        return render(request, "newInvoice.html",{
            "buyers": buyers
        })
    
    elif request.method == "POST":
        data = request.body
        data = data.decode('utf-8')
        data = json.loads(data)
        #data = data.decode('utf-8')
        #data = json.loads(data)
        data = data["post_data"]
        #print(data['buyer'])
        if data['type'] == 'newInvoice':

            buyer = Buyer.objects.get(name=data['buyer'])
            seller = SelfInfo.objects.get(id=1)
            invoice = Invoice(
                seller = seller,
                buyer = buyer,
                date = data['date']
            )
            invoice.save()
            id=invoice.id
            return JsonResponse({'message': 'Data received', 'id': id},safe=False)
        elif data['type'] == 'newEntry':
            invoiceNum = Invoice.objects.get(id=data['invoicenum'])

            newEntry = Entry(
                invoicenum = invoiceNum,
                particulars = data['particular'],
                hsn = data['hsnnum'],
                shade = data['shade'],
                challan = data['challanNum'],
                prgnum = data['prgNum'],
                dyeType = data['dye'],
                qty = data['qty'],
                rate = data['rate'],
            )
            newEntry.save()
            return JsonResponse({'message': 'Data received'},safe=False)
    else:
        return JsonResponse({'error': 'Bad request'}, status=400)

@login_required(login_url='login')
def createChallan(request):
    if request.method == "GET":
        buyers = Buyer.objects.all()
        return render(request, "newChallan.html",{
            "buyers": buyers
        })
    elif request.method == "POST":
        data = request.body
        data = data.decode('utf-8')
        data = json.loads(data)
        #data = data.decode('utf-8')
        #data = json.loads(data)
        data = data["post_data"]
        #print(data['buyer'])
        if data['type'] == 'newChallan':

            buyer = Buyer.objects.get(name=data['buyer'])
            seller = SelfInfo.objects.get(id=1)
            challan = Challan(
                sender = seller,
                receiver = buyer,
                date = data['date']
            )
            challan.save()
            id=challan.id
            return JsonResponse({'message': 'Data received', 'id': id},safe=False)
        elif data['type'] == 'newChallanEntry':

            challanNum = Challan.objects.get(id=data['challanNum'])            
            newEntry = ChallanEntry(
                challanNum = challanNum,
                materialName = data['materialName'],
                shade = data['shade'],
                dyeingType = data['dye'],
                befQty = data['befQty'],
                aftQty = data['aftQty'],
                remark = data['remark'],
            )
            newEntry.save()
            return JsonResponse({'message': 'Data received'},safe=False)
    else:
        return JsonResponse({'error': 'Bad request'}, status=400)

@login_required(login_url='login')
def createBuyer(request):
    allBuyers = Buyer.objects.all()

    if request.method == "POST":
        
        flag = False
        for buyer in allBuyers:
            if buyer.gstin == request.POST["gstin"]:
                flag = True

        if not flag:
            newBuyer = Buyer(
                name = request.POST["name"],
                address = request.POST["address"],
                state = request.POST["state"],
                gstin = request.POST["gstin"]
            )
            newBuyer.save()
            allBuyers = Buyer.objects.all()
            return render(request, "createBuyer.html",{'buyers': allBuyers})
        else:
            return render(request, "createBuyer.html",{
                'buyers': allBuyers,
                'message': "Buyer Already Exists!"})
    else:
        return render(request, "createBuyer.html",{'buyers': allBuyers})
    
@login_required(login_url='login')
def invoice(request):
    if request.method == "GET":
        id = request.GET["id"]
        invoice = Invoice.objects.get(id=id)
        self = invoice.seller
        entries = Entry.objects.filter(invoicenum=id).values()
        self = SelfInfo.objects.get(name=self)
        buyer = Buyer.objects.get(invoiceBuyer=invoice)
        fields = []
        serialNum = 1
        totalQty = 0
        totalAmount = 0
        hsn = 0
        for entry in entries:
            hsn = entry['hsn']
            amount = entry['qty'] * entry['rate']
            entry = entry|{'amount': amount}
            entry = entry|{'serialNum': serialNum}
            fields += [entry]
            serialNum += 1
            totalQty += entry["qty"]
            totalAmount += entry["amount"]
        
        totalAmount = float("{:.2f}".format(totalAmount))
        gst = float("{:.2f}".format(totalAmount * 0.025))
        totalGst = gst * 2
        gstInWords = num2words(totalGst, to='currency', lang='en_IN', currency='INR').upper()
        roundedAmount = round(totalAmount + (gst * 2))
        roundAmount = roundedAmount - (totalAmount + (gst * 2))
        roundAmount = float("{:.2f}".format(roundAmount)) 
        amountInWords = num2words(float(roundedAmount), to='currency', lang='en_IN', currency='INR').upper()
        print(gstInWords)
        return render(request, 'invoice.html', {
            'invoice': invoice,
            'self': self,
            'buyer': buyer,
            'entries': fields,
            'totalAmount': totalAmount,
            'totalQty': totalQty,
            'roundedAmount': roundedAmount,
            'roundAmount':roundAmount,
            'amountInWords': amountInWords,
            'gst': gst,
            'hsn': hsn,
            'totalGst': totalGst,
            'gstInWords': gstInWords,
        })
    elif request.method == "POST":
        id = request.POST["deleteInvoice"]
        invoice = Invoice.objects.get(id=id)
        invoice.delete()
        return HttpResponseRedirect(reverse("index"))

    

@login_required(login_url='login')
def challan(request):
    if request.method == "GET":
        id = request.GET["id"]
        challan = Challan.objects.get(id=id)
        self = challan.sender
        entries = ChallanEntry.objects.filter(challanNum=id).values()
        self = SelfInfo.objects.get(name=self)
        receiver = Buyer.objects.get(challanReceiver=challan)
        fields = []
        serialNum = 1
        befQty = 0
        aftQty = 0
        for entry in entries:
            befQty += entry["befQty"]
            aftQty += entry["aftQty"]
            entry = entry|{'serialNum': serialNum}
            fields += [entry]
            serialNum += 1
        return render(request, 'challan.html', {
            'challan': challan,
            'self': self,
            'receiver': receiver,
            'entries': fields,
            'befQty': befQty,
            'aftQty': aftQty
        })
    elif request.method == "POST":
        id = request.POST["deleteChallan"]
        challan = Challan.objects.get(id=id)
        challan.delete()
        return HttpResponseRedirect(reverse("index"))
        

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))