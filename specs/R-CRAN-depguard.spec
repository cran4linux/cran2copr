%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depguard
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Manifest-Based Dependency Conflict Detection for Sandboxed R Sessions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-cli 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-cli 

%description
Provides lightweight, manifest-based checking of R package dependencies
(including transitive dependencies) against the currently installed
environment, without requiring a full project lockfile. Designed for
sandboxed or ephemeral notebook environments (e.g. Kaggle, Colab, Binder)
where 'renv'-style lockfile ownership is impractical. Includes session
snapshot/diff tools (building on 'sessioninfo') to detect when an install
silently changes the version of a package that is already loaded, and
optional single-package version rollback.

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
