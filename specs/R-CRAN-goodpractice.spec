%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  goodpractice
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advice on R Package Building

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lintr >= 3.0.0
BuildRequires:    R-CRAN-cyclocomp >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-praise 
BuildRequires:    R-CRAN-rcmdcheck 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-spelling 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-treesitter 
BuildRequires:    R-CRAN-treesitter.r 
BuildRequires:    R-CRAN-urlchecker 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whoami 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-lintr >= 3.0.0
Requires:         R-CRAN-cyclocomp >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-praise 
Requires:         R-CRAN-rcmdcheck 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-spelling 
Requires:         R-tools 
Requires:         R-CRAN-treesitter 
Requires:         R-CRAN-treesitter.r 
Requires:         R-CRAN-urlchecker 
Requires:         R-utils 
Requires:         R-CRAN-whoami 
Requires:         R-CRAN-withr 

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
