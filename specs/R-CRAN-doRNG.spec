%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doRNG
%global packver   1.8.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.6
Release:          1%{?dist}%{?buildtag}
Summary:          Generic Reproducible Parallel Backend for 'foreach' Loops

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rngtools >= 1.5
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-rngtools >= 1.5
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-iterators 

%description
Provides functions to perform reproducible parallel foreach loops, using
independent random streams as generated by L'Ecuyer's combined
multiple-recursive generator [L'Ecuyer (1999),
<DOI:10.1287/opre.47.1.159>]. It enables to easily convert standard
'%%dopar%%' loops into fully reproducible loops, independently of the number
of workers, the task scheduling strategy, or the chosen parallel
environment and associated foreach backend.

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
