%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bamlss
%global packver   1.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Additive Models for Location, Scale, and Shape (and Beyond)

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-distributions3 >= 0.2.1
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-distributions3 >= 0.2.1
Requires:         R-CRAN-coda 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-parallel 

%description
Infrastructure for estimating probabilistic distributional regression
models in a Bayesian framework. The distribution parameters may capture
location, scale, shape, etc. and every parameter may depend on complex
additive terms (fixed, random, smooth, spatial, etc.) similar to a
generalized additive model. The conceptual and computational framework is
introduced in Umlauf, Klein, Zeileis (2019)
<doi:10.1080/10618600.2017.1407325> and the R package in Umlauf, Klein,
Simon, Zeileis (2021) <doi:10.18637/jss.v100.i04>.

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
