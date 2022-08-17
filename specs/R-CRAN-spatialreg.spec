%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialreg
%global packver   1.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Regression Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-spData 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-gmodels 
Requires:         R-CRAN-spData 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-boot 
Requires:         R-splines 
Requires:         R-CRAN-LearnBayes 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-gmodels 

%description
A collection of all the estimation functions for spatial cross-sectional
models (on lattice/areal data using spatial weights matrices) contained up
to now in 'spdep', 'sphet' and 'spse'. These model fitting functions
include maximum likelihood methods for cross-sectional models proposed by
'Cliff' and 'Ord' (1973, ISBN:0850860369) and (1981, ISBN:0850860814),
fitting methods initially described by 'Ord' (1975)
<doi:10.1080/01621459.1975.10480272>. The models are further described by
'Anselin' (1988) <doi:10.1007/978-94-015-7799-1>. Spatial two stage least
squares and spatial general method of moment models initially proposed by
'Kelejian' and 'Prucha' (1998) <doi:10.1023/A:1007707430416> and (1999)
<doi:10.1111/1468-2354.00027> are provided. Impact methods and MCMC
fitting methods proposed by 'LeSage' and 'Pace' (2009)
<doi:10.1201/9781420064254> are implemented for the family of
cross-sectional spatial regression models. Methods for fitting the log
determinant term in maximum likelihood and MCMC fitting are compared by
'Bivand et al.' (2013) <doi:10.1111/gean.12008>, and model fitting methods
by 'Bivand' and 'Piras' (2015) <doi:10.18637/jss.v063.i18>; both of these
articles include extensive lists of references. 'spatialreg' >= 1.1-*
corresponded to 'spdep' >= 1.1-1, in which the model fitting functions
were deprecated and passed through to 'spatialreg', but masked those in
'spatialreg'. From versions 1.2-*, the functions have been made defunct in
'spdep'.

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
