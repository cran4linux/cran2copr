%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vennabers
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Venn-Abers Classification and Regression Calibration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch

%description
Calibrates the predictions of classification and regression models with
Venn-Abers predictors. A Venn-Abers predictor turns the score of any model
into a pair of probabilities that contains a calibrated value when the
observations are independent and identically distributed (Vovk and Petej,
2014, <doi:10.48550/arXiv.1211.0025>); Inductive and Cross Venn-Abers
predictors make this practical for large data sets (Vovk, Petej and
Fedorova, 2015, <doi:10.48550/arXiv.1511.00213>). The package serves
analysts and researchers who need calibrated probabilities or prediction
bounds for binary classification, multiclass classification by one-vs-one
coupling (Manokhin, 2017,
<https://proceedings.mlr.press/v60/manokhin17a.html>) or one-vs-rest, and
regression (Petej and Vovk, 2026, <doi:10.48550/arXiv.2605.06646>).
Predictions of an existing model can be calibrated directly, or optional
'tidymodels' workflows fit the model, create the calibration splits and
tune the complete procedure. Diagnostics include the Brier score, log
loss, plots of fitted calibration maps and reliability diagrams with the
CORP (consistent, optimally binned, reproducible and
pool-adjacent-violators based) method of Dimitriadis, Gneiting and Jordan
(2021) <doi:10.1073/pnas.2016191118>.

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
