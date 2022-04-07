%global __brp_check_rpaths %{nil}
%global packname  dials
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Creating Tuning Parameter Values

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-vctrs >= 0.3.8
BuildRequires:    R-CRAN-hardhat >= 0.2.0
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-rlang >= 1.0.1
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-vctrs >= 0.3.8
Requires:         R-CRAN-hardhat >= 0.2.0
Requires:         R-CRAN-scales 
Requires:         R-CRAN-DiceDesign 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Many models contain tuning parameters (i.e. parameters that cannot be
directly estimated from the data). These tools can be used to define
objects for creating, simulating, or validating values for such
parameters.

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
