%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mev
%global packver   1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling of Extreme Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-alabama 
Requires:         R-methods 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 

%description
Various tools for the analysis of univariate, multivariate and functional
extremes. Exact simulation from max-stable processes [Dombry, Engelke and
Oesting (2016) <doi:10.1093/biomet/asw008>, R-Pareto processes for various
parametric models, including Brown-Resnick (Wadsworth and Tawn, 2014,
<doi:10.1093/biomet/ast042>) and Extremal Student (Thibaud and Opitz,
2015, <doi:10.1093/biomet/asv045>). Threshold selection methods, including
Wadsworth (2016) <doi:10.1080/00401706.2014.998345>, and Northrop and
Coleman (2014) <doi:10.1007/s10687-014-0183-z>. Multivariate extreme
diagnostics. Estimation and likelihoods for univariate extremes, e.g.,
Coles (2001) <doi:10.1007/978-1-4471-3675-0>.

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
