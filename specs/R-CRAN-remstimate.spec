%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remstimate
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimization Frameworks for Tie-Oriented and Actor-Oriented Relational Event Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-remify >= 4.1.0
BuildRequires:    R-CRAN-remstats >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-remify >= 4.1.0
Requires:         R-CRAN-remstats >= 4.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-mvnfast 

%description
Tools for fitting, diagnosing, and analyzing tie-oriented and
actor-oriented relational event models, under both frequentist and
Bayesian approaches. The package supports tie-oriented modeling (Butts,
2008, <doi:10.1111/j.1467-9531.2008.00203.x>) and an actor-oriented
modeling framework (Stadtfeld et al., 2017, <doi:10.15195/v4.a14>), with
additional model diagnostics and goodness-of-fit tools. Interfaces to
estimation backends provide a range of extensions: random-effects
(frailty) relational event models capturing sender, receiver, and dyadic
heterogeneity (Juozaitiene & Wit 2024, <doi:10.1007/s11336-024-09952-x>;
Mulder & Hoff, 2024, <doi:10.1214/24-AOAS1885>), finite mixture and dyadic
latent class models for unobserved dyadic heterogeneity (Lakdawala et al.,
2026, <doi:10.1016/j.socnet.2026.06.006>), penalized estimation via the
lasso, ridge, and elastic net (Tibshirani, R., 1996,
<doi:10.1111/j.2517-6161.1996.tb02080.x>; Karimova et al., 2023,
<doi:10.1016/j.socnet.2023.02.006>), and approximate Bayesian
regularization (Karimova et al., 2025, <doi:10.1016/j.jmp.2025.102925>).
Modeling of events with a duration is also supported (Lakdawala et al.,
2026, <doi:10.48550/arXiv.2602.21000>) and moving window relational event
models (Mulder & Leenders, 2019, <doi:10.1016/j.chaos.2018.11.027>;
Meijerink et al., 2023, <doi:10.1371/journal.pone.0272309>).

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
