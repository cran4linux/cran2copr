%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLwrap
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Modelling for Everyone

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-vip 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-innsight 
BuildRequires:    R-CRAN-fastshap 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-vip 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-innsight 
Requires:         R-CRAN-fastshap 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-scales 

%description
A minimal library specifically designed to make the estimation of Machine
Learning (ML) techniques as easy and accessible as possible, particularly
within the framework of the Knowledge Discovery in Databases (KDD) process
in data mining. The package provides essential tools to structure and
execute each stage of a predictive or classification modeling workflow,
aligning closely with the fundamental steps of the KDD methodology, from
data selection and preparation, through model building and tuning, to the
interpretation and evaluation of results using Sensitivity Analysis. The
'MLwrap' workflow is organized into four core steps; preprocessing(),
build_model(), fine_tuning(), and sensitivity_analysis(). These steps
correspond, respectively, to data preparation and transformation, model
construction, hyperparameter optimization, and sensitivity analysis. The
user can access comprehensive model evaluation results including fit
assessment metrics, plots, predictions, and performance diagnostics for ML
models implemented through 'Neural Networks', 'Random Forest', 'XGBoost'
(Extreme Gradient Boosting), and 'Support Vector Machines' (SVM)
algorithms. By streamlining these phases, 'MLwrap' aims to simplify the
implementation of ML techniques, allowing analysts and data scientists to
focus on extracting actionable insights and meaningful patterns from large
datasets, in line with the objectives of the KDD process.

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
