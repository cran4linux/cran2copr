%global __brp_check_rpaths %{nil}
%global packname  MultBiplotR
%global packver   1.3.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.30
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Analysis Using Biplots in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-optimr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dunn.test 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-optimr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dunn.test 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-mvtnorm 

%description
Several multivariate techniques from a biplot perspective. It is the
translation (with many improvements) into R of the previous package
developed in 'Matlab'. The package contains some of the main developments
of my team during the last 30 years together with some more standard
techniques. Package includes: Classical Biplots, HJ-Biplot, Canonical
Biplots, MANOVA Biplots, Correspondence Analysis, Canonical Correspondence
Analysis, Canonical STATIS-ACT, Logistic Biplots for binary and ordinal
data, Multidimensional Unfolding, External Biplots for Principal
Coordinates Analysis or Multidimensional Scaling, among many others.
References can be found in the help of each procedure.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
