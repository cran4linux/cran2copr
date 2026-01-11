%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastei
%global packver   0.0.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.12
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for ''A Fast Alternative for the R x C Ecological Inference Case''

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-jsonlite 

%description
Estimates the probability matrix for the R×C Ecological Inference problem
using the Expectation-Maximization Algorithm with four approximation
methods for the E-Step, and an exact method as well. It also provides a
bootstrap function to estimate the standard deviation of the estimated
probabilities. In addition, it has functions that aggregate rows optimally
to have more reliable estimates in cases of having few data points. For
comparing the probability estimates of two groups, a Wald test routine is
implemented. The library has data from the first round of the Chilean
Presidential Election 2021 and can also generate synthetic election data.
Methods described in Thraves, Charles; Ubilla, Pablo; Hermosilla, Daniel
(2024) ''A Fast Ecological Inference Algorithm for the R×C case''
<doi:10.2139/ssrn.4832834>.

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
