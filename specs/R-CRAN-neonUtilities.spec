%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neonUtilities
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Working with NEON Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.17.8
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-data.table >= 1.17.8
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jose 
Requires:         R-CRAN-downloader 
Requires:         R-utils 
Requires:         R-CRAN-R.utils 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-rlang 

%description
NEON data packages can be accessed through the NEON Data Portal
<https://www.neonscience.org> or through the NEON Data API (see
<https://data.neonscience.org/data-api> for documentation). Data delivered
from the Data Portal are provided as monthly zip files packaged within a
parent zip file, while individual files can be accessed from the API. This
package provides tools that aid in discovering, downloading, and
reformatting data prior to use in analyses. This includes downloading data
via the API, merging data tables by type, and converting formats. For more
information, see the readme file at
<https://github.com/NEONScience/NEON-utilities>.

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
