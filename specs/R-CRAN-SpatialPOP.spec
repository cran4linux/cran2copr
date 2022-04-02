%global __brp_check_rpaths %{nil}
%global packname  SpatialPOP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generation of Spatial Data with Spatially Varying Model Parameter

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-numbers 
Requires:         R-base 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-numbers 

%description
A spatial population can be generated based on spatially varying
regression model under the assumption that observations are collected from
a uniform two-dimensional grid consist of (m * m) lattice points with unit
distance between any two neighbouring points. For method details see Chao,
Liu., Chuanhua, Wei. and Yunan, Su.
(2018).<DOI:10.1080/10485252.2018.1499907>.  This spatially generated data
can be used to test different issues related to the statistical analysis
of spatial data. This generated spatial data can be utilized in
geographically weighted regression analysis for studying the spatially
varying relationships among the variables.

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
