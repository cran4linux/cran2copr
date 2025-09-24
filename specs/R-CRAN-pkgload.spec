%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgload
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Package Installation and Attach

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.3.0
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-desc 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-rprojroot 
Requires:         R-utils 

%description
Simulates the process of installing a package and then attaching it. This
is a key part of the 'devtools' package as it allows you to rapidly
iterate while developing a package.

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
