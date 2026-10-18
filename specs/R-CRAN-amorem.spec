%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  amorem
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Augmented Modelling of Relational Events

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-survival >= 3.7.3
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-survival >= 3.7.3
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-withr 

%description
An integrated workflow for relational event models, in which timestamped
interactions among actors arrive in continuous time and the event rate
depends on the history of the network itself. Event streams are simulated
by an exact Gillespie kernel or an approximate tau-leap kernel; non-events
are drawn by case-control sampling in the manner of Lerner and Lomi (2020)
<doi:10.1017/nws.2019.57>, or from a time-shifted copy of the process so
that covariates shared by all dyads at a given time remain estimable
(Lembo et al. 2025, <doi:10.1093/jrsssc/qlaf058>); the timing- and
closure-based endogenous statistics of Juozaitiene and Wit (2024)
<doi:10.1093/jrsssa/qnae132> are computed from that history; and one
front-end fits the resulting case-control data by conditional-logistic
partial likelihood, by penalised regression on its degenerate one-control
binomial form (which admits smooth, time-varying and actor random
effects), or by stochastic gradient descent, including the additive-spline
construction of Filippi-Mazzola and Wit (2024)
<doi:10.1093/jrsssc/qlae023>. Martingale-residual goodness-of-fit
diagnostics are provided for the linear fit, together with simulation and
statistic computation for relational hyper-events, a collection of
documented event logs from published interaction networks, and a
reconstructed El Nino index as a global covariate.

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
