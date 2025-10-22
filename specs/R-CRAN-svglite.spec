%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  svglite
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          An 'SVG' Graphics Device

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libpng-devel
BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-systemfonts >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-textshaping >= 0.3.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-systemfonts >= 1.3.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-textshaping >= 0.3.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-lifecycle 

%description
A graphics device for R that produces 'Scalable Vector Graphics'.
'svglite' is a fork of the older 'RSvgDevice' package.

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
