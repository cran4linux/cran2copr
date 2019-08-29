%global packname  BayesCR
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Bayesian Analysis of Censored Regression Models Under ScaleMixture of Skew Normal Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mnormt 

%description
Propose a parametric fit for censored linear regression models based on
SMSN distributions, from a Bayesian perspective. Also, generates SMSN
random variables.

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
