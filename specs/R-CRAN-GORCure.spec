%global packname  GORCure
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          2%{?dist}
Summary:          Fit Generalized Odds Rate Mixture Cure Model with IntervalCensored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ICsurv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-survival 
Requires:         R-CRAN-ICsurv 
Requires:         R-CRAN-pracma 
Requires:         R-MASS 

%description
Generalized Odds Rate Mixture Cure (GORMC) model is a flexible model of
fitting survival data with a cure fraction, including the Proportional
Hazards Mixture Cure (PHMC) model and the Proportional Odds Mixture Cure
Model as special cases. This package fit the GORMC model with interval
censored data.

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
