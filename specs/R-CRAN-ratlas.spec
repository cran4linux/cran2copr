%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ratlas
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          ATLAS Formatting Functions and Templates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-colorspace >= 1.4.1
BuildRequires:    R-CRAN-scales >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-knitr >= 1.22
BuildRequires:    R-CRAN-fs >= 1.2.7
BuildRequires:    R-CRAN-bookdown >= 0.9
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-hrbrthemes >= 0.6.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-officedown >= 0.2.2
BuildRequires:    R-CRAN-extrafont >= 0.17
BuildRequires:    R-CRAN-xfun >= 0.12
BuildRequires:    R-CRAN-xaringan >= 0.11
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-colorspace >= 1.4.1
Requires:         R-CRAN-scales >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-knitr >= 1.22
Requires:         R-CRAN-fs >= 1.2.7
Requires:         R-CRAN-bookdown >= 0.9
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-hrbrthemes >= 0.6.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-officedown >= 0.2.2
Requires:         R-CRAN-extrafont >= 0.17
Requires:         R-CRAN-xfun >= 0.12
Requires:         R-CRAN-xaringan >= 0.11
Requires:         R-grDevices 

%description
Provides templates, formatting tools, and 'ggplot2' themes tailored for
the Accessible Teaching, Learning, and Assessment Systems (ATLAS)
organization. These templates facilitate the creation of topic guides and
technical reports, while the formatting functions enable users to
customize numbers and tables to meet specific requirements. Additionally,
the themes ensure a uniform visual style across graphics.

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
