%global packname  metR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Tools for Easier Analysis of Meteorological Fields

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-formula.tools 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-maptools 
Requires:         R-Matrix 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 

%description
Many useful functions and extensions for dealing with meteorological data
in the tidy data framework. Extends 'ggplot2' for better plotting of
scalar and vector fields and provides commonly used analysis methods in
the atmospheric sciences.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
