%global packname  stepPenal
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Stepwise Forward Variable Selection in Penalized Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
BuildRequires:    R-base 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-caret 
Requires:         R-stats 
Requires:         R-base 

%description
Model Selection Based on Combined Penalties. This package implements a
stepwise forward variable selection algorithm based on a penalized
likelihood criterion that combines the L0 with L2 or L1 norms.

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
