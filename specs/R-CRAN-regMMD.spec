%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regMMD
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Regression and Estimation Through Maximum Mean Discrepancy Minimization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-Rdpack >= 0.7

%description
The functions in this package compute robust estimators by minimizing a
kernel-based distance known as MMD (Maximum Mean Discrepancy) between the
sample and a statistical model. Recent works proved that these estimators
enjoy a universal consistency property, and are extremely robust to
outliers. Various optimization algorithms are implemented: stochastic
gradient is available for most models, but the package also allows
gradient descent in a few models for which an exact formula is available
for the gradient. In terms of distribution fit, a large number of
continuous and discrete distributions are available: Gaussian,
exponential, uniform, gamma, Poisson, geometric, etc. In terms of
regression, the models available are: linear, logistic, gamma, beta and
Poisson. Alquier, P. and Gerber, M. (2024) <doi:10.1093/biomet/asad031>
Cherief-Abdellatif, B.-E. and Alquier, P. (2022) <doi:10.3150/21-BEJ1338>.

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
