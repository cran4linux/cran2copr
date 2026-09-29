%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  svyLocAdj
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Survey Data (E.g., DHS) with Adjustment for Location Perturbations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-spTimer 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-spTimer 
Requires:         R-CRAN-rstantools

%description
Bayesian spatial models for survey data, such as Demographic and Health
Survey (DHS), with spatial cluster location displacement adjustments. The
package implements models for (1) continuous, (2) binary, (3) count and
(4) spatially varying models for continuous outcomes. For more details see
Bakar et al. (2026) <doi:10.1093/jrsssa/qnag068>.

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
