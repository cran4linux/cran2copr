%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saebenchmarking
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Benchmarking Small Area Estimates and Their Mean Squared Errors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-sae 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-sae 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Adjusts model-based small area estimates so that their weighted aggregate
agrees with the weighted aggregate of the direct estimates, using the
difference, ratio, and optimum benchmarking methods described in Rao and
Molina (2015, ISBN:978-1-118-73578-7) and Wang, Fuller and Qu (2008). The
mean squared error (MSE) of the benchmarked empirical best linear unbiased
predictor (EBLUP) under the Fay-Herriot model is estimated with the
second-order approximation or the parametric bootstrap of Steorts and
Ghosh (2013) <doi:10.5705/ss.2012.053>. The posterior MSE of the
benchmarked hierarchical Bayes (HB) estimator follows Datta, Ghosh,
Steorts and Maples (2011) <doi:10.1007/s11749-010-0218-y>.

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
