from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from CreditScore.models import Farmer, Farm, Finance, Weather, SocialInteraction, PsychometricAssessment, \
    QuestionCategory, QuestionType, QuestionAnswer


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = (
        'Surname', 'MiddleNames', 'LastName', 'NationalIDNumber', 'TelephoneNumber', 'TelephoneServiceProvider',
        'PermanentPhysicalAddress', 'Gender', 'LevelOfEducation', 'HasDisability', 'MaritalStatus', 'FarmerAge',
        'Guarantor', 'GuarantorTelephoneAddress', 'GuarantorIDNumber')


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ('FarmOwnershipType', 'FarmSize', 'MainCropPastureGrown', 'EstimateYieldPerSeason', 'CropsGrownFor',
                  'MainLivesockBreed', 'GPS', 'County')


class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = ('MainSourceOfFinance', 'TakingInsurance', 'GrossIncomePerMonth', 'Derogatory', 'CollectionCount',
                  'DeclaredBanruptcy', 'InquiresCount06', 'InquiriesTimeLast', 'InquiriesFinanceCnt24',
                  'TermLoanTimeFirst', 'TermLoanTimeLast', 'TermLoanCnt03', 'TermLoanCnt12', 'TermLoanCnt24',
                  'TermsLoanCnt', 'TermLoanSum', 'TermLoanMaxSum', 'TermLoanSatCnt', 'TermLoanDel60Cnt',
                  'TermLoanBadCnt24', 'TermLoan75UtilCnt', 'TermLoan50UtilCnt', 'TermLoanBalance', 'TermLoanSatPct',
                  'TermLoanDel3060Cnt24', 'TermLoanDel90Cnt24', 'TermLoanDel60CntAll', 'TermLoanOpenPct',
                  'TermLoanBadDerogCnt', 'TermLoanDel60Cnt24', 'TermLoanOpen24Pct')


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = (
        'MinAnnualRainfall', 'MaxAnnualRainfall', 'AnnualRainfall', 'MaxAnnualTemperature', 'MinAnnualTemperature',
        'MaxAnnualRelativeHumidity', 'MinAnnualRelativeHumidity', 'MinWindSpeed', 'MaxWindSpeed', 'FarmLevelMaxNDVI',
        'FarmLevelMinNDVI')


class SocialInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialInteraction
        fields = ('MembershipToGroups', 'ProjectsRunBy')


class PsychometricAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychometricAssessment
        fields = (
        'CropsGrownForSale', 'ScaredOfInsects', 'GoodAtPlanning', 'GoodAtSaving', 'MakingMoneyToMeIsLessImportant',
        'NoRegretInFailure', 'ComfortableTakingRisk', 'LoveGrowingPlants', 'preferGrowingCrops')


class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = ('Id', 'Name',)


class QuestionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionType
        fields = ('Id', 'Name', 'CategoryId')


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = ('Id', 'Name', 'Score', 'TypeId', 'CategoryId')
