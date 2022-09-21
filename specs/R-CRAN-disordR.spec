%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  disordR
%global packver   0.0-9-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Ordered Vectors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.3.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-Matrix >= 1.3.3
Requires:         R-methods 
Requires:         R-CRAN-digest 

%description
Functionality for manipulating values of associative maps.  Ordinary R
vectors are unsuitable for working with values of associative maps because
elements of an R vector may be accessed by reference to their location in
the vector, but associative maps are stored in arbitrary order.  However,
when associating keys with values one needs both parts to be in 1-1
correspondence, so one cannot dispense with the order entirely.  The
'disordR' package includes a single S4 class, disord.  This class allows
one to perform only those operations appropriate for manipulating values
of associative maps and prevents any other operation (such as accessing an
element at a particular location).  A useful heuristic is that one is only
allowed to access or modify a disord object using a python list
comprehension.  The idea is to prevent ill-defined operations on values
(or keys) of associative maps, whose order is undefined or at best
implementation-specific, while allowing and facilitating sensible
operations.

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
