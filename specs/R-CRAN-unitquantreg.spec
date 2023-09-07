%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unitquantreg
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Quantile Regression Models for Bounded Data

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-optimx 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 

%description
A collection of parametric quantile regression models for bounded data. At
present, the package provides 13 parametric quantile regression models. It
can specify regression structure for any quantile and shape parameters. It
also provides several S3 methods to extract information from fitted model,
such as residual analysis, prediction, plotting, and model comparison. For
more computation efficient the [dpqr]'s, likelihood, score and hessian
functions are written in C++. For further details see Mazucheli et. al
(2022) <doi:10.1016/j.cmpb.2022.106816>.

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
