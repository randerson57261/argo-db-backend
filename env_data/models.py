from django.db import models
from deployments.models import deployment

class cycle_metadata(models.Model):

    #fields of the model
    DEPLOYMENT = models.ForeignKey(deployment, related_name='cycle_metadata', on_delete=models.PROTECT)
    DATE_ADD = models.DateTimeField() #creation of record in db
    PROFILE_ID = models.CharField(default=0, max_length=20, unique=True)

    ParkObs = models.CharField(blank=True, null=True, max_length=200)
    ParkDescentP = models.CharField(blank=True, null=True, max_length=2000)
    CONNECTION_ATTEMPTS = models.IntegerField(null=True, blank=True)
    CONNECTIONS = models.IntegerField(null=True, blank=True)
    UPLOAD_ATTEMPTS = models.IntegerField(null=True, blank=True)
    UPLOADS = models.IntegerField(null=True, blank=True)
    MSG_BYTES = models.IntegerField(null=True, blank=True)
    LOG_BYTES = models.IntegerField(null=True, blank=True)
    ISUS_BYTES = models.IntegerField(null=True, blank=True)
    GPS_DURATION = models.DurationField(null=True, blank=True)
    TRANS_DURATION = models.DurationField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cycle Metadata"

    #Default return
    def __str__(self): 
        return str(self.PROFILE_ID)


meta_int_fields = ['ActiveBallastAdjustments',  'BatteryCounts', 
    'BuoyancyPumpOnTime',  'CurrentBuoyancyPosition', 'DeepProfileBuoyancyPosition', 'FlashErrorsCorrectable', 
    'FlashErrorsUncorrectable', 'FloatId', 'GpsFixTime',  'IceMLSample', 'ParkDescentPCnt', 'ParkBuoyancyPosition', 'ProfileId', 'ObsIndex', 
    'SurfaceBuoyancyPosition', 'Vacuum', 'GpsNsat', 'IsusPowerCycleCounter','RtcSkew']
meta_str_fields = ['NpfFwRev', 'IceEvasionRecord', 'IceMLMedianT','Sbe41cpStatus', 'status']
meta_float_fields = ['GpsLong', 'GpsLat','Sbe41cpHumidity','Sbe41cpHumidityTemp','SurfacePressure', 'pHBaseAmps','pHBatteryInVolts','pHBatteryOutVolts',
    'pHCounterVolts', 'pHCounterAmps', 'AirBladderPressure', 'AirPumpAmps', 'AirPumpVolts', 'BuoyancyPumpAmps', 'BuoyancyPumpVolts',
    'QuiescentAmps', 'QuiescentVolts', 'Sbe41cpAmps', 'Sbe41cpVolts', 'Sbe63Amps', 'Sbe63Volts',  'McomsAmps', 'McomsVolts', 'Ocr504Amps','Ocr504Volts']
meta_date_fields = ['GpsFixDate','TimeStartDescent', 'TimeStartPark', 'TimeStartProfileDescent', 'TimeStartProfile', 'TimeStopProfile', 'TimeStartTelemetry']

for field in meta_int_fields:
    cycle_metadata.add_to_class(field, models.IntegerField(blank=True, null=True))

for field in meta_str_fields:
    cycle_metadata.add_to_class(field, models.CharField(blank=True, null=True, max_length=50))

for field in meta_float_fields:
    cycle_metadata.add_to_class(field, models.FloatField(blank=True, null=True))

for field in meta_date_fields:
    cycle_metadata.add_to_class(field, models.DateTimeField(blank=True, null=True))


