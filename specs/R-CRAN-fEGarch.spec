%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fEGarch
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of a Broad Family of EGARCH Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-smoots 
BuildRequires:    R-CRAN-esemifar 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-methods 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-smoots 
Requires:         R-CRAN-esemifar 
Requires:         R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-numDeriv 

%description
Implement and fit a variety of models from a very broad family of
exponential generalized autoregressive conditional heteroskedasticity
(EGARCH) models, such as a MEGARCH (modified EGARCH), FIEGARCH
(fractionally integrated EGARCH), FIMLog-GARCH (fractionally integrated
modulus Log-GARCH), and more. The FIMLog-GARCH as part of the EGARCH
family is discussed in Feng et al. (2023)
<https://econpapers.repec.org/paper/pdnciepap/156.htm>. For convenience
and the purpose of comparison, a variety of other popular GARCH-type
models, like an APARCH model, a fractionally integrated APARCH (FIAPARCH)
model, standard GARCH and fractionally integrated GARCH (FIGARCH) models,
GJR-GARCH and FIGJR-GARCH models, TGARCH and FITGARCH models, are
implemented. Models are fitted through quasi-maximum-likelihood
estimation.

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
