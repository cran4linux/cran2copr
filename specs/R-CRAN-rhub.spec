%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rhub
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for R Package Developers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gitcreds 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rematch 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whoami 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gitcreds 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rematch 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rprojroot 
Requires:         R-utils 
Requires:         R-CRAN-whoami 

%description
R-hub v2 uses GitHub Actions to run 'R CMD check' and similar package
checks. The 'rhub' package helps you set up R-hub v2 for your R package,
and start running checks.

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
