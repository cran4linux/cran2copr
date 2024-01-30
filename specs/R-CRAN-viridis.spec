%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viridis
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Colorblind-Friendly Color Maps for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-viridisLite >= 0.4.0
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-viridisLite >= 0.4.0
Requires:         R-CRAN-gridExtra 

%description
Color maps designed to improve graph readability for readers with common
forms of color blindness and/or color vision deficiency. The color maps
are also perceptually-uniform, both in regular form and also when
converted to black-and-white for printing. This package also contains
'ggplot2' bindings for discrete and continuous color and fill scales. A
lean version of the package called 'viridisLite' that does not include the
'ggplot2' bindings can be found at
<https://cran.r-project.org/package=viridisLite>.

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
