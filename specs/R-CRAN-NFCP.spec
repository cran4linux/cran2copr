%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NFCP
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          N-Factor Commodity Pricing Through Term Structure Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FKF.SP 
BuildRequires:    R-CRAN-LSMRealOptions 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-FKF.SP 
Requires:         R-CRAN-LSMRealOptions 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-rgenoud 
Requires:         R-stats 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-Rdpack 

%description
Commodity pricing models are (systems of) stochastic differential
equations that are utilized for the valuation and hedging of commodity
contingent claims (i.e. derivative products on the commodity) and other
commodity related investments. Commodity pricing models that capture
market dynamics are of great importance to commodity market participants
in order to exercise sound investment and risk-management strategies.
Parameters of commodity pricing models are estimated through maximum
likelihood estimation, using available term structure futures data of a
commodity. 'NFCP' (n-factor commodity pricing) provides a framework for
the modeling, parameter estimation, probabilistic forecasting, option
valuation and simulation of commodity prices through state space and Monte
Carlo methods, risk-neutral valuation and Kalman filtering. 'NFCP' allows
the commodity pricing model to consist of n correlated factors, with both
random walk and mean-reverting elements. The n-factor commodity pricing
model framework was first presented in the work of Cortazar and Naranjo
(2006) <doi:10.1002/fut.20198>. Examples presented in 'NFCP' replicate the
two-factor crude oil commodity pricing model presented in the prolific
work of Schwartz and Smith (2000) <doi:10.1287/mnsc.46.7.893.12034> with
the approximate term structure futures data applied within this study
provided in the 'NFCP' package.

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
