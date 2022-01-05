%global __brp_check_rpaths %{nil}
%global packname  h3jsr
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access Uber's H3 Library

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 4.0.0
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-V8 >= 4.0.0
Requires:         R-CRAN-geojsonsf 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Provides access to Uber's H3 library for geospatial indexing via its
JavaScript transpile 'h3-js' <https://github.com/uber/h3-js> and 'V8'
<https://github.com/jeroen/v8>.

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
