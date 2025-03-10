%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  STATcubeR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for the 'STATcube' REST API and Open Government Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.1
BuildRequires:    R-CRAN-pillar >= 1.5.0
BuildRequires:    R-CRAN-vctrs >= 0.5.2
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-cli >= 3.4.1
Requires:         R-CRAN-pillar >= 1.5.0
Requires:         R-CRAN-vctrs >= 0.5.2
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Import data from the 'STATcube' REST API or from the open data portal of
Statistics Austria. This package includes a client for API requests as
well as parsing utilities for data which originates from 'STATcube'.
Documentation about 'STATcubeR' is provided by several vignettes included
in the package as well as on the public 'pkgdown' page at
<https://statistikat.github.io/STATcubeR/>.

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
