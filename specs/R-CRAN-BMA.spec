%global packname  BMA
%global packver   3.18.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.18.12
Release:          3%{?dist}
Summary:          Bayesian Model Averaging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-methods 
Requires:         R-survival 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-rrcov 
Requires:         R-methods 

%description
Package for Bayesian model averaging and variable selection for linear
models, generalized linear models and survival models (cox regression).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/libs
