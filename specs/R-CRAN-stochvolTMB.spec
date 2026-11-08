%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stochvolTMB
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood Estimation of Stochastic Volatility Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-sn 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-MASS 

%description
Parameter estimation for stochastic volatility models using maximum
likelihood. The latent log-volatility is integrated out of the likelihood
using the Laplace approximation. The models are fitted via 'TMB' (Template
Model Builder) (Kristensen, Nielsen, Berg, Skaug, and Bell (2016)
<doi:10.18637/jss.v070.i05>). The observation error can be Gaussian, t,
skew-Gaussian or skew t (Jones and Faddy (2003)
<doi:10.1111/1467-9868.00378>), with or without leverage. Exact
one-step-ahead residuals, Value at Risk and Expected Shortfall are
calculated with a filter on a grid for the log-volatility, and the Value
at Risk can be backtested with the tests of Kupiec (1995)
<doi:10.3905/jod.1995.407942> and Christoffersen (1998)
<doi:10.2307/2527341>.

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
