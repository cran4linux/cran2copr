%global __brp_check_rpaths %{nil}
%global packname  omsvg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build and Transform 'SVG' Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.3.2
BuildRequires:    R-CRAN-dplyr >= 1.0.3
BuildRequires:    R-CRAN-htmltools >= 0.5.1.1
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-sass >= 0.3.0
BuildRequires:    R-CRAN-gt >= 0.2.2
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-xml2 >= 1.3.2
Requires:         R-CRAN-dplyr >= 1.0.3
Requires:         R-CRAN-htmltools >= 0.5.1.1
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-sass >= 0.3.0
Requires:         R-CRAN-gt >= 0.2.2
Requires:         R-CRAN-magrittr 

%description
Build 'SVG' components using element-based functions. With an 'svg'
object, we can modify its graphical elements with a suite of transform
functions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
