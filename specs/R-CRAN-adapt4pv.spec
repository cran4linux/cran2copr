%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adapt4pv
%global packver   0.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Approaches for Signal Detection in Pharmacovigilance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 3.0.2
BuildRequires:    R-CRAN-Matrix >= 1.0.6
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-glmnet >= 3.0.2
Requires:         R-CRAN-Matrix >= 1.0.6
Requires:         R-CRAN-speedglm 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
A collection of several pharmacovigilance signal detection methods based
on adaptive lasso. Additional lasso-based and propensity score-based
signal detection approaches are also supplied. See Courtois et al
<doi:10.1186/s12874-021-01450-3>.

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
