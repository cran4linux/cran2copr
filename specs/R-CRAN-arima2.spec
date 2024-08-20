%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arima2
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood Based Inference for ARIMA Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Estimating and analyzing auto regressive integrated moving average (ARIMA)
models. The primary function in this package is arima(), which fits an
ARIMA model to univariate time series data using a random restart
algorithm. This approach frequently leads to models that have model
likelihood greater than or equal to that of the likelihood obtained by
fitting the same model using the arima() function from the 'stats'
package. This package enables proper optimization of model likelihoods,
which is a necessary condition for performing likelihood ratio tests. This
package relies heavily on the source code of the arima() function of the
'stats' package. For more information, please see Jesse Wheeler and Edward
L. Ionides (2023) <doi:10.48550/arXiv.2310.01198>.

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
