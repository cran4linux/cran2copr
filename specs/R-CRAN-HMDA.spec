%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HMDA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Holistic Multimodel Domain Analysis for Exploratory Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-h2o >= 3.34.0.0
BuildRequires:    R-CRAN-psych >= 2.4.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-splitTools >= 1.0.1
BuildRequires:    R-CRAN-shapley >= 0.5
BuildRequires:    R-CRAN-h2otools >= 0.4
BuildRequires:    R-CRAN-autoEnsemble >= 0.3
Requires:         R-CRAN-curl >= 4.3.0
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-h2o >= 3.34.0.0
Requires:         R-CRAN-psych >= 2.4.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-splitTools >= 1.0.1
Requires:         R-CRAN-shapley >= 0.5
Requires:         R-CRAN-h2otools >= 0.4
Requires:         R-CRAN-autoEnsemble >= 0.3

%description
Holistic Multimodel Domain Analysis (HMDA) is a robust and transparent
framework designed for exploratory machine learning research, aiming to
enhance the process of feature assessment and selection. HMDA addresses
key limitations of traditional machine learning methods by evaluating the
consistency across multiple high-performing models within a fine-tuned
modeling grid, thereby improving the interpretability and reliability of
feature importance assessments. Specifically, it computes Weighted Mean
SHapley Additive exPlanations (WMSHAP), which aggregate feature
contributions from multiple models based on weighted performance metrics.
HMDA also provides confidence intervals to demonstrate the stability of
these feature importance estimates. This framework is particularly
beneficial for analyzing complex, multidimensional datasets common in
health research, supporting reliable exploration of mental health outcomes
such as suicidal ideation, suicide attempts, and other psychological
conditions. Additionally, HMDA includes automated procedures for feature
selection based on WMSHAP ratios and performs dimension reduction analyses
to identify underlying structures among features. For more details see
Haghish (2025) <doi:10.13140/RG.2.2.32473.63846>.

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
