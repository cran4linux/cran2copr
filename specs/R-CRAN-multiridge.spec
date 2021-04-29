%global packname  multiridge
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Cross-Validation for Multi-Penalty Ridge Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-risksetROC 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-snowfall 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-risksetROC 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-snowfall 

%description
Multi-penalty linear, logistic and cox ridge regression, including
estimation of the penalty parameters by efficient (repeated)
cross-validation and marginal likelihood maximization. Multiple
high-dimensional data types that require penalization are allowed, as well
as unpenalized variables. Paired and preferential data types can be
specified. See Van de Wiel et al. (2021), <arXiv:2005.09301>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
