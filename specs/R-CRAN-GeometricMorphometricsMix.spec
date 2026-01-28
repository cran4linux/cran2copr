%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeometricMorphometricsMix
%global packver   0.6.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Heterogeneous Methods for Shape and Other Multidimensional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-ape 
Requires:         R-stats 
Requires:         R-CRAN-corpcor 
Requires:         R-methods 
Requires:         R-CRAN-mclust 

%description
Tools for geometric morphometric analyses and multidimensional data.
Implements methods for morphological disparity analysis using bootstrap
and rarefaction, as reviewed in Foote (1997)
<doi:10.1146/annurev.ecolsys.28.1.129>. Includes integration and
modularity testing, following Fruciano et al. (2013)
<doi:10.1371/journal.pone.0069376>, using Escoufier's RV coefficient as
test statistic as well as two-block partial least squares - PLS, Rohlf and
Corti (2000) <doi:10.1080/106351500750049806>. Also includes vector angle
comparisons, orthogonal projection for data correction (Burnaby (1966)
<doi:10.2307/2528217>; Fruciano (2016) <doi:10.1007/s00427-016-0537-4>),
and parallel analysis for dimensionality reduction (Buja and Eyuboglu
(1992) <doi:10.1207/s15327906mbr2704_2>).

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
