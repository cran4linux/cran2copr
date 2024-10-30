%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sfaR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Frontier Analysis Routines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-marqLevAlg 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mnorm 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-trustOptim 
BuildRequires:    R-CRAN-ucminf 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-marqLevAlg 
Requires:         R-CRAN-maxLik 
Requires:         R-methods 
Requires:         R-CRAN-mnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-qrng 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-trustOptim 
Requires:         R-CRAN-ucminf 

%description
Maximum likelihood estimation for stochastic frontier analysis (SFA) of
production (profit) and cost functions. The package includes the basic
stochastic frontier for cross-sectional or pooled data with several
distributions for the one-sided error term (i.e., Rayleigh, gamma,
Weibull, lognormal, uniform, generalized exponential and truncated skewed
Laplace), the latent class stochastic frontier model (LCM) as described in
Dakpo et al. (2021) <doi:10.1111/1477-9552.12422>, for cross-sectional and
pooled data, and the sample selection model as described in Greene (2010)
<doi:10.1007/s11123-009-0159-1>, and applied in Dakpo et al. (2021)
<doi:10.1111/agec.12683>.  Several possibilities in terms of optimization
algorithms are proposed.

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
