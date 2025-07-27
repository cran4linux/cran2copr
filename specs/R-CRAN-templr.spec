%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  templr
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          MASCOTNUM / RT-UQ Algorithms Template Tools

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 

%description
Helper functions for MASCOTNUM / RT-UQ <https://uq.math.cnrs.fr/>
algorithm template, for design of numerical experiments practice:
algorithm template parser to support MASCOTNUM specification
<https://github.com/MASCOTNUM/algorithms>, 'ask & tell' decoupling
injection (inspired by
<https://search.r-project.org/CRAN/refmans/sensitivity/html/decoupling.html>)
to use "crimped" algorithms (like uniroot(), optim(), ...) from outside R,
basic template examples: Brent algorithm for 1 dim root finding and
L-BFGS-B from base optim().

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
