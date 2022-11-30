%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tarchetypes
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Archetypes for Targets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-fs >= 1.4.2
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.25
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-vctrs >= 0.3.4
BuildRequires:    R-CRAN-furrr >= 0.3.0
BuildRequires:    R-CRAN-targets >= 0.11.0
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-fs >= 1.4.2
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.25
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-vctrs >= 0.3.4
Requires:         R-CRAN-furrr >= 0.3.0
Requires:         R-CRAN-targets >= 0.11.0
Requires:         R-utils 

%description
Function-oriented Make-like declarative workflows for Statistics and data
science are supported in the 'targets' R package. As an extension to
'targets', the 'tarchetypes' package provides convenient user-side
functions to make 'targets' easier to use. By establishing reusable
archetypes for common kinds of targets and pipelines, these functions help
express complicated reproducible workflows concisely and compactly. The
methods in this package were influenced by the 'drake' R package by Will
Landau (2018) <doi:10.21105/joss.00550>.

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
