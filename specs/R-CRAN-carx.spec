%global packname  carx
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}%{?buildtag}
Summary:          Censored Autoregressive Model with Exogenous Covariates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-nlme 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-nlme 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
A censored time series class is designed. An estimation procedure is
implemented to estimate the Censored AutoRegressive time series with
eXogenous covariates (CARX), assuming normality of the innovations. Some
other functions that might be useful are also included.

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
