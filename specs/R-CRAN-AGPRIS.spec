%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AGPRIS
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          AGricultural PRoductivity in Space

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-maxLik 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-maxLik 

%description
Functionalities to simulate space-time data and to estimate
dynamic-spatial panel data models. Estimators implemented are the BCML
(Elhorst (2010), <doi:10.1016/j.regsciurbeco.2010.03.003>), the MML
(Elhorst (2010) <doi:10.1016/j.regsciurbeco.2010.03.003>) and the INLA
Bayesian estimator (Lindgren and Rue, (2015) <doi:10.18637/jss.v063.i19>;
Bivand, Gomez-Rubio and Rue, (2015) <doi:10.18637/jss.v063.i20>) adapted
to panel data. The package contains functions to replicate the analyses of
the scientific article entitled "Agricultural Productivity in Space"
(Baldoni and Esposti (2021), <doi:10.1111/ajae.12155>)).

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
