%global packname  greeks
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivities of Prices of Financial Options

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 

%description
Methods to calculate sensitivities of financial option prices for European
and Asian options in the Black Scholes model. Classical formulas are
implemented for European options in the Black Scholes Model, as is
presented in Hull, J. C. (2017). Options, Futures, and Other Derivatives,
Global Edition (9th Edition). Pearson. In the case of Asian options,
Malliavin Monte Carlo Greeks are implemented, see Hudde, A. & Rüschendorf,
L. (2016). European and Asian Malliavin Monte Carlo Greeks for general
Jump Diffusions with nonvanishing Brownian motion part.
<arXiv:1603.00920>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
