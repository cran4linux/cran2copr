%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgmd
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Markdown Reference Documentation for R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-fs >= 1.6.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-fs >= 1.6.0
Requires:         R-CRAN-purrr >= 1.0.0

%description
Generates plain Markdown reference documentation for any R package,
installed or a local development source tree, optimized for rendering in
the 'GitHub'/'Gitea' browser UI and for use as LLM context (e.g. 'Claude
Code'). Reads Rd documentation via tools::Rd_db() (installed packages) or
directly from man/*.Rd (development packages, no installation required)
and renders one file per topic plus a navigable index.

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
