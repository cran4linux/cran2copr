%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pboost
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Profile Boosting Framework for Parametric Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Formula 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Formula 

%description
A profile boosting framework for feature selection in parametric models.
It offers a unified interface pboost() and several wrapped models,
including linear model, generalized linear models, quantile regression,
Cox proportional hazards model, beta regression. An S3 interface EBIC() is
provided as the stopping rule for the profile boosting by default.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
