%global packname  ie2misc
%global packver   0.8.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.6
Release:          3%{?dist}%{?buildtag}
Summary:          Irucka Embry's Miscellaneous USGS Functions

License:          CC0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.1.4
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.10.2
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-gWidgets2tcltk 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-mgsub 
BuildRequires:    R-CRAN-reader 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-openxlsx >= 4.1.4
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-data.table >= 1.10.2
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-gWidgets2tcltk 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-mgsub 
Requires:         R-CRAN-reader 
Requires:         R-CRAN-lubridate 
Requires:         R-tcltk 
Requires:         R-utils 
Requires:         R-tools 

%description
A collection of Irucka Embry's miscellaneous USGS functions (processing
.exp and .psf files, statistical error functions, "+" dyadic operator for
use with NA, creating ADAPS and QW spreadsheet files, calculating
saturated enthalpy). Irucka created these functions while a Cherokee
Nation Technology Solutions (CNTS) United States Geological Survey (USGS)
Contractor and/or USGS employee.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
