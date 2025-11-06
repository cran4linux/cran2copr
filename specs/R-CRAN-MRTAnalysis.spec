%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRTAnalysis
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Proximal, Distal, and Mediated Causal Excursion Effects for Micro-Randomized Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 

%description
Provides methods to analyze micro-randomized trials (MRTs) with binary
treatment options.  Supports three types of analyses: (1) proximal causal
excursion effects, including weighted and centered least squares (WCLS)
for continuous proximal outcomes by Boruvka et al. (2018)
<doi:10.1080/01621459.2017.1305274> and the estimator for marginal
excursion effect (EMEE) for binary proximal outcomes by Qian et al. (2021)
<doi:10.1093/biomet/asaa070>; (2) distal causal excursion effects (DCEE)
for continuous distal outcomes using a two-stage estimator by Qian (2025)
<doi:10.48550/arXiv.2502.13500>; and (3) mediated causal excursion effects
(MCEE) for continuous distal outcomes, estimating natural direct and
indirect excursion effects in the presence of time-varying mediators by
Qian (2025) <doi:10.48550/arXiv.2506.20027>.

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
