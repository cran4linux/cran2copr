%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greeks
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivities of Prices of Financial Options and Implied Volatilites

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tidyr 

%description
Methods to calculate sensitivities of financial option prices for
European, Asian, American and Digital Options options in the Black Scholes
model, and in more general jump diffusion models. A shiny app to
interactively view plot the results is included. Furthermore, methods to
compute implied volatilities are provided for a wide range of option types
and custom payoff functions. Classical formulas are implemented for
European options in the Black Scholes Model, as is presented in Hull, J.
C. (2017). Options, Futures, and Other Derivatives, Global Edition (9th
Edition). Pearson. In the case of Asian options, Malliavin Monte Carlo
Greeks are implemented, see Hudde, A. & Rüschendorf, L. (2016). European
and Asian Greeks for exponential Lévy processes. <arXiv:1603.00920>. For
American options, the Binomial Tree Method is implemented, as is presented
in Hull, J. C. (2017).

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
