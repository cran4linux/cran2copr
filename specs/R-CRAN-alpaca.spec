%global __brp_check_rpaths %{nil}
%global packname  alpaca
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fit GLM's with High-Dimensional k-Way Fixed Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a routine to partial out factors with many levels during the
optimization of the log-likelihood function of the corresponding
generalized linear model (glm). The package is based on the algorithm
described in Stammann (2018) <arXiv:1707.01815> and is restricted to glm's
that are based on maximum likelihood estimation and non-linear. It also
offers an efficient algorithm to recover estimates of the fixed effects in
a post-estimation routine and includes robust and multi-way clustered
standard errors. Further the package provides analytical bias corrections
for binary choice models (logit and probit) derived by Fernandez-Val and
Weidner (2016) <doi:10.1016/j.jeconom.2015.12.014> and Hinz, Stammann, and
Wanner (2020) <arXiv:2004.12655>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
