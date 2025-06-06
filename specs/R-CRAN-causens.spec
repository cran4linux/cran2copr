%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causens
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Causal Sensitivity Analyses Using Various Statistical Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
While data from randomized experiments remain the gold standard for causal
inference, estimation of causal estimands from observational data is
possible through various confounding adjustment methods. However, the
challenge of unmeasured confounding remains a concern in causal inference,
where failure to account for unmeasured confounders can lead to biased
estimates of causal estimands. Sensitivity analysis within the framework
of causal inference can help adjust for possible unmeasured confounding.
In `causens`, three main methods are implemented: adjustment via
sensitivity functions (Brumback, Hernán, Haneuse, and Robins (2004)
<doi:10.1002/sim.1657> and Li, Shen, Wu, and Li (2011)
<doi:10.1093/aje/kwr096>), Bayesian parametric modelling and Monte Carlo
approaches (McCandless, Lawrence C and Gustafson, Paul (2017)
<doi:10.1002/sim.7298>).

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
