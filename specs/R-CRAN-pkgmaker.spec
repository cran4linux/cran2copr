%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgmaker
%global packver   0.32.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.32.10
Release:          1%{?dist}%{?buildtag}
Summary:          Development Utilities for R Packages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-registry 
Requires:         R-tools 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-assertthat 

%description
Provides some low-level utilities to use for package development. It
currently provides managers for multiple package specific options and
registries, vignette, unit test and bibtex related utilities. It serves as
a base package for packages like 'NMF', 'RcppOctave', 'doRNG', and as an
incubator package for other general purposes utilities, that will
eventually be packaged separately. It is still under heavy development and
changes in the interface(s) are more than likely to happen.

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
