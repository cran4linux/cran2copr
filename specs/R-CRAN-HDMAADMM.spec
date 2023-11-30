%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDMAADMM
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          ADMM for High-Dimensional Mediation Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-RcppEigen 

%description
We use the Alternating Direction Method of Multipliers (ADMM) for
parameter estimation in high-dimensional, single-modality mediation
models. To improve the sensitivity and specificity of estimated mediation
effects, we offer the sure independence screening (SIS) function for
dimension reduction. The available penalty options include Lasso, Elastic
Net, Pathway Lasso, and Network-constrained Penalty. The methods employed
in the package are based on Boyd, S., Parikh, N., Chu, E., Peleato, B., &
Eckstein, J. (2011). <doi:10.1561/2200000016>, Fan, J., & Lv, J. (2008)
<doi:10.1111/j.1467-9868.2008.00674.x>, Li, C., & Li, H. (2008)
<doi:10.1093/bioinformatics/btn081>, Tibshirani, R. (1996)
<doi:10.1111/j.2517-6161.1996.tb02080.x>, Zhao, Y., & Luo, X. (2022)
<doi:10.4310/21-sii673>, and Zou, H., & Hastie, T. (2005)
<doi:10.1111/j.1467-9868.2005.00503.x>.

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
