%global packname  scorecardModelUtils
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          3%{?dist}
Summary:          Credit Scorecard Modelling Utils

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 

%description
Provides infrastructure functionalities such as missing value treatment,
information value calculation, GINI calculation etc. which are used for
developing a traditional credit scorecard as well as a machine learning
based model. The functionalities defined are standard steps for any credit
underwriting scorecard development, extensively used in financial domain.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
