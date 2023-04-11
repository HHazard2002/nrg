from django.urls import path
from . import views
from api.views import *

urlpatterns = [
    
  path('', views.getRoutes),

  path('add4000/', views.add4000),
  path('electricityPrices/', views.getElectricityPrices),
  path('nrgPrices/', views.getNRGPrices),
    
  path('max/', views.max, name='max'),
  path('max2/', views.max2),
  path('galeShapley/', views.gale_shapley),
  path('new_gurobi/', views.new_gurobi),
  path('new_stable/', views.stableMariageBetter),

  path('transferEnergy2/', views.transferEnergy2),
  path('stableMariage2/', views.stableMariage2),
  path('new_gurobi2/', views.new_gurobi2),
  
  path('account/', ListAccounts.as_view()),
  path('objects/', ListObjects.as_view()), 
  path('modifyObject/', views.modifyObjects),

  # Account/Registration
  path('changeProfileDetails/', views.changeProfileDetails),
  path('createAccount/', views.createAccount),
  path('updateAccount/', views.updateAccount),
  path('register/', views.registration),
  path('login/', views.login, name="login"),
  path('newUser/', views.registration_view),
  path('updateAccount2/', views.updateAccount2),
  path('deleteAccount/', views.deleteAccount),

  # Objects
  path('updateObject/', views.updateObject),
  path('getAccountObject/', views.getAccountObject),
  path('switchObjectState/', views.switchObjectState),
  path('deleteObject/', views.deleteObject),
  path('desactivateObject/', views.desactivateObject),
  path('createObject/', views.createObject),
  path('switch/', views.switchOn),
  path('getAccountObjects/', views.getAccountObjects),

  # Energy/Expenses/Data
  path('updateEnergy/', views.updateEnergy),
  path('objectData/', views.getObjectsData),
  path('weeklyObjectData/', views.getObjectsWeeklyData),
  path('objectExpenses/', views.getObjectsExpenses),
  path('weeklyObjectExpenses/', views.getObjectsWeeklyExpenses),
  path('weeklyEnergyMix/', views.getWeeklyEnergyMix),
  path('overallEnergyMix/', views.getOverallEnergyMix),
  path('dailyDataUpdates/', views.dailyDataUpdate),

  # Blockchain
  path('transferEnergy/', views.transferEnergy),
  path('stableMariage/', views.stableMariage),
  path('linearSolution/', views.linearSolution),
  path('gurobi/', views.gurobi),

  path('getTransactions/', views.getTransactions),
  path('createTransactions/', views.createTransactions),
  path('addTransactions/', views.addTransactions),
  path('storeTransactions/', views.storeTransactions),
  path('deleteAllTransactions/', views.deleteAllTransactions),

  path('getBalanceOf/<str:username>/', views.getBalanceOf),
  path('deployContract/', views.deploy_contract),
  path('transfer/', views.transfer),
  path('transferFrom/', views.transferFrom),

  # Test
  path('getBalanceOfTest/', views.getBalanceOfTest),

  # Not in use (To be checked)
  path('currConsuming/', views.getConsumingUsers),
  path('currProducing/', views.getProducingUsers),

  path('accounts/', views.getAccounts),
  path('account/', views.getAccount),

  path('modifyConsumption/', views.modifyConsumption),
  path('modifyProduction/', views.modifyProduction),

  #path('updateEnergy/', views.updateEnergy),
  path('getProducers/', views.getProducers),
  path('getConsumers/', views.getConsumers),
  path('getObjects/', views.getObjects),
]