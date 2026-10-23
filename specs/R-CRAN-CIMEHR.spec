%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CIMEHR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal EHR Analysis with Informative Visits and Recording

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Longitudinal outcomes in electronic health records (EHR) are seen only
when a patient visits and the outcome is recorded at that visit, and both
processes can depend on the patient's latent health. The package fits the
CIMEHR estimator for this setting, a three-stage procedure linked by a
shared latent factor: a frailty partial likelihood for the visiting
process, a pairwise likelihood for the recording (observation) process,
and an estimating equation for the outcome. Spline and higher-order
Laplace variants are included, together with comparison methods (summary
statistics, linear mixed models, Lin-Ying, Liang, pairwise likelihood,
joint models, inverse intensity rate ratio weighting and balancing,
multiple imputation, linear increments and EHRJoint) behind one common
interface. Methods are described in Yang, Shi, and Mukherjee (2026)
<doi:10.48550/arXiv.2602.15374>.

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
