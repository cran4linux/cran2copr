%global __brp_check_rpaths %{nil}
%global packname  MorphoTools2
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Morphometric Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-candisc 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-heplots 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-stats 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-candisc 
Requires:         R-CRAN-car 
Requires:         R-CRAN-class 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-heplots 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-StatMatch 
Requires:         R-utils 
Requires:         R-CRAN-vegan 
Requires:         R-stats 

%description
Tools for multivariate analyses of morphological data, wrapped in one
package, to make the workflow convenient and fast. Statistical and
graphical tools provide a comprehensive framework for checking and
manipulating input data, statistical analyses, and visualization of
results. Several methods are provided for the analysis of raw data, to
make the dataset ready for downstream analyses. Integrated statistical
methods include hierarchical classification, principal component analysis,
principal coordinates analysis, non-metric multidimensional scaling, and
multiple discriminant analyses: canonical, stepwise, and classificatory
(linear, quadratic, and the non-parametric k nearest neighbours). The
philosophy of the package will be described in Šlenker et al. (in prep).

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
