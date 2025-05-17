%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mermboost
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Gradient Boosting for Generalized Additive Mixed Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-stabs 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-stabs 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
Provides a novel framework to estimate mixed models via gradient boosting.
The implemented functions are based on the 'mboost' and 'lme4' packages,
and the family range is therefore determined by 'lme4'. A correction
mechanism for cluster-constant covariates is implemented, as well as
estimation of the covariance of random effects. These methods are
described in the accompanying publication; see
<doi:10.1007/s11222-025-10612-y> for details.

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
