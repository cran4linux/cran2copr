%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  practicalSigni
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Practical Significance Ranking of Regressors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.7
BuildRequires:    R-CRAN-xtable >= 1.8
BuildRequires:    R-CRAN-generalCorr >= 1.2
BuildRequires:    R-CRAN-NNS >= 0.9
BuildRequires:    R-CRAN-np >= 0.60
Requires:         R-CRAN-randomForest >= 4.7
Requires:         R-CRAN-xtable >= 1.8
Requires:         R-CRAN-generalCorr >= 1.2
Requires:         R-CRAN-NNS >= 0.9
Requires:         R-CRAN-np >= 0.60

%description
Consider a possibly nonlinear nonparametric regression with p regressors.
We provide evaluations by 13 methods to rank regressors by their practical
significance or importance using various methods, including machine
learning tools. Comprehensive methods are as follows. m6=Generalized
partial correlation coefficient or GPCC by Vinod
(2021)<doi:10.1007/s10614-021-10190-x> and Vinod
(2022)<https://www.mdpi.com/1911-8074/15/1/32>. m7= a generalization of
psychologists' effect size incorporating nonlinearity and many variables.
m8= local linear partial (dy/dxi) using the 'np' package for kernel
regressions. m9= partial (dy/dxi) using the 'NNS' package. m10= importance
measure using the 'NNS' boost function. m11= Shapley Value measure of
importance (cooperative game theory). m12 and m13= two versions of the
random forest algorithm.

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
