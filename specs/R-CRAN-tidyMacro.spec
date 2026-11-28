%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyMacro
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Vector Autoregressions and Local Projections via 'C++'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 

%description
Estimation and identification of structural vector autoregressions and
local projections, with a compiled 'C++' backend. Shocks can be identified
by short-run (recursive) restrictions, long-run restrictions following
Blanchard and Quah (1989) <https://www.jstor.org/stable/1827924>, maximum
forecast error variance share following Uhlig (2005)
<doi:10.1016/j.jmoneco.2004.05.007>, external instruments (proxy SVAR)
following Mertens and Ravn (2013) <doi:10.1257/aer.103.4.1212> and Kaenzig
(2021) <doi:10.1257/aer.20190964>, heteroskedasticity across regimes, and
sign or narrative sign restrictions. Local projections follow Jorda (2005)
<doi:10.1257/0002828053828518> and cover instrumental variables,
state-dependent and nonlinear specifications, panel data as in Mian, Sufi
and Verner (2017) <doi:10.1093/qje/qjx017>, and the
difference-in-differences estimator of Dube, Girardi, Jorda and Taylor
(2025) <doi:10.1002/jae.70000>. Inference uses residual, wild and
moving-block bootstraps, heteroskedasticity and autocorrelation consistent
standard errors, and one-way or two-way cluster-robust standard errors.

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
