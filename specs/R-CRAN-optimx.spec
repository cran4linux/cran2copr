%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optimx
%global packver   2025-4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Expanded Replacement and Extension of the 'optim' Function

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-pracma 

%description
Provides a replacement and extension of the optim() function to call to
several function minimization codes in R in a single statement. These
methods handle smooth, possibly box constrained functions of several or
many parameters. Note that function 'optimr()' was prepared to simplify
the incorporation of minimization codes going forward. Also implements
some utility codes and some extra solvers, including safeguarded Newton
methods. Many methods previously separate are now included here. This is
the version for CRAN.

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
