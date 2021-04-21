from django.db import models
from choices.views import get_choices

#Domains for choices and db contstraints
class Status(models.TextChoices): #AOML, not Argo compliant
    ESTIMATED = 'estimated','estimated'
    AS_RECORDED = 'as recorded','as recorded'
    UNKNOWN = 'unknown','unknown'

class DeploymentType(models.TextChoices): #AOML, not Argo compliant
    RV = 'R/V','R/V'
    VOS = 'VOS','VOS'
    MV = 'M/V','M/V'


Instrument_Choices = get_choices('instrument_types')
Platform_Maker_Choices = get_choices('platform_makers')
Platform_Types_Choices = get_choices('platform_types')
Transmission_Systems_Choices = get_choices('transmission_systems')

class deployment(models.Model):
    # fields of the database
    ADD_DATE = models.DateTimeField() #creation of record in db
    AOML_ID = models.CharField(max_length=25, blank=True, null=True)
    PLATFORM_NUMBER = models.CharField(max_length=25, unique=True, blank=True, null=True) #WMO
    FLOAT_SERIAL_NO = models.IntegerField(blank=True, null=True)
    PLATFORM_MAKER = models.CharField(choices=Platform_Maker_Choices, max_length=25, blank=True, null=True)
    PLATFORM_TYPE = models.CharField(choices=Platform_Types_Choices, max_length=25, blank=True, null=True)
    INST_TYPE = models.CharField(max_length=25, blank=True, null=True)
    WMO_INST_TYPE = models.CharField(choices=Instrument_Choices, max_length=25, blank=True, null=True)
    WMO_RECORDER_TYPE = models.CharField(max_length=25, blank=True, null=True)

    PTT = models.CharField(max_length=25, blank=True, null=True)
    TRANS_SYSTEM = models.CharField(choices=Transmission_Systems_Choices, max_length=25, blank=True, null=True)
    IRIDIUM_PROGRAM_NO = models.CharField(max_length=25, blank=True, null=True)

    START_DATE = models.DateTimeField(blank=True, null=True)
    START_DATE_QC = models.CharField(max_length=25, choices=Status.choices, default=Status.ESTIMATED, blank=True, null=True)
    
    LAUNCH_DATE = models.DateTimeField(blank=True, null=True)
    LAUNCH_DATE_QC = models.CharField(max_length=25, choices=Status.choices, default=Status.ESTIMATED, blank=True, null=True)
    LAUNCH_LATITUDE = models.FloatField(blank=True, null=True) #WGS84 decimal degrees
    LAUNCH_LONGITUDE = models.FloatField(blank=True, null=True) #WGS84 decimal degrees
    LAUNCH_POSITION_QC = models.CharField(max_length=25, choices=Status.choices, default=Status.ESTIMATED, blank=True, null=True)

    PROJECT_NAME = models.CharField(max_length=25, blank=True, null=True)
    PI_NAME  = models.CharField(max_length=100, blank=True, null=True)
    PI_ADDRESS = models.CharField(max_length=100, blank=True, null=True)
    ORIGIN_COUNTRY = models.CharField(max_length=25, blank=True, null=True)

    DEPLOYER = models.CharField(max_length=25, blank=True, null=True)
    DEPLOYER_ADDRESS = models.CharField(max_length=100, blank=True, null=True)
    DEPLOYMENT_TYPE = models.CharField(choices=DeploymentType.choices, max_length=25, blank=True, null=True)
    DEPLOYMENT_PLATFORM = models.CharField(max_length=25, blank=True, null=True)
    DEPLOYMENT_CRUISE_ID = models.CharField(max_length=25, blank=True, null=True)
    DEPLOYMENT_REFERENCE_STATION_ID = models.CharField(max_length=25, blank=True, null=True)
    DEPLOYMENT_PLATFORM_ID = models.CharField(max_length=25, blank=True, null=True)
    

    ROM_VERSION = models.CharField(max_length=25, blank=True, null=True)

    BATTERY_TYPE = models.CharField(max_length=25, blank=True, null=True)
    BATTERY_MANUFACTURER = models.CharField(max_length=25, blank=True, null=True)
    BATTERY_MODEL = models.CharField(max_length=25, blank=True, null=True)
    BATTERY_SERIAL_NO = models.CharField(max_length=25, blank=True, null=True)
    BATTERY_VOLTAGE = models.FloatField(max_length=25, blank=True, null=True)
    BATTERY_PACKS = models.CharField(max_length=25, blank=True, null=True)
    BATTERY_DETAILS = models.CharField(max_length=25, blank=True, null=True)
    PUMP_BATTERY_SERIAL_NO = models.IntegerField(blank=True, null=True)

    CUSTOMIZATION = models.CharField(max_length=200, blank=True, null=True)
    COMMENTS = models.TextField(blank=True, null=True)

    #Database constraints
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_CHECKS",
                check=models.Q(START_DATE_QC__in=Status.values)
                & models.Q(LAUNCH_DATE_QC__in=Status.values)
                & models.Q(LAUNCH_POSITION_QC__in=Status.values)
                & models.Q(DEPLOYMENT_TYPE__in=DeploymentType.values)
                & models.Q(WMO_INST_TYPE__in=[pair[0] for pair in Instrument_Choices])
                & models.Q(PLATFORM_MAKER__in=[pair[0] for pair in Platform_Maker_Choices])
                & models.Q(PLATFORM_TYPE__in=[pair[0] for pair in Platform_Types_Choices])
                & models.Q(TRANS_SYSTEM__in=[pair[0] for pair in Transmission_Systems_Choices])
                & models.Q(LAUNCH_LATITUDE__lte=90)
                & models.Q(LAUNCH_LATITUDE__gte=-90)
                & models.Q(LAUNCH_LONGITUDE__lte=180)
                & models.Q(LAUNCH_LONGITUDE__gte=-180)
            )
        ]

    #For admin detail view
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

    # renames the instances of the model 
    # with their title name 
    def __str__(self): 
        return 'SN: '+str(self.FLOAT_SERIAL_NO)+' ID: '+str(self.id) + " WMO: " + str(self.PLATFORM_NUMBER)