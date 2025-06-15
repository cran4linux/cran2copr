%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EFAfactors
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Determining the Number of Factors in Exploratory Factor Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ddpcr 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-SimCorMultRes 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ddpcr 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-SimCorMultRes 
Requires:         R-CRAN-xgboost 

%description
Provides a collection of standard factor retention methods in Exploratory
Factor Analysis (EFA), making it easier to determine the number of
factors. Traditional methods such as the scree plot by Cattell (1966)
<doi:10.1207/s15327906mbr0102_10>, Kaiser-Guttman Criterion (KGC) by
Guttman (1954) <doi:10.1007/BF02289162> and Kaiser (1960)
<doi:10.1177/001316446002000116>, and flexible Parallel Analysis (PA) by
Horn (1965) <doi:10.1007/BF02289447> based on eigenvalues form PCA or EFA
are readily available. This package also implements several newer methods,
such as the Empirical Kaiser Criterion (EKC) by Braeken and van Assen
(2017) <doi:10.1037/met0000074>, Comparison Data (CD) by Ruscio and Roche
(2012) <doi:10.1037/a0025697>, and Hull method by Lorenzo-Seva et al.
(2011) <doi:10.1080/00273171.2011.564527>, as well as some AI-based
methods like Comparison Data Forest (CDF) by Goretzko and Ruscio (2024)
<doi:10.3758/s13428-023-02122-4> and Factor Forest (FF) by Goretzko and
Buhner (2020) <doi:10.1037/met0000262>. Additionally, it includes a deep
neural network (DNN) trained on large-scale datasets that can efficiently
and reliably determine the number of factors.

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
