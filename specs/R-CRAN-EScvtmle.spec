%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EScvtmle
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Experiment-Selector CV-TMLE for Integration of Observational and RCT Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-SuperLearner >= 2.0.28
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-origami >= 1.0.5
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-SuperLearner >= 2.0.28
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-origami >= 1.0.5

%description
The experiment selector cross-validated targeted maximum likelihood
estimator (ES-CVTMLE) aims to select the experiment that optimizes the
bias-variance tradeoff for estimating a causal average treatment effect
(ATE) where different experiments may include a randomized controlled
trial (RCT) alone or an RCT combined with real-world data. Using
cross-validation, the ES-CVTMLE separates the selection of the optimal
experiment from the estimation of the ATE for the chosen experiment. The
estimated bias term in the selector is a function of the difference in
conditional mean outcome under control for the RCT compared to the
combined experiment. In order to help include truly unbiased external data
in the analysis, the estimated average treatment effect on a negative
control outcome may be added to the bias term in the selector. For more
details about this method, please see Dang et al. (2022)
<arXiv:2210.05802>.

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
