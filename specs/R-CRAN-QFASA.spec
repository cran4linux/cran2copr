%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QFASA
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Fatty Acid Signature Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-bootstrap 
BuildRequires:    R-CRAN-Compositional 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-bootstrap 
Requires:         R-CRAN-Compositional 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvtnorm 

%description
Accurate estimates of the diets of predators are required in many areas of
ecology, but for many species current methods are imprecise, limited to
the last meal, and often biased. The diversity of fatty acids and their
patterns in organisms, coupled with the narrow limitations on their
biosynthesis, properties of digestion in monogastric animals, and the
prevalence of large storage reservoirs of lipid in many predators, led to
the development of quantitative fatty acid signature analysis (QFASA) to
study predator diets.

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
