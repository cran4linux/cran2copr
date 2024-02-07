%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  instantiate
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pre-Compiled 'CmdStan' Models in R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Similar to 'rstantools' for 'rstan', the 'instantiate' package builds
pre-compiled 'CmdStan' models into CRAN-ready statistical modeling R
packages. The models compile once during installation, the executables
live inside the file systems of their respective packages, and users have
the full power and convenience of 'cmdstanr' without any additional
compilation after package installation. This approach saves time and helps
R package developers migrate from 'rstan' to the more modern 'cmdstanr'.
Packages 'rstantools', 'cmdstanr', 'stannis', and 'stanapi' are similar
Stan clients with different objectives.

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
