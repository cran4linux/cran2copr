%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  randnet
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Random Network Model Estimation, Selection and Parameter Tuning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-AUC 
BuildRequires:    R-CRAN-sparseFLMM 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-poweRlaw 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-AUC 
Requires:         R-CRAN-sparseFLMM 
Requires:         R-CRAN-mgcv 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-poweRlaw 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-data.table 

%description
Model selection and parameter tuning procedures for a class of random
network models. The model selection can be done by a general
cross-validation framework called ECV from Li et. al. (2016)
<arXiv:1612.04717> . Several other model-based and task-specific methods
are also included, such as NCV from Chen and Lei (2016) <arXiv:1411.1715>,
likelihood ratio method from Wang and Bickel (2015) <arXiv:1502.02069>,
spectral methods from Le and Levina (2015) <arXiv:1507.00827>. Many
network analysis methods are also implemented, such as the regularized
spectral clustering (Amini et. al. 2013 <doi:10.1214/13-AOS1138>) and its
degree corrected version and graphon neighborhood smoothing (Zhang et. al.
2015 <arXiv:1509.08588>). It also includes the consensus clustering of Gao
et. al. (2014) <arXiv:1410.5837>, the method of moments estimation of
nomination SBM of Li et. al. (2020) <arxiv:2008.03652>, and the network
mixing method of Li and Le (2021) <arxiv:2106.02803>. It also includes the
informative core-periphery data processing method of Miao and Li (2021)
<arXiv:2101.06388>. The work to build and improve this package is
partially supported by the NSF grants DMS-2015298 and DMS-2015134.

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
