%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  uniml
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Predictive Modeling Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-mlr3filters 
BuildRequires:    R-CRAN-mlr3fselect 
BuildRequires:    R-CRAN-mlr3tuning 
BuildRequires:    R-CRAN-mlr3measures 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-mlr3misc 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Boruta 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-shapviz 
BuildRequires:    R-CRAN-kernelshap 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-mlr3filters 
Requires:         R-CRAN-mlr3fselect 
Requires:         R-CRAN-mlr3tuning 
Requires:         R-CRAN-mlr3measures 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-mlr3misc 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Boruta 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-shapviz 
Requires:         R-CRAN-kernelshap 

%description
A unified toolkit for binary and multiclass classification modelling that
chains preprocessing, feature selection, model training and tuning,
evaluation, visualization, and SHAP interpretability behind one set of
objects, while keeping a strict separation between the data that fits a
model and the data that judges it. Models, tasks, resampling, and tuning
are 'mlr3' objects, multiple imputation is pooled with Rubin's rules, and
results are exported in a layout that can be reopened outside R.

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
