%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitmix
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Finite Mixture Model Fitting of Lifespan Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Fits the lifespan datasets of biological systems such as yeast, fruit
flies, and other similar biological units with well-known finite mixture
models introduced by Farewell V. (1982) <doi:10.2307/2529885> and
Al-Hussaini et al. (2000) <doi:10.1080/00949650008812033>. Estimates
parameter space fitting of a lifespan dataset with finite mixtures of
parametric distributions. Computes the following tasks; 1) Estimates
parameter space of the finite mixture model by implementing the
expectation maximization (EM) algorithm. 2) Finds a sequence of four
goodness-of-fit measures consist of Akaike Information Criterion (AIC),
Bayesian Information Criterion (BIC), Kolmogorov-Smirnov (KS), and
log-likelihood (log-likelihood) statistics. 3)The initial values is
determined by k-means clustering.

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
