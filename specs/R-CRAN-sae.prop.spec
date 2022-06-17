%global __brp_check_rpaths %{nil}
%global packname  sae.prop
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Estimation using Fay-Herriot Models with Additive Logistic Transformation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-fpc 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-fpc 

%description
Implements Additive Logistic Transformation (alr) for Small Area
Estimation under Fay Herriot Model. Small Area Estimation is used to
borrow strength from auxiliary variables to improve the effectiveness of a
domain sample size. This package uses Empirical Best Linear Unbiased
Prediction (EBLUP) estimator. The Additive Logistic Transformation (alr)
are based on transformation by Aitchison J (1986). The covariance matrix
for multivariate application is base on covariance matrix used by Esteban
M, Lombardía M, López-Vizcaíno E, Morales D, and Pérez A
<doi:10.1007/s11749-019-00688-w>. The non-sampled models are modified
area-level models based on models proposed by Anisa R, Kurnia A, and
Indahwati I <doi:10.9790/5728-10121519>, with univariate model using
model-3, and multivariate model using model-1. The MSE are estimated using
Parametric Bootstrap approach. For non-sampled cases, MSE are estimated
using modified approach proposed by Haris F and Ubaidillah A
<doi:10.4108/eai.2-8-2019.2290339>.

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
