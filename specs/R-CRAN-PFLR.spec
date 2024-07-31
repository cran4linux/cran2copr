%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PFLR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Penalized Functional Linear Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-flare 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-flare 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of commonly used penalized functional linear regression
models, including the Smooth and Locally Sparse (SLoS) method by Lin et
al. (2016) <doi:10.1080/10618600.2016.1195273>, Nested Group bridge
Regression (NGR) method by Guan et al. (2020)
<doi:10.1080/10618600.2020.1713797>, Functional Linear Regression That's
interpretable (FLIRTI) by James et al. (2009) <doi:10.1214/08-AOS641>, and
the Penalized B-spline regression method.

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
