%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rix
%global packver   0.15.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Data Science Environments with 'Nix'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-utils 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sys 
Requires:         R-utils 

%description
Simplifies the creation of reproducible data science environments using
the 'Nix' package manager, as described in Dolstra (2006) <ISBN
90-393-4130-3>. The included `rix()` function generates a complete
description of the environment as a `default.nix` file, which can then be
built using 'Nix'. This results in project specific software environments
with pinned versions of R, packages, linked system dependencies, and other
tools. Additional helpers make it easy to run R code in 'Nix' software
environments for testing and production.

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
