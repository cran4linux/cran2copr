%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaselection
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analytic Selection Models for Dependent Effect Sizes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-simhelpers >= 0.3.1
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-simhelpers >= 0.3.1
Requires:         R-CRAN-Formula 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Rdpack 

%description
Fits a flexible class of p-value selection models for meta-analysis and
meta-regression models, providing standard errors and confidence intervals
based on either cluster-robust variance estimators (i.e., sandwich
estimators) or cluster-level bootstrapping to handle dependent effect size
estimates, as described in Pustejovsky, Citkowicz, and Joshi (2025)
<DOI:10.31222/osf.io/qg5x6_v1> and Citkowicz, Pustejovsky, and Joshi
(2026) <DOI:10.31222/osf.io/wjpxk_v1>. Supported models include
generalizations of the step-function selection model as proposed by Vevea
and Hedges (1995) <DOI:10.1007/BF02294384> and the beta-function selection
model as proposed by Citkowicz and Vevea (2017) <DOI:10.1037/met0000119>.

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
