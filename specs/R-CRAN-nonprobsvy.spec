%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonprobsvy
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Inference Based on Non-Probability Samples

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-survey 
Requires:         R-CRAN-maxLik 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-formula.tools 

%description
Statistical inference with non-probability samples when auxiliary
information from external sources such as probability samples or
population totals or means is available. The package implements various
methods such as inverse probability (propensity score) weighting, mass
imputation and doubly robust approach. Details can be found in: Chen et
al. (2020) <doi:10.1080/01621459.2019.1677241>, Yang et al. (2020)
<doi:10.1111/rssb.12354>, Kim et al. (2021) <doi:10.1111/rssa.12696>, Yang
et al. (2021)
<https://www150.statcan.gc.ca/n1/pub/12-001-x/2021001/article/00004-eng.htm>
and Wu (2022)
<https://www150.statcan.gc.ca/n1/pub/12-001-x/2022002/article/00002-eng.htm>.
For details on the package and its functionalities see
<doi:10.48550/arXiv.2504.04255>.

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
