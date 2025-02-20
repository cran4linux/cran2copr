%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viralmodels
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Viral Load and CD4 Lymphocytes Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-workflowsets 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-workflowsets 

%description
Provides a comprehensive framework for building, evaluating, and
visualizing regression models for analyzing viral load and CD4 (Cluster of
Differentiation 4) lymphocytes data. It leverages the principles of the
tidymodels ecosystem of Max Kuhn and Hadley Wickham (2020)
<https://www.tidymodels.org> to offer a user-friendly experience in model
development. This package includes functions for data preprocessing,
feature engineering, model training, tuning, and evaluation, along with
visualization tools to enhance the interpretation of model results. It is
specifically designed for researchers in biostatistics, computational
biology, and HIV research who aim to perform reproducible and rigorous
analyses to gain insights into disease dynamics. The main focus is on
improving the understanding of the relationships between viral load, CD4
lymphocytes, and other relevant covariates to contribute to HIV research
and the visibility of vulnerable seropositive populations.

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
