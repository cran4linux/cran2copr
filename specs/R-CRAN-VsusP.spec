%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VsusP
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection Using Shrinkage Priors

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bayesreg 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-bayesreg 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Select variables from shrinkage-prior posterior coefficient draws using
sequential two-means clustering from Li and Pati (2017)
<doi:10.1016/j.csda.2016.10.008>. Estimate a signal count at each tuning
threshold and rank coefficients by posterior median absolute magnitude.
Accept supplied coefficient draws or fit Gaussian shrinkage regression
through 'bayesreg' or native ridge, horseshoe and spike-and-slab samplers.
Retain chain identities for diagnostics, prediction and posterior plots.
Also provide the signal adaptive variable selector of Ray and Bhattacharya
(2018) <doi:10.48550/arXiv.1810.09004>, decoupled shrinkage and selection
with the adaptive-L1 approximation of Hahn and Carvalho (2015)
<doi:10.1080/01621459.2014.993077>, optional exact two-cluster fitting,
basic two-means selection, exact-zero spike-and-slab inclusion summaries
and tuning sensitivity summaries.

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
