%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shapes
%global packver   1.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Shape Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fitdistrplus 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fitdistrplus 

%description
Routines for the statistical analysis of landmark shapes, including
Procrustes analysis, graphical displays, principal components analysis,
permutation and bootstrap tests, thin-plate spline transformation grids
and comparing covariance matrices. See Dryden, I.L. and Mardia, K.V.
(2016). Statistical shape analysis, with Applications in R (2nd Edition),
John Wiley and Sons.

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
