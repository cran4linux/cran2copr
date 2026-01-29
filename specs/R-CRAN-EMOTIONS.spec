%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMOTIONS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Models for Lactation Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-splines 
Requires:         R-CRAN-tibble 

%description
Lactation curves describe temporal changes in milk yield and are key to
breeding and managing dairy animals more efficiently. The use of ensemble
modeling, which consists of combining predictions from multiple models,
has the potential to yields more accurate and robust estimates of
lactation patterns than relying solely on single model estimates. The
package EMOTIONS fits 47 models for lactation curves and creates ensemble
models using model averaging based on Akaike information criterion (AIC),
Bayesian information criterion (BIC), root mean square percentage error
(RMSPE) and mean squared error (MAE), variance of the predictions, cosine
similarity for each model's predictions, and Bayesian Model Average (BMA).
The daily production values predicted through the ensemble models can be
used to estimate resilience indicators in the package. The package allows
the graphical visualization of the model ranks and the predicted lactation
curves. Additionally, the packages allows the user to detect milk loss
events and estimate residual-based resilience indicators.

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
