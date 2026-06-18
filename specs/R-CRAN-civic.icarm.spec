%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  civic.icarm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretable Civic-Accountable and Responsible Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 

%description
A general-purpose framework for Interpretable Civic-Accountable and
Responsible Machine Learning (ICARM). Works with any clean tabular data
and automatically detects whether a task is binary classification,
multi-class classification, or regression from the target variable type.
Provides a single unified entry point civic_fit() alongside tidy
interfaces for global and local model explanations, group-level fairness
auditing, probability calibration, multi-model comparison, threshold
analysis, and reproducible audit trails. Designed to support the
DataCitizen-Pro research agenda at Ludwigsburg University of Education:
developing data literacy, statistical reasoning, and democratic judgment
formation in civic and political teacher education. References: Biecek
(2018) <doi:10.18637/jss.v085.i04>, Kuhn (2008)
<doi:10.18637/jss.v028.i05>, Awe (2025)
<https://github.com/Olawaleawe/civic.icarm>.

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
