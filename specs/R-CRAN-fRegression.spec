%global packname  fRegression
%global packver   3042.82
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3042.82
Release:          1%{?dist}
Summary:          Rmetrics - Regression Based Decision and Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-mgcv 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-lmtest 
Requires:         R-mgcv 
Requires:         R-nnet 
Requires:         R-CRAN-polspline 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
A collection of functions for linear and non-linear regression modelling.
It implements a wrapper for several regression models available in the
base and contributed packages of R.

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
%doc %{rlibdir}/%{packname}/obsolete
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
