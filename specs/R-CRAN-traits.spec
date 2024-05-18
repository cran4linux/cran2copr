%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  traits
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Species Trait Data from Around the Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-tibble >= 1.3.4
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.19
BuildRequires:    R-CRAN-taxize >= 0.7.4
BuildRequires:    R-CRAN-crul >= 0.6.0
BuildRequires:    R-CRAN-rvest >= 0.3.1
BuildRequires:    R-CRAN-xml2 >= 0.1.2
BuildRequires:    R-CRAN-hoardr 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-tibble >= 1.3.4
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-jsonlite >= 0.9.19
Requires:         R-CRAN-taxize >= 0.7.4
Requires:         R-CRAN-crul >= 0.6.0
Requires:         R-CRAN-rvest >= 0.3.1
Requires:         R-CRAN-xml2 >= 0.1.2
Requires:         R-CRAN-hoardr 

%description
Species trait data from many different sources, including sequence data
from 'NCBI' (<https://www.ncbi.nlm.nih.gov/>), plant trait data from
'BETYdb', data from 'EOL' 'Traitbank', 'Birdlife' International, and more.

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
