%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unvs.med
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Universal Approach for Causal Mediation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-snowfall 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-CRAN-snowfall 

%description
This program realizes a universal estimation approach that accommodates
multi-category variables and effect scales, making up for the deficiencies
of the existing approaches when dealing with non-binary exposures and
complex models. The estimation via bootstrapping can simultaneously
provide results of causal mediation on risk difference (RD), odds ratio
(OR) and risk ratio (RR) scales with tests of the effects' difference. The
estimation is also applicable to many other settings, e.g., moderated
mediation, inconsistent covariates, panel data, etc. The high flexibility
and compatibility make it possible to apply for any type of model, greatly
meeting the needs of current empirical researches.

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