class mission_reported(models.Model):
    DEPLOYMENT = models.ForeignKey(deployment, related_name='mission_reported', on_delete=models.PROTECT)
    DATE_ADD = models.DateTimeField() #creation of record in db
    PROFILE_ID = models.CharField(default=0, max_length=20, unique=True)
    
    AscentTimeOut = models.IntegerField(blank=True, null=True)
    BuoyancyNudge = models.IntegerField(blank=True, null=True)
    BuoyancyNudgeInitial = models.IntegerField(blank=True, null=True)
    ConnectTimeOut = models.IntegerField(blank=True, null=True)
    CpActivationP = models.IntegerField(blank=True, null=True)
    DeepProfileDescentTime = models.IntegerField(blank=True, null=True)
    DeepProfileBuoyancyPos = models.IntegerField(blank=True, null=True)
    DeepProfilePressure = models.IntegerField(blank=True, null=True)
    DownTime = models.IntegerField(blank=True, null=True)
    FloatId = models.CharField(max_length=25, blank=True, null=True)
    FullExtension = models.IntegerField(blank=True, null=True)
    FullRetraction = models.IntegerField(blank=True, null=True)
    IceDetectionP = models.FloatField(blank=True, null=True)
    IceEvasionP = models.FloatField(blank=True, null=True)
    IceMLTCritical = models.FloatField(blank=True, null=True)
    IceMonths = models.CharField(max_length=25, blank=True, null=True)
    IsusInit = models.IntegerField(blank=True, null=True)
    HpvEmfK = models.FloatField(blank=True, null=True)
    HpvRes = models.IntegerField(blank=True, null=True)
    MaxAirBladder = models.IntegerField(blank=True, null=True)
    MaxLogKb = models.IntegerField(blank=True, null=True)
    MissionPrelude = models.IntegerField(blank=True, null=True)
    OkVacuum = models.IntegerField(blank=True, null=True)
    PActivationBuoyancyPosition = models.IntegerField(blank=True, null=True)
    ParkDescentTime = models.IntegerField(blank=True, null=True)
    ParkBuoyancyPos = models.IntegerField(blank=True, null=True)
    ParkPressure = models.IntegerField(blank=True, null=True)
    PnPCycleLen = models.IntegerField(blank=True, null=True)
    TelemetryRetry = models.IntegerField(blank=True, null=True)
    TimeOfDay = models.IntegerField(blank=True, null=True)
    UpTime = models.IntegerField(blank=True, null=True)
    PhBattMode = models.IntegerField(blank=True, null=True)
    Verbosity = models.IntegerField(blank=True, null=True)
    DebugBits = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Missions Reported"

    #Default return
    def __str__(self): 
        return str(self.PROFILE_ID)


