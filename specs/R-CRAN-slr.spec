%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slr
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Latin Rectangles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ibd 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ibd 
Requires:         R-CRAN-gmp 

%description
A facility to generate balanced semi-Latin rectangles with any cell size
(preferably up to ten) with given number of treatments, see Uto, N.P. and
Bailey, R.A. (2020). "Balanced Semi-Latin rectangles: properties,
existence and constructions for block size two". Journal of Statistical
Theory and Practice, 14(3), 1-11, <doi:10.1007/s42519-020-00118-3>. It
also provides facility to generate partially balanced semi-Latin
rectangles for cell size 2, 3 and 4 for any number of treatments.

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
