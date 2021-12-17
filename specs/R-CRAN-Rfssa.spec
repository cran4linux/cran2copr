%global __brp_check_rpaths %{nil}
%global packname  Rfssa
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Singular Spectrum Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-Rssa 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-Rssa 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-markdown 

%description
Methods and tools for implementing univariate and multivariate functional
singular spectrum analysis for functional time series whose variables
might be observed over different dimensional domains. The univariate fssa
algorithm is described in Haghbin H., Najibi, S.M., Mahmoudvand R., Trinka
J., Maadooliat M. (2021) and the multivariate fssa over different
dimensional domains technique may be found in Trinka J., Haghbin H., and
Maadooliat M. (Accepted). In addition, one may perform forecasting of
univariate and multivariate fts whose variables are observed over
one-dimensional domains as described in the dissertation of Trinka J.
(2021) and the manuscript of Trinka J., Haghbin H., Maadooliat M. (2020)
where the manuscript is to be submitted to a journal for publication.

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
