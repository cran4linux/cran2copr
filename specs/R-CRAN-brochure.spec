%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brochure
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multipage 'Shiny' Apps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-routr >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.12
BuildRequires:    R-CRAN-attempt >= 0.3.1
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-routr >= 2.0.0
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-rlang >= 0.4.12
Requires:         R-CRAN-attempt >= 0.3.1
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-purrr 

%description
Build natively multi-page 'Shiny' applications, serving content on several
endpoints instead of a single page. Pages are declared with their own user
interface and server function and are dispatched by URL with 'routr',
including parameterised routes. Redirections, request and response
middleware, and helpers to read and set cookies are also provided.

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