# Continuous profile samples, binned data generally above 1000 dbar
class continuous_profile(models.Model):

    #fields of the model
    DEPLOYMENT = models.ForeignKey(deployment, on_delete=models.PROTECT)
    DATE_ADD = models.DateTimeField() #creation of record in db
    PROFILE_ID = models.CharField(default=0, max_length=20)
    
    #Raw variables
    PRES = models.FloatField("Pressure dbar", blank=True, null=True)
    TEMP = models.FloatField("Temperature C", blank=True, null=True)
    PSAL = models.FloatField("Practical Salinity", blank=True, null=True)
    NB_SAMPLE_CTD = models.IntegerField("CTD Sample Count", blank=True, null=True)
    PHASE_DELAY_DOXY = models.FloatField("O2 Phase Delay microsecond", blank=True, null=True)
    TEMP_VOLTAGE_DOXY = models.FloatField("O2 Temperature voltage", blank=True, null=True)
    NB_SAMPLE_OPTODE = models.IntegerField("O2 Sample Count", blank=True, null=True)
    FLUORESCENCE_CHLA = models.FloatField("Fluorescence CHLa count", blank=True, null=True)
    BETA_BACKSCATTERING700 = models.FloatField("Beta Backscattering 700nm count", blank=True, null=True)
    FLUORESCENCE_CDOM = models.FloatField("Fluorescence CDOM count", blank=True, null=True)
    NB_SAMPLE_FLBBCD = models.IntegerField("FLBBCD Sample Count", blank=True, null=True)
    VRS_PH = models.FloatField("pH Vrs", blank=True, null=True)
    NB_SAMPLE_SFET = models.FloatField("pH Sample Count", blank=True, null=True)
    RAW_DOWN_IRRADIANCE380 = models.FloatField("Downwelling Irradiance at 380nm count", blank=True, null=True)
    RAW_DOWN_IRRADIANCE412 = models.FloatField("Downwelling Irradiance at 412nm count", blank=True, null=True)
    RAW_DOWN_IRRADIANCE490 = models.FloatField("Downwelling Irradiance at 490nm count", blank=True, null=True)
    RAW_DOWNWELLING_PAR = models.FloatField("Downwelling PAR count", blank=True, null=True)
    NB_SAMPLE_OCR = models.IntegerField("OCR Sample Count", blank=True, null=True)
    INCLINATION = models.FloatField("Inclination", blank=True, null=True)
    AZIMUTH = models.FloatField("Azimuth", blank=True, null=True)

    #Derived variables
    SAL_ABSOLUTE = models.FloatField("Absolute Salinity", blank=True, null=True)
    TEMP_CONSERVATIVE = models.FloatField("Temperature conservative", blank=True, null=True)
    SIGMA_0 = models.FloatField("Potential Density", blank=True, null=True)
    DEPTH = models.FloatField("Depth m", blank=True, null=True)
    DOXY = models.FloatField("Dissolved Oxygen umol/kg", blank=True, null=True)
    CHLA = models.FloatField("Chlorophyll a mg/m3", blank=True, null=True)
    BBP700 = models.FloatField("Particle backscattering at 700 nm m-1", blank=True, null=True)
    CDOM = models.FloatField("Coloured dissolved organic matter ppb", blank=True, null=True)
    PH_IN_SITU_TOTAL = models.FloatField("pH total scale", blank=True, null=True)
    DOWN_IRRADIANCE380 = models.FloatField("Downwelling Irradiance at 380nm W/m^2/nm", blank=True, null=True)
    DOWN_IRRADIANCE412 = models.FloatField("Downwelling Irradiance at 412nm W/m^2/nm", blank=True, null=True)
    DOWN_IRRADIANCE490 = models.FloatField("Downwelling Irradiance at 490nm W/m^2/nm", blank=True, null=True)
    DOWNWELLING_PAR = models.FloatField("Downwelling PAR microMoleQuanta/m^2/sec", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Continuous Profile"

    #Default return
    def __str__(self): 
        return str(self.DEPLOYMENT)

# Nitrate continuous profile samples
class nitrate_continuous_profile(models.Model):

    #fields of the model
    DEPLOYMENT = models.ForeignKey(deployment, on_delete=models.PROTECT)
    DATE_ADD = models.DateTimeField() #creation of record in db
    PROFILE_ID = models.CharField(default=0, max_length=20)
    
    #nitrate data fields
    SAMPLE_TIME = models.DateTimeField()
    DARK_CURRENT = models.FloatField("Dark Current", blank=True, null=True)
    PRES = models.FloatField("Pressure dbar", blank=True, null=True)
    TEMP = models.FloatField("Temperature C", blank=True, null=True)
    PSAL = models.FloatField("Salinity", blank=True, null=True)
    NO3 = models.FloatField("Nitrate umol/kg", blank=True, null=True)
    BL_B = models.FloatField("Baseline Incercept", blank=True, null=True)
    BL_M = models.FloatField("Baseline Slope", blank=True, null=True)
    RMS_ERROR = models.FloatField("RMS Error", blank=True, null=True)
    WL_240 = models.FloatField(blank=True, null=True)
    ABS_240 = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Nitrate Continuous Profile"

    #Default return
    def __str__(self): 
        return str(self.DEPLOYMENT)

class discrete_profile(models.Model):
    #fields of the model
    DEPLOYMENT = models.ForeignKey(deployment, on_delete=models.PROTECT)
    DATE_ADD = models.DateTimeField() #creation of record in db
    PROFILE_ID = models.CharField(default=0, max_length=20)

    #Raw variables
    PRES = models.FloatField("Pressure dbar", blank=True, null=True)
    TEMP = models.FloatField("Temperature C", blank=True, null=True)
    PSAL = models.FloatField("Practical Salinity", blank=True, null=True)
    NITRATE = models.FloatField("Nitrate umol/kg", blank=True, null=True)
    PHASE_DELAY_DOXY = models.FloatField("O2 Phase Delay microsecond", blank=True, null=True)
    TEMP_VOLTAGE_DOXY = models.FloatField("O2 Temperature voltage", blank=True, null=True)
    FLUORESCENCE_CHLA = models.FloatField("Fluorescence CHLa count", blank=True, null=True)
    BETA_BACKSCATTERING700 = models.FloatField("Beta Backscattering 700nm count", blank=True, null=True)
    FLUORESCENCE_CDOM = models.FloatField("Fluorescence CDOM count", blank=True, null=True)
    VRS_PH = models.FloatField("pH Vrs", blank=True, null=True)
    VK_PH = models.FloatField("pH Vk", blank=True, null=True)
    IB_PH = models.FloatField("pH Ib", blank=True, null=True)
    IK_PH = models.FloatField("pH Ik", blank=True, null=True)
    RAW_DOWN_IRRADIANCE380 = models.FloatField("Downwelling Irradiance at 380nm count", blank=True, null=True)
    RAW_DOWN_IRRADIANCE412 = models.FloatField("Downwelling Irradiance at 412nm count", blank=True, null=True)
    RAW_DOWN_IRRADIANCE490 = models.FloatField("Downwelling Irradiance at 490nm count", blank=True, null=True)
    RAW_DOWNWELLING_PAR = models.FloatField("Downwelling PAR count", blank=True, null=True)
    TILT = models.FloatField("Tilt degree", blank=True, null=True)

    #Derived variables
    SAL_ABSOLUTE = models.FloatField("Absolute Salinity", blank=True, null=True)
    TEMP_CONSERVATIVE = models.FloatField("Temperature conservative", blank=True, null=True)
    SIGMA_0 = models.FloatField("Potential Density", blank=True, null=True)
    DEPTH = models.FloatField("Depth m", blank=True, null=True)
    DOXY = models.FloatField("Dissolved Oxygen umol/kg", blank=True, null=True)
    CHLA = models.FloatField("Chlorophyll a mg/m3", blank=True, null=True)
    BBP700 = models.FloatField("Particle backscattering at 700 nm m-1", blank=True, null=True)
    CDOM = models.FloatField("Coloured dissolved organic matter ppb", blank=True, null=True)
    PH_IN_SITU_TOTAL = models.FloatField("pH total scale", blank=True, null=True)
    DOWN_IRRADIANCE380 = models.FloatField("Downwelling Irradiance at 380nm W/m^2/nm", blank=True, null=True)
    DOWN_IRRADIANCE412 = models.FloatField("Downwelling Irradiance at 412nm W/m^2/nm", blank=True, null=True)
    DOWN_IRRADIANCE490 = models.FloatField("Downwelling Irradiance at 490nm W/m^2/nm", blank=True, null=True)
    DOWNWELLING_PAR = models.FloatField("Downwelling PAR microMoleQuanta/m^2/sec", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Discrete Profile"

    #Default return
    def __str__(self): 
        return str(self.DEPLOYMENT)


# Table in db
class park(models.Model):

    #fields of the model
    DEPLOYMENT = models.ForeignKey(deployment, related_name='park', on_delete=models.PROTECT)
    DATE_ADD = models.DateTimeField()
    PROFILE_ID = models.CharField(default=0, max_length=20)

    DATE_MEASURED = models.DateTimeField()
    PRES = models.FloatField(blank=True, null=True) #Blank=True is not required
    TEMP = models.FloatField(blank=True, null=True)
    PSAL = models.FloatField(blank=True, null=True)
    PHASE_DELAY_DOXY = models.FloatField(blank=True, null=True)
    TEMP_VOLTAGE_DOXY = models.FloatField(blank=True, null=True)
    VRS_PH = models.FloatField(blank=True, null=True)
    VK_PH = models.FloatField(blank=True, null=True)
    IB_PH = models.FloatField(blank=True, null=True)
    IK_PH = models.FloatField(blank=True, null=True)
    RAW_DOWN_IRRADIANCE380 = models.FloatField(blank=True, null=True)
    RAW_DOWN_IRRADIANCE412 = models.FloatField(blank=True, null=True)
    RAW_DOWN_IRRADIANCE490 = models.FloatField(blank=True, null=True)
    RAW_DOWNWELLING_PAR = models.FloatField(blank=True, null=True)
    TILT = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Park Data"

    #Default return
    def __str__(self): 
        return str(self.DEPLOYMENT)