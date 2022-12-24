%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gwasrapidd
%global packver   0.99.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.14
Release:          1%{?dist}%{?buildtag}
Summary:          'REST' 'API' Client for the 'NHGRI'-'EBI' 'GWAS' Catalog

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr > 0.8.99
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-concatenate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-tidyr > 0.8.99
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-concatenate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-testthat 
Requires:         R-utils 
Requires:         R-CRAN-progress 

%description
'GWAS' R 'API' Data Download. This package provides easy access to the
'NHGRI'-'EBI' 'GWAS' Catalog data by accessing the 'REST' 'API'
<https://www.ebi.ac.uk/gwas/rest/docs/api/>.

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
