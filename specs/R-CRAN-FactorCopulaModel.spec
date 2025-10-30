%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FactorCopulaModel
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Copula Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-VineCopula 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-VineCopula 

%description
Inference methods for factor copula models for continuous data in Krupskii
and Joe (2013) <doi:10.1016/j.jmva.2013.05.001>, Krupskii and Joe (2015)
<doi:10.1016/j.jmva.2014.11.002>, Fan and Joe (2024)
<doi:10.1016/j.jmva.2023.105263>, one factor truncated vine models in Joe
(2018) <doi:10.1002/cjs.11481>, and Gaussian oblique factor models.
Functions for computing tail-weighted dependence measures in Lee, Joe and
Krupskii (2018) <doi:10.1080/10485252.2017.1407414> and estimating tail
dependence parameter.

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
