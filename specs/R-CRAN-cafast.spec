%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cafast
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Companions to the 'CAs' Package for Covering Arrays

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-CAs 
Requires:         R-CRAN-CAs 

%description
Compiled implementations and generalizations of selected functions of the
'CAs' package by Ulrike Groemping for covering arrays. The package
provides a C version of the search for the largest set of rows that can be
made constant by permuting symbols, the power construction of Colbourn and
Torres-Jimenez (2010) <doi:10.1090/conm/523/10309> for any strength,
number of columns and number of levels, a counting kernel that tabulates
value tuples for every set of t columns, and fast versions of the
flexible-value tools and of the randomized post-optimization of Nayeri,
Colbourn and Konjevod (2013) <doi:10.1016/j.ejc.2012.07.017>. Each
function was tested against its 'CAs' counterpart, and the remaining
differences are documented.

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
