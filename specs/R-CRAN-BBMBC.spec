%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BBMBC
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Beta-Binomial Models for Evaluating Overdispersed B-Cell Phenotyping Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmmTMB 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for statistical power calculations to plan early-phase
vaccine and immunotherapy trials comparing rare, antigen-specific immune
cell frequencies. Originally designed for memory B-cell phenotyping
studies and generalizable to high-parameter flow cytometry assays across
vaccinology and immuno-oncology, the models overdispersed count
distributions using Beta-Binomial generalized linear models. Unlike
rank-based tests, this approach retains response magnitude information
while accounting for extra-binomial variation, small sample sizes, unequal
between-participant variability, and uncertainty in pilot estimates.
Includes method-of-moments dispersion estimation, likelihood ratio testing
across experimental arms, and Monte Carlo simulation to evaluate
statistical power with well-controlled empirical Type I error rates. This
workflow is directly motivated by the analysis of immunology data in
"Vaccination with mRNA-encoded membrane-anchored HIV envelope trimers
elicited tier 2 neutralizing antibodies in a phase 1 clinical trial"
(Parks et al. 2025) <doi:10.1126/scitranslmed.ady6831>.

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
