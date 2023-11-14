%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dockerfiler
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Dockerfile Creation from R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-cli >= 2.3.0
BuildRequires:    R-CRAN-remotes >= 2.2.0
BuildRequires:    R-CRAN-usethis >= 2.0.1
BuildRequires:    R-CRAN-jsonlite >= 1.7.2
BuildRequires:    R-CRAN-fs >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-pkgbuild >= 1.2.0
BuildRequires:    R-CRAN-attempt >= 0.3.1
BuildRequires:    R-CRAN-pak >= 0.2.0
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-cli >= 2.3.0
Requires:         R-CRAN-remotes >= 2.2.0
Requires:         R-CRAN-usethis >= 2.0.1
Requires:         R-CRAN-jsonlite >= 1.7.2
Requires:         R-CRAN-fs >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-pkgbuild >= 1.2.0
Requires:         R-CRAN-attempt >= 0.3.1
Requires:         R-CRAN-pak >= 0.2.0
Requires:         R-CRAN-memoise 
Requires:         R-utils 

%description
Build a Dockerfile straight from your R session. 'dockerfiler' allows you
to create step by step a Dockerfile, and provide convenient tools to wrap
R code inside this Dockerfile.

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
