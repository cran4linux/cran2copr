%global packname  parfm
%global packver   2.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.6
Release:          1%{?dist}
Summary:          Parametric Frailty Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sn 
Requires:         R-survival 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-msm 
Requires:         R-graphics 
Requires:         R-CRAN-sn 

%description
Fits Parametric Frailty Models by maximum marginal likelihood. Possible
baseline hazards: exponential, Weibull, inverse Weibull (Fréchet),
Gompertz, lognormal, log-skew-normal, and loglogistic. Possible Frailty
distributions: gamma, positive stable, inverse Gaussian and lognormal.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
