%global __brp_check_rpaths %{nil}
%global packname  mcboost
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Calibration Boosting

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.13.6
BuildRequires:    R-CRAN-mlr3misc >= 0.8.0
BuildRequires:    R-CRAN-mlr3proba >= 0.4.0
BuildRequires:    R-CRAN-mlr3pipelines >= 0.3.0
BuildRequires:    R-CRAN-mlr3 >= 0.10
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-data.table >= 1.13.6
Requires:         R-CRAN-mlr3misc >= 0.8.0
Requires:         R-CRAN-mlr3proba >= 0.4.0
Requires:         R-CRAN-mlr3pipelines >= 0.3.0
Requires:         R-CRAN-mlr3 >= 0.10
Requires:         R-CRAN-backports 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-glmnet 

%description
Implements 'Multi-Calibration Boosting' (2018)
<https://proceedings.mlr.press/v80/hebert-johnson18a.html> and
'Multi-Accuracy Boosting' (2019) <arXiv:1805.12317> for the
multi-calibration of a machine learning model's prediction. 'MCBoost'
updates predictions for sub-groups in an iterative fashion in order to
mitigate biases like poor calibration or large accuracy differences across
subgroups. Multi-Calibration works best in scenarios where the underlying
data & labels are unbiased, but resulting models are. This is often the
case, e.g. when an algorithm fits a majority population while ignoring or
under-fitting minority populations.

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
