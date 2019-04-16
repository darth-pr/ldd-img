# LDD-IMG Change Log

## Release 1.6.0.0 - In Progress

* LDD-IMG-4 This is an example entry in that provides a short description of the fix. TODO: REMOVE THIS ENTRY

## Release 1.5.1.0 - TODO: Update w/ Release Date

* changed unit of bandwidth attribute from Units_of_Frequency to Units_of_Length

## Release 1.5.0.0 - TODO: Update w/ Release Date

* upgraded to v1A10 of the IM
* removed old blocks of commented out XML

## Release 1.4.0.0 - TODO: Update w/ Release Date

* upgraded to v1900 of the IM
* removed specific Autoexposure algorithm classes and introduced generic Algorithm_Parameter class
* new/improved definitions for Companding_Parameters, Downsampling_Parameters, Exposure_Parameters
* removed the following attributes: Data_Correction.data_correction_subtype
* removed the following classes because they were insufficiently multi-mission:
      - Derived_Product_Parameters
      - Frame_Parameters
      - Product_Identification 
      - Stereo_Product_Parameters
      - Vector_Range_Origin
 * added exposure_type enumeration
 * new flat_field_algorithm attribute
 * changed compression_type to compression_class and compression_mode_name to compression_type
 * added new enumerations for compression_class and compression_type
 * added new Instrument_Device_Currents class
