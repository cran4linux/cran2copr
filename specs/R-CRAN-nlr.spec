%global packname  nlr
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Nonlinear Regression Modelling using Robust Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-robcor 
BuildRequires:    R-CRAN-TSA 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-CRAN-robcor 
Requires:         R-CRAN-TSA 
Requires:         R-CRAN-tseries 
Requires:         R-stats 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-quantreg 

%description
Non-Linear Robust package is developed to handle the problem of outliers
in nonlinear regression, using robust statistics. It covers classic
methods in nonlinear regression as well. It has facilities to fit models
in the case of auto correlated and heterogeneous variance cases, while it
include tools to detecting outliers in nonlinear regression. (Riazoshams
H, Midi H, and Ghilagaber G, (2018, ISBN:978-1-118-73806-1). Robust
Nonlinear Regression, with Application using R, John Wiley and Sons.)

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
