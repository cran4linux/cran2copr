%global packname  waveformlidar
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Waveform LiDAR Data Processing and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.8.0
BuildRequires:    R-CRAN-data.table >= 1.9.7
BuildRequires:    R-CRAN-rgdal >= 1.3.0
BuildRequires:    R-CRAN-rgeos >= 0.3.8
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-flux 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-raster >= 2.8.0
Requires:         R-CRAN-data.table >= 1.9.7
Requires:         R-CRAN-rgdal >= 1.3.0
Requires:         R-CRAN-rgeos >= 0.3.8
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-flux 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-splitstackshape 
Requires:         R-CRAN-reshape2 

%description
A wealth of Full Waveform (FW) Light Detection and Ranging (LiDAR) data
are available to the public from different sources, which is poised to
boost the extensive application of FW LiDAR data. However, we lack a handy
and open source tool that can be used by ecological and remote sensing
communities for processing and analyzing FW LiDAR data. To this end, we
introduce 'waveformlidar', an R package dedicated to FW LiDAR processing,
analysis and visualization as a solution to the constraint. Specifically,
this package provides several commonly used waveform processing methods
such as Gaussian, adaptive Gaussian and Weibull decompositions, and
deconvolution approaches (Gold and Richard-Lucy (RL)) with customized
settings. In addition, we also develop some functions to derive commonly
used waveform metrics for characterizing vegetation structure. Moreover, a
new way to directly visualize FW LiDAR data is developed through
converting waveforms into points to form the Hyper Point cloud (HPC),
which can be easily adopted and subsequently analyzed with existing
discrete-return LiDAR processing tools such as 'LAStools' and 'FUSION'.
Basic explorations of the HPC such as 3D voxelization of the HPC and
conversion from original waveforms to composite waveforms are also
available in this package. All of these functions are developed based on
small-footprint FW LiDAR data, but they can be easily transplanted to the
large footprint FW LiDAR data such as Geoscience Laser Altimeter System
(GLAS) and Global Ecosystem Dynamics Investigation (GEDI) data analysis.
References: Zhou et al. (2017a) <doi:10.1016/j.isprsjprs.2017.04.021>;
Zhou et al. (2017b) <doi:10.1016/j.rse.2017.08.012>; Zhou et al. (2018a)
<doi:10.3390/rs10010039>;Zhou et al. (2018b) <doi:10.3390/rs10121949>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
