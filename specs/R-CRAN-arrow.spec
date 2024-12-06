%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arrow
%global packver   18.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          18.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Integration to 'Apache' 'Arrow'

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libarrow-dataset-devel
BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-bit64 >= 0.9.7
BuildRequires:    R-CRAN-cpp11 >= 0.4.2
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-bit64 >= 0.9.7
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
'Apache' 'Arrow' <https://arrow.apache.org/> is a cross-language
development platform for in-memory data. It specifies a standardized
language-independent columnar memory format for flat and hierarchical
data, organized for efficient analytic operations on modern hardware. This
package provides an interface to the 'Arrow C++' library.

%prep
%setup -q -c -n %{packname}
sed -i 's|PKGCONFIG_DIRS=.*|PKGCONFIG_DIRS=-L%{_libdir}|' %{packname}/configure
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
