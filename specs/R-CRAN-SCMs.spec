%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCMs
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Specification Curve Analysis for Synthetic Control Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.1.2
BuildRequires:    R-CRAN-CVXR >= 1.9.0
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-ECOSolveR 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gridtext 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-tibble >= 3.1.2
Requires:         R-CRAN-CVXR >= 1.9.0
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ECOSolveR 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gridtext 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-generics 

%description
Estimates synthetic control models while exposing the implementation
choices that define the synthetic counterfactual: how matching variables
are constructed, how predictor weights are set, which constraints the
donor weights satisfy (simplex, lasso, ridge, penalized), whether an
intercept is included, and which outcome model corrects for bias (OLS,
ridge, lasso, augmented synthetic control). Runs specification-curve
analysis over a grid of these choices (Simonsohn, Simmons and Nelson
(2020) <doi:10.1038/s41562-020-0912-z>), with placebo-in-space and
bootstrap inference for single specifications and placebo inference for
the curve as a whole, and uses 'xgboost' models with SHAP values (Lundberg
and Lee (2017) <doi:10.48550/arXiv.1705.07874>) to show which choices
drive the estimates. Methods follow Abadie, Diamond and Hainmueller (2010)
<doi:10.1198/jasa.2009.ap08746>, Abadie (2021) <doi:10.1257/jel.20191450>,
Ben-Michael, Feller and Rothstein (2021)
<doi:10.1080/01621459.2021.1929245> and Chen and Guestrin (2016)
<doi:10.1145/2939672.2939785>.

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
