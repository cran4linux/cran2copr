%global packname  RandomCoefficients
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Adaptive Estimation in the Linear Random Coefficients Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-fourierin 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-rdetools 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-RCEIM 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-fourierin 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-rdetools 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-RCEIM 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-VGAM 

%description
We implement adaptive estimation of the joint density linear model where
the coefficients - intercept and slopes - are random and independent from
regressors which support is a proper subset. The estimator proposed in
Gaillac and Gautier (2019) <arXiv:1905.06584> is based on Prolate
Spheroidal Wave Functions which are computed efficiently in
'RandomCoefficients'. This package also provides a parallel implementation
of the estimator.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
