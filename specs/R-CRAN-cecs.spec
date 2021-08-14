%global __brp_check_rpaths %{nil}
%global packname  cecs
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for the C Implementation of CEC Benchmark Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-cec2013 >= 0.1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-cec2013 >= 0.1.5

%description
Goal of this package is to provide access to benchmark functions defined
for the Special Session and Competition on Real-Parameter Single Objective
Optimization in one place. The package contains functions from following
years: 2013, 2014, 2015, 2017, 2019, 2021
(<https://github.com/P-N-Suganthan>). Implementations of CEC-2013 (Y.
Gonzalez-Fernandez & M. Zambrano-Bigiarini) and CEC2017 (D. Jagodziński)
are taken from existed R packages. Also, the original C source code has
been cleaned and reorganized for better readability.

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
