%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  searchlight
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Audited Analysis of Police Stop and Search Records

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CARBayes >= 6.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-CARBayes >= 6.1.1
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-splines 
Requires:         R-CRAN-suncalc 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xml2 

%description
Acquire and audit public police stop and search archives for England and
Wales, retaining provenance and explicit coverage information. Designed
for exposure-based ethnic disparity analysis with separately reported
sampling and assumption uncertainty. Contains public sector information
licensed under the Open Government Licence v3.0.

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
