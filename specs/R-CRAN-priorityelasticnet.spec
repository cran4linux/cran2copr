%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  priorityelasticnet
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Analysis of Multi-Omics Data Using an Offset-Based Method

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-cvms 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-PRROC 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-cvms 

%description
Priority-ElasticNet extends the Priority-LASSO method (Klau et al. (2018)
<doi:10.1186/s12859-018-2344-6>) by incorporating the ElasticNet penalty,
allowing for both L1 and L2 regularization. This approach fits successive
ElasticNet models for several blocks of (omics) data with different
priorities, using the predicted values from each block as an offset for
the subsequent block. It also offers robust options to handle block-wise
missingness in multi-omics data, improving the flexibility and
applicability of the model in the presence of incomplete datasets.

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
