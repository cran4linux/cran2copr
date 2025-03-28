%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cbioportalR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Browse and Query Clinical and Genomic Data from cBioPortal

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-httr >= 1.4.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.3
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-cli >= 3.3.0
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-httr >= 1.4.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.3
Requires:         R-CRAN-purrr >= 0.3.4

%description
Provides R users with direct access to genomic and clinical data from the
'cBioPortal' web resource via user-friendly functions that wrap
'cBioPortal's' existing API endpoints
<https://www.cbioportal.org/api/swagger-ui/index.html>. Users can browse
and query genomic data on mutations, copy number alterations and fusions,
as well as data on tumor mutational burden ('TMB'), microsatellite
instability status ('MSI'), 'FACETS' and select clinical data points
(depending on the study). See <https://www.cbioportal.org/> and Gao et
al., (2013) <doi:10.1126/scisignal.2004088> for more information on the
cBioPortal web resource.

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
