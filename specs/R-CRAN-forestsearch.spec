%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forestsearch
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Subgroup Identification in Clinical Trials with Survival Endpoints

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future.callr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-policytree 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-weightedsurv 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future.callr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-policytree 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-weightedsurv 

%description
Implements statistical methods for exploratory subgroup identification in
clinical trials with survival endpoints. Provides tools for identifying
patient subgroups with differential treatment effects using machine
learning approaches including Generalized Random Forests (GRF), LASSO
regularization, and exhaustive combinatorial search algorithms. Features
bootstrap bias correction using infinitesimal jackknife methods to address
selection bias in post-hoc analyses. Designed for clinical researchers
conducting exploratory subgroup analyses in randomized controlled trials,
particularly for multi-regional clinical trials (MRCT) requiring regional
consistency evaluation. Supports both accelerated failure time (AFT) and
Cox proportional hazards models with comprehensive diagnostic and
visualization tools. Methods are described in León et al. (2024)
<doi:10.1002/sim.10163>.

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
