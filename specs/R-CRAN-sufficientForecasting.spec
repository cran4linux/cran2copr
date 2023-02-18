%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sufficientForecasting
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sufficient Forecasting using Factor Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-stats 
Requires:         R-CRAN-gam 
Requires:         R-stats 

%description
The sufficient forecasting (SF) method is implemented by this package for
a single time series forecasting using many predictors and a possibly
nonlinear forecasting function. Assuming that the predictors are driven by
some latent factors, the SF first conducts factor analysis and then
performs sufficient dimension reduction on the estimated factors to derive
predictive indices for forecasting. The package implements several
dimension reduction approaches, including principal components (PC),
sliced inverse regression (SIR), and directional regression (DR). Methods
for dimension reduction are as described in: Fan, J., Xue, L. and Yao, J.
(2017) <doi:10.1016/j.jeconom.2017.08.009>, Luo, W., Xue, L., Yao, J. and
Yu, X. (2022) <doi:10.1093/biomet/asab037> and Yu, X., Yao, J. and Xue, L.
(2022) <doi:10.1080/07350015.2020.1813589>.

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
