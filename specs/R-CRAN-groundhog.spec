%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  groundhog
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Version-Control for CRAN, GitHub, and GitLab Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-utils 
Requires:         R-methods 

%description
Make R scripts reproducible, by ensuring that every time a given script is
run, the same version of the used packages are loaded (instead of
whichever version the user running the script happens to have installed).
This is achieved by using the command groundhog.library() instead of the
base command library(), and including a date in the call. The date is used
to call on the same version of the package every time (the most recent
version available at that date). Load packages from CRAN, GitHub, or
Gitlab. ======================================= Note: groundhog relied on
Microsoft's MRAN archive which is being discontinued. This version of
groundhog is transitioning away from MRAN, relying on it only for dates
prior to Jan 31, 2023. A future release of groundhog, v2.3.0, expected by
May 2023, will discontinue relying on MRAN entirely.

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
