%global __brp_check_rpaths %{nil}
%global packname  islasso
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Induced Smoothed Lasso

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-glmnet >= 4.0
BuildRequires:    R-CRAN-Matrix >= 1.0.6
Requires:         R-CRAN-glmnet >= 4.0
Requires:         R-CRAN-Matrix >= 1.0.6

%description
An implementation of the induced smoothing (IS) idea to lasso
regularization models to allow estimation and inference on the model
coefficients (currently hypothesis testing only). Linear, logistic,
Poisson and gamma regressions with several link functions are implemented.
The algorithm is described in the original paper: Cilluffo, G., Sottile,
G., La Grutta, S. and Muggeo, V. (2019) The Induced Smoothed lasso: A
practical framework for hypothesis testing in high dimensional regression.
<doi:10.1177/0962280219842890>, and discussed in a tutorial: Sottile, G.,
Cilluffo, G., and Muggeo, V. (2019) The R package islasso: estimation and
hypothesis testing in lasso regression. <doi:10.13140/RG.2.2.16360.11521>.

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
