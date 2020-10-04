%global packname  CopCTS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Copula-Based Semiparametric Analysis for Time Series Data withDetection Limits

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-copBasic 
BuildRequires:    R-methods 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-copBasic 
Requires:         R-methods 

%description
Semiparametric estimation for censored time series with lower detection
limit. The latent response is a sequence of stationary process with Markov
property of order one. Estimation of copula parameter(COPC) and
Conditional quantile estimation are included for five available copula
functions. Copula selection methods based on L2 distance from empirical
copula function are also included.

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
