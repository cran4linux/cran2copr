%global packname  Tplyr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Grammar of Clinical Data Summary

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-lifecycle 

%description
A tool created to simplify the data manipulation necessary to create
clinical reports.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
