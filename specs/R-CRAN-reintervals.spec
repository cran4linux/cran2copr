%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reintervals
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence, Prediction, Tolerance, and New-Group-Mean Intervals for Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 

%description
Confidence, prediction, tolerance, and new-group-mean (also called CInew
or new-batch-mean) intervals for linear mixed models fitted with 'lme4'
('lmerMod' objects), returned through one uniform interface. Several
validated interval engines are provided and selected automatically for the
fitted model, with a manual override: an expected-mean-square, modified
large-sample construction for random-intercept models (Francq, Lin and
Hoyer (2019) <doi:10.1002/sim.8386>); a restricted-maximum- likelihood
closed form for random-slope models; an unweighted lot-mean
analysis-of-variance closed form for unbalanced single-observation
fixed-slope stability designs (Montes, Burdick and Leblond (2019)
<doi:10.5731/pdajpst.2018.008839>) and, without a covariate, for the
one-way random-effects model (Hoffman and Kringle (2005)
<doi:10.1081/BIP-200048826>); and a generalized-pivotal-quantity Monte
Carlo engine (Oliva-Aviles and Hauser (2025)
<doi:10.1080/00401706.2024.2407324>). Intervals are two-sided or
one-sided; one-sided tolerance limits follow Hoffman (2010)
<doi:10.1198/TECH.2010.09171>. General fixed effects are supported for
random-intercept models; random-slope models are supported for a single
continuous covariate (the stability design). The methods serve general
linear-mixed-model interval estimation, with particular support for
pharmaceutical stability and shelf-life work and for bioassay applications
through the tolerance and new-group-mean intervals.

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
