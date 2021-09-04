%global __brp_check_rpaths %{nil}
%global packname  dockerfiler
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Dockerfile Creation from R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-attempt >= 0.3.1
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pkgbuild 
Requires:         R-CRAN-attempt >= 0.3.1
Requires:         R-CRAN-glue 
Requires:         R-CRAN-R6 
Requires:         R-utils 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pkgbuild 

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
