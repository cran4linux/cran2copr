%global packname  prodlim
%global packver   2019.11.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.11.13
Release:          3%{?dist}%{?buildtag}
Summary:          Product-Limit Estimation for Censored Event History Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-survival 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-lava 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-survival 
Requires:         R-KernSmooth 
Requires:         R-CRAN-lava 

%description
Fast and user friendly implementation of nonparametric estimators for
censored event history (survival) analysis. Kaplan-Meier and
Aalen-Johansen method.

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
%{rlibdir}/%{packname}/libs
