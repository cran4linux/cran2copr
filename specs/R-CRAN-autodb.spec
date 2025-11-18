%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autodb
%global packver   3.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Database Normalisation for Data Frames

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Automatic normalisation of a data frame to third normal form, with the
intention of easing the process of data cleaning. (Usage to design your
actual database for you is not advised.) Originally inspired by the
'AutoNormalize' library for 'Python' by 'Alteryx'
(<https://github.com/alteryx/autonormalize>), with various changes and
improvements. Automatic discovery of functional or approximate
dependencies, normalisation based on those, and plotting of the resulting
"database" via 'Graphviz', with options to exclude some attributes at
discovery time, or remove discovered dependencies at normalisation time.

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
