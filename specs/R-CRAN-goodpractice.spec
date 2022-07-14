%global __brp_check_rpaths %{nil}
%global packname  goodpractice
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Advice on R Package Building

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lintr >= 3.0.0
BuildRequires:    R-CRAN-cyclocomp >= 1.1.0
BuildRequires:    R-CRAN-xmlparsedata >= 1.0.1
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-praise 
BuildRequires:    R-CRAN-rcmdcheck 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whoami 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-lintr >= 3.0.0
Requires:         R-CRAN-cyclocomp >= 1.1.0
Requires:         R-CRAN-xmlparsedata >= 1.0.1
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-praise 
Requires:         R-CRAN-rcmdcheck 
Requires:         R-CRAN-rstudioapi 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-whoami 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xml2 

%description
Give advice about good practices when building R packages. Advice includes
functions and syntax to avoid, package structure, code complexity, code
formatting, etc.

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
