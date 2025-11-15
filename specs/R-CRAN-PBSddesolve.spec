%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PBSddesolve
%global packver   1.13.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.7
Release:          1%{?dist}%{?buildtag}
Summary:          Solver for Delay Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0

%description
Functions for solving systems of delay differential equations by
interfacing with numerical routines written by Simon N. Wood, including
contributions from Benjamin J. Cairns. These numerical routines first
appeared in Simon Wood's 'solv95' program. This package includes a
vignette and a complete user's guide. 'PBSddesolve' originally appeared on
CRAN under the name 'ddesolve'. That version is no longer supported. The
current name emphasizes a close association with other 'PBS' packages,
particularly 'PBSmodelling'.

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
