from django.db import models


# Create your models here.


class Farmer(models.Model):
    Surname = models.CharField(max_length=500)
    MiddleNames = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    NationalIDNumber = models.IntegerField()
    TelephoneNumber = models.IntegerField()
    TelephoneServiceProvider = models.CharField(max_length=500)
    PermanentPhysicalAddress = models.CharField(max_length=500)
    Gender = models.CharField(max_length=500)
    LevelOfEducation = models.CharField(max_length=500)
    HasDisability = models.CharField(max_length=500)
    MaritalStatus = models.CharField(max_length=500)
    FarmerAge = models.CharField(max_length=500)
    Guarantor = models.CharField(max_length=500)
    GuarantorTelephoneAddress = models.IntegerField()
    GuarantorIDNumber = models.IntegerField()

    def __str__(self):
        return Surname


class Farm(models.Model):
    FarmOwnershipType = models.CharField(max_length=500)
    FarmSize = models.CharField(max_length=500)
    MainCropPastureGrown = models.CharField(max_length=500)
    EstimateYieldPerSeason = models.CharField(max_length=500)
    CropsGrownFor = models.CharField(max_length=500)
    MainLivesockBreed = models.CharField(max_length=500)
    GPS = models.CharField(max_length=500)
    County = models.CharField(max_length=500)


class Finance(models.Model):
    MainSourceOfFinance = models.CharField(max_length=500)
    TakingInsurance = models.CharField(max_length=500)
    GrossIncomePerMonth = models.CharField(max_length=500)
    Derogatory = models.CharField(max_length=500)
    CollectionCount = models.CharField(max_length=500)
    DeclaredBanruptcy = models.CharField(max_length=500)
    InquiresCount06 = models.CharField(max_length=500)
    InquiriesTimeLast = models.CharField(max_length=500)
    InquiriesFinanceCnt24 = models.CharField(max_length=500)
    TermLoanTimeFirst = models.CharField(max_length=500)
    TermLoanTimeLast = models.CharField(max_length=500)
    TermLoanCnt03 = models.CharField(max_length=500)
    TermLoanCnt12 = models.CharField(max_length=500)
    TermLoanCnt24 = models.CharField(max_length=500)
    TermsLoanCnt = models.CharField(max_length=500)
    TermLoanSum = models.CharField(max_length=500)
    TermLoanMaxSum = models.CharField(max_length=500)
    TermLoanSatCnt = models.CharField(max_length=500)
    TermLoanDel60Cnt = models.CharField(max_length=500)
    TermLoanBadCnt24 = models.CharField(max_length=500)
    TermLoan75UtilCnt = models.CharField(max_length=500)
    TermLoan50UtilCnt = models.CharField(max_length=500)
    TermLoanBalance = models.CharField(max_length=500)
    TermLoanSatPct = models.CharField(max_length=500)
    TermLoanDel3060Cnt24 = models.CharField(max_length=500)
    TermLoanDel90Cnt24 = models.CharField(max_length=500)
    TermLoanDel60CntAll = models.CharField(max_length=500)
    TermLoanOpenPct = models.CharField(max_length=500)
    TermLoanBadDerogCnt = models.CharField(max_length=500)
    TermLoanDel60Cnt24 = models.CharField(max_length=500)
    TermLoanOpen24Pct = models.CharField(max_length=500)


class Weather(models.Model):
    MinAnnualRainfall = models.CharField(max_length=500)
    MaxAnnualRainfall = models.CharField(max_length=500)
    AnnualRainfall = models.CharField(max_length=500)
    MaxAnnualTemperature = models.CharField(max_length=500)
    MinAnnualTemperature = models.CharField(max_length=500)
    MaxAnnualRelativeHumidity = models.CharField(max_length=500)
    MinAnnualRelativeHumidity = models.CharField(max_length=500)
    MinWindSpeed = models.CharField(max_length=500)
    MaxWindSpeed = models.CharField(max_length=500)
    FarmLevelMaxNDVI = models.CharField(max_length=500)
    FarmLevelMinNDVI = models.CharField(max_length=500)


class SocialInteraction(models.Model):
    MembershipToGroups = models.CharField(max_length=500)
    ProjectsRunBy = models.CharField(max_length=500)


class PsychometricAssessment(models.Model):
    CropsGrownForSale = models.CharField(max_length=500)
    ScaredOfInsects = models.CharField(max_length=500)
    GoodAtPlanning = models.CharField(max_length=500)
    GoodAtSaving = models.CharField(max_length=500)
    MakingMoneyToMeIsLessImportant = models.CharField(max_length=500)
    NoRegretInFailure = models.CharField(max_length=500)
    ComfortableTakingRisk = models.CharField(max_length=500)
    LoveGrowingPlants = models.CharField(max_length=500)
    preferGrowingCrops = models.CharField(max_length=500)


class QuestionCategory(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=500)

    def __str__(self):
        return self.Name


class QuestionType(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=500)
    CategoryId = models.IntegerField()

    def __str__(self):
        return f"{self.Name} -id: {self.Id}"


class QuestionAnswer(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=500)
    Score = models.IntegerField(default=0)
    TypeId = models.IntegerField()
    CategoryId = models.IntegerField()