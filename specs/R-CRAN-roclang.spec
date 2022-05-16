%global __brp_check_rpaths %{nil}
%global packname  roclang
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Diffusing Function Documentations into 'Roxygen' Comments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 7.1.1
BuildRequires:    R-methods >= 4.0.0
BuildRequires:    R-utils >= 4.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-rex >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-roxygen2 >= 7.1.1
Requires:         R-methods >= 4.0.0
Requires:         R-utils >= 4.0.0
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-rex >= 1.2.0
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-purrr >= 0.3.4

%description
Efficient diffusing of content across function documentations. Sections,
parameters or dot parameters are extracted from function documentations
and turned into valid Rd character strings, which are ready to diffuse
into the 'roxygen' comments of another function by inserting inline code.

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
