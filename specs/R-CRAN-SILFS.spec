%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SILFS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Subgroup Identification with Latent Factor Structure

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Ckmeans.1d.dp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-Ckmeans.1d.dp 

%description
In various domains, many datasets exhibit both high variable dependency
and group structures, which necessitates their simultaneous estimation.
This package provides functions for two subgroup identification methods
based on penalized functions, both of which utilize factor model
structures to adapt to data with cross-sectional dependency. The first
method is the Subgroup Identification with Latent Factor Structure Method
(SILFSM) we proposed. By employing Center-Augmented Regularization and
factor structures, the SILFSM effectively eliminates data dependencies
while identifying subgroups within datasets. For this model, we offer
optimization functions based on two different methods: Coordinate Descent
and our newly developed Difference of Convex-Alternating Direction Method
of Multipliers (DC-ADMM) algorithms; the latter can be applied to cases
where the distance function in Center-Augmented Regularization takes L1
and L2 forms. The other method is the Factor-Adjusted Pairwise Fusion
Penalty (FA-PFP) model, which incorporates factor augmentation into the
Pairwise Fusion Penalty (PFP) developed by Ma, S. and Huang, J. (2017)
<doi:10.1080/01621459.2016.1148039>. Additionally, we provide a function
for the Standard CAR (S-CAR) method, which does not consider the
dependency and is for comparative analysis with other approaches.
Furthermore, functions based on the Bayesian Information Criterion (BIC)
of the SILFSM and the FA-PFP method are also included in 'SILFS' for
selecting tuning parameters. For more details of Subgroup Identification
with Latent Factor Structure Method, please refer to He et al. (2024)
<doi:10.48550/arXiv.2407.00882>.

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
