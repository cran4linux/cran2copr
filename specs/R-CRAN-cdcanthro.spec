%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cdcanthro
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Standardized Metrics Based on the CDC and WHO Growth Charts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-stats 
Requires:         R-utils 

%description
Calculation of sex- and age-standardized growth metrics using the LMS
method (lambda-mu-sigma). The package includes functions for the CDC
Growth Charts (cdc_z) and the WHO Charts (who_z). Because CDC recommends
using the WHO Charts for children under 24 months and the CDC Charts among
older children, there can be large differences at age 2.0 years. For
example, a girl weighing 9.9 kg would be at the WHO 10th percentile on the
day before her second birthday, but at the CDC 2nd percentile the
following day. The 'gradual_z' function reduces the differences among 2-
to 5-year-olds by taking a weighted average of the CDC and WHO z-scores.

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
