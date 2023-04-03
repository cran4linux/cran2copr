%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metrica
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Performance Metrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-ggpp 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-energy 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-ggpp 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-energy 

%description
A compilation of more than 80 functions designed to quantitatively and
visually evaluate prediction performance of regression (continuous
variables) and classification (categorical variables) of point-forecast
models (e.g. APSIM, DSSAT, DNDC, supervised Machine Learning). For
regression, it includes functions to generate plots (scatter, tiles,
density, & Bland-Altman plot), and to estimate error metrics (e.g. MBE,
MAE, RMSE), error decomposition (e.g. lack of accuracy-precision), model
efficiency (e.g. NSE, E1, KGE), indices of agreement (e.g. d, RAC),
goodness of fit (e.g. r, R2), adjusted correlation coefficients (e.g. CCC,
dcorr), symmetric regression coefficients (intercept, slope), and mean
absolute scaled error (MASE) for time series predictions. For
classification (binomial and multinomial), it offers functions to generate
and plot confusion matrices, and to estimate performance metrics such as
accuracy, precision, recall, specificity, F-score, Cohen's Kappa, G-mean,
and many more. For more details visit the vignettes
<https://adriancorrendo.github.io/metrica/>.

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
