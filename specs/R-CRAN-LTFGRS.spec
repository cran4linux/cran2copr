%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LTFGRS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of Several Phenotype-Based Family Genetic Risk Scores

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-batchmeans 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-batchmeans 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-tidyr 

%description
Implementation of several phenotype-based family genetic risk scores with
unified input data and data preparation functions to help facilitate the
required data preparation and management. The implemented family genetic
risk scores are the extended liability threshold model conditional on
family history from Pedersen (2022) <doi:10.1016/j.ajhg.2022.01.009> and
Pedersen (2023) <https://www.nature.com/articles/s41467-023-41210-z>,
Pearson-Aitken Family Genetic Risk Scores from Krebs (2024)
<doi:10.1016/j.ajhg.2024.09.009>, and family genetic risk score from
Kendler (2021) <doi:10.1001/jamapsychiatry.2021.0336>.

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
