%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  obliqueRSF
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Oblique Random Forests for Right-Censored Time-to-Event Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Oblique random survival forests incorporate linear combinations of input
variables into random survival forests (Ishwaran, 2008
<DOI:10.1214/08-AOAS169>). Regularized Cox proportional hazard models
(Simon, 2016 <DOI:10.18637/jss.v039.i05>) are used to identify optimal
linear combinations of input variables.

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
