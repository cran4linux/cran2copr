%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesDLMfMRI
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis for Task-Based Fmri Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-neurobase 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mathjaxr 

%description
The 'BayesDLMfMRI' package performs statistical analysis for task-based
functional magnetic resonance imaging (fMRI) data at both individual and
group levels. The analysis to detect brain activation at the individual
level is based on modeling the fMRI signal using Matrix-Variate Dynamic
Linear Models (MDLM). The analysis for the group stage is based on
posterior distributions of the state parameter obtained from the modeling
at the individual level. In this way, this package offers several R
functions with different algorithms to perform inference on the state
parameter to assess brain activation for both individual and group stages.
Those functions allow for parallel computation when the analysis is
performed for the entire brain as well as analysis at specific voxels when
it is required. References: Cardona-Jiménez (2021)
<doi:10.1016/j.csda.2021.107297>; Cardona-Jiménez (2021)
<arXiv:2111.01318>.

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
