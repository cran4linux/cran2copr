%global packname  aoristic
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          aoristic analysis with spatial output (kml)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-GISTools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-plotKML 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-GISTools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-plotKML 
Requires:         R-MASS 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-RColorBrewer 

%description
'Aoristic' is one of the past tenses in Greek and represents an uncertain
occurrence time.  Aoristic analysis suggested by Ratcliffe (2002) is a
method to analyze events that do not have exact times of occurrence but
have starting times and ending times.  For example, a property crime
database (e.g., burglary) typically has a starting time and ending time of
the crime that could have occurred.  Aoristic analysis allocates the
probability of a crime incident occurring at every hour over a 24-hour
period. The probability is aggregated over a study area to create an
aoristic graph. Using crime incident data with lat/lon, DateTimeFrom, and
DateTimeTo, functions in this package create a total of three (3) kml
files and corresponding aoristic graphs: 1) density and contour; 2) grid
count; and 3) shapefile boundary. (see also:
https://sites.google.com/site/georgekick/software)

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
