%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rd2d
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Inference for Boundary Discontinuity Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggplot2 

%description
Provides pointwise and uniform estimation and inference methods for
boundary discontinuity (BD) designs, a causal inference design that
generalizes univariate regression discontinuity (RD) designs to settings
with bivariate scores. Implements local polynomial methods for
location-based and distance-based analyses, including sharp and fuzzy
designs, data-driven bandwidth selection, pointwise confidence intervals,
and uniform confidence bands. Methodology is developed in Cattaneo,
Titiunik, and Yu (2026) <doi:10.48550/arXiv.2505.05670> for location-based
methods and Cattaneo, Titiunik, and Yu (2026)
<doi:10.48550/arXiv.2510.26051> for distance-based methods. For an
overview and empirical guidance, see Cattaneo, Titiunik, and Yu (2026)
<doi:10.48550/arXiv.2511.06474>. The companion software article is
Cattaneo, Titiunik, and Yu (2025) <doi:10.48550/arXiv.2505.07989>.

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
