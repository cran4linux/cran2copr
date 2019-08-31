%global packname  camtrapR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Camera Trap Data Management and Preparation of Occupancy andSpatial Capture-Recapture Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl(Image::ExifTool)
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-overlap 
BuildRequires:    R-CRAN-secr 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-ritis 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-overlap 
Requires:         R-CRAN-secr 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-ritis 

%description
Management of and data extraction from camera trap photographs in wildlife
studies. The package provides a workflow for storing and sorting camera
trap photos, tabulates records of species and individuals, and creates
detection/non-detection matrices for occupancy and spatial
capture-recapture analyses with great flexibility. In addition, it
provides simple mapping functions (number of species, number of
independent species detections by station including GIS export) and can
visualise species activity data.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/pictures
%{rlibdir}/%{packname}/INDEX
