%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IVDML
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Double Machine Learning with Instrumental Variables and Heterogeneity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ranger 
Requires:         R-stats 
Requires:         R-CRAN-xgboost 

%description
Instrumental variable (IV) estimators for homogeneous and heterogeneous
treatment effects with efficient machine learning instruments. The
estimators are based on double/debiased machine learning allowing for
nonlinear and potentially high-dimensional control variables. Details can
be found in Scheidegger, Guo and Bühlmann (2025) "Inference for
heterogeneous treatment effects with efficient instruments and machine
learning" <doi:10.48550/arXiv.2503.03530>.

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
