%global packname  pec
%global packver   2019.11.03
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.11.03
Release:          1%{?dist}
Summary:          Prediction Error Curves for Risk Prediction Models in SurvivalAnalysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-rms >= 4.2.0
BuildRequires:    R-survival >= 2.37.7
BuildRequires:    R-CRAN-timereg >= 1.8.9
BuildRequires:    R-CRAN-prodlim >= 1.4.9
BuildRequires:    R-CRAN-foreach >= 1.4.2
Requires:         R-CRAN-rms >= 4.2.0
Requires:         R-survival >= 2.37.7
Requires:         R-CRAN-timereg >= 1.8.9
Requires:         R-CRAN-prodlim >= 1.4.9
Requires:         R-CRAN-foreach >= 1.4.2

%description
Validation of risk predictions obtained from survival models and competing
risk models based on censored data using inverse weighting and
cross-validation.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
