%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gazepath
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Parse Eye-Tracking Data into Fixations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 

%description
Eye-tracking data must be transformed into fixations and saccades before
it can be analyzed. This package provides a non-parametric speed-based
approach to do this on a trial basis. The method is especially useful when
there are large differences in data quality, as the thresholds are
adjusted accordingly. The same pre-processing procedure can be applied to
all participants, while accounting for individual differences in data
quality. The method is described in van Renswoude et al. (2018)
<doi:10.3758/s13428-017-0909-3>.

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
