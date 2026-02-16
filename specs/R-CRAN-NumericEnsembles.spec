%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NumericEnsembles
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatically Runs 18 Individual and 14 Ensembles of Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-brnn 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-olsrr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-reactablefmtr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vip 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-brnn 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-olsrr 
Requires:         R-parallel 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-reactablefmtr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tree 
Requires:         R-utils 
Requires:         R-CRAN-vip 
Requires:         R-CRAN-xgboost 

%description
Automatically runs 18 individual models and 14 ensembles on numeric data,
for a total of 32 models. The package automatically returns complete
results on all 32 models, 25 charts and six tables. The user simply
provides the tidy data, and answers a few questions (for example, how many
times would you like to resample the data). From there the package
randomly splits the data into train, test and validation sets as the user
requests (for example, train = 0.60, test = 0.20, validation = 0.20), fits
each of models on the training data, makes predictions on the test and
validation sets, measures root mean squared error (RMSE), removes features
above a user-set level of Variance Inflation Factor, and has several
optional features including scaling all numeric data, four different ways
to handle strings in the data. Perhaps the most significant feature is the
package's ability to make predictions using the 32 pre trained models on
totally new (untrained) data if the user selects that feature. This
feature alone represents a very effective solution to the issue of
reproducibility of models in data science. The package can also randomly
resample the data as many times as the user sets, thus giving more
accurate results than a single run. The graphs provide many results that
are not typically found. For example, the package automatically calculates
the Kolmogorov-Smirnov test for each of the 32 models and plots a bar
chart of the results, a bias bar chart of each of the 32 models, as well
as several plots for exploratory data analysis (automatic histograms of
the numeric data, automatic histograms of the numeric data). The package
also automatically creates a summary report that can be both sorted and
searched for each of the 32 models, including RMSE, bias, train RMSE, test
RMSE, validation RMSE, overfitting and duration. The best results on the
holdout data typically beat the best results in data science competitions
and published results for the same data set.

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
