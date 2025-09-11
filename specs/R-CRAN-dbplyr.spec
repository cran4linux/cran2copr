%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbplyr
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'dplyr' Back End for Databases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-R6 >= 2.2.2
BuildRequires:    R-CRAN-pillar >= 1.9.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-blob >= 1.2.0
BuildRequires:    R-CRAN-DBI >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-vctrs >= 0.6.3
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-R6 >= 2.2.2
Requires:         R-CRAN-pillar >= 1.9.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-blob >= 1.2.0
Requires:         R-CRAN-DBI >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-vctrs >= 0.6.3
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-utils 

%description
A 'dplyr' back end for databases that allows you to work with remote
database tables as if they are in-memory data frames.  Basic features
works with any database that has a 'DBI' back end; more advanced features
require 'SQL' translation to be provided by the package author.

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
