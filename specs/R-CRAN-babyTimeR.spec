%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  babyTimeR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parse Output from 'BabyTime' Application

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.4.1
BuildRequires:    R-CRAN-janitor >= 2.2.0
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-lubridate >= 1.9.3
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-snakecase >= 0.11.1
BuildRequires:    R-utils 
Requires:         R-methods >= 4.4.1
Requires:         R-CRAN-janitor >= 2.2.0
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-lubridate >= 1.9.3
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-snakecase >= 0.11.1
Requires:         R-utils 

%description
'BabyTime' is an application for tracking infant and toddler care
activities like sleeping, eating, etc. This package will take the
outputted .zip files and parse it into a usable list object with cleaned
data. It handles malformed and incomplete data gracefully and is designed
to parse one directory at a time.

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
