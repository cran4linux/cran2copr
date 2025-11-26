%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psyntur
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Helper Tools for Teaching Statistical Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 4.2.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-psych >= 2.1.6
BuildRequires:    R-CRAN-GGally >= 2.1.2
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-formula.tools >= 1.7.1
BuildRequires:    R-CRAN-fastDummies >= 1.6.3
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-tidyselect >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-effsize >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggthemes >= 4.2.4
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-psych >= 2.1.6
Requires:         R-CRAN-GGally >= 2.1.2
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-formula.tools >= 1.7.1
Requires:         R-CRAN-fastDummies >= 1.6.3
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-tidyselect >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-effsize >= 0.8.1
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.4

%description
Provides functions and data-sets that are helpful for teaching statistics
and data analysis. It was originally designed for use when teaching
students in the Psychology Department at Nottingham Trent University.

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
