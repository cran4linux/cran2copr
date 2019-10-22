%global packname  SensMixed
%global packver   2.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Analysis of Sensory and Consumer Data in a Mixed Model Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-MASS 
Requires:         R-CRAN-lme4 >= 1.1
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-MASS 

%description
Functions that facilitate analysis of Sensory as well as Consumer data
within a mixed effects model framework. The so-called mixed assessor
models, that correct for the scaling effect are implemented. The
generation of the d-tilde plots forms part of the package. The shiny
application provides a GUI for the functionalities.

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
%doc %{rlibdir}/%{packname}/sensmixedUI
%doc %{rlibdir}/%{packname}/slowTests
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
