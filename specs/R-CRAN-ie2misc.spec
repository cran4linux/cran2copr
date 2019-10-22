%global packname  ie2misc
%global packver   0.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          1%{?dist}
Summary:          Irucka Embry's Miscellaneous USGS Functions

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-tcltk 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-gWidgets2tcltk 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-qdap 
BuildRequires:    R-CRAN-reader 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-tcltk 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-gWidgets2tcltk 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-qdap 
Requires:         R-CRAN-reader 
Requires:         R-CRAN-lubridate 

%description
A collection of Irucka Embry's miscellaneous USGS functions (processing
.exp and .psf files, statistical error functions, "+" dyadic operator for
use with NA, creating ADAPS and QW spreadsheet files, calculating
saturated enthalpy). Irucka created these functions while a Cherokee
Nation Technology Solutions (CNTS) United States Geological Survey (USGS)
Contractor and/or USGS employee.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
