%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modeltests
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Testing Infrastructure for Broom Model Generics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-testthat >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-testthat >= 2.0.0
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-generics 

%description
Provides a number of testthat tests that can be used to verify that
tidy(), glance() and augment() methods meet consistent specifications.
This allows methods for the same generic to be spread across multiple
packages, since all of those packages can make the same guarantees to
users about returned objects.

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
