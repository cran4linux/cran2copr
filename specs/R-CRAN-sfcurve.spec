%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sfcurve
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          2x2, 3x3 and Nxn Space-Filling Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-colorRamp2 
Requires:         R-grid 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-colorRamp2 

%description
Implementation of all possible forms of 2x2 and 3x3 space-filling curves,
i.e., the generalized forms of the Hilbert curve
<https://en.wikipedia.org/wiki/Hilbert_curve>, the Peano curve
<https://en.wikipedia.org/wiki/Peano_curve> and the Peano curve in the
meander type (Figure 5 in <https://eudml.org/doc/141086>). It can
generates nxn curves expanded from any specific level-1 units. It also
implements the H-curve and the three-dimensional Hilbert curve.

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
