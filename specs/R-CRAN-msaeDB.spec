%global packname  msaeDB
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Difference Benchmarking for Multivariate Small Area Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magic 
Requires:         R-stats 

%description
Implements Benchmarking Method for Multivariate Small Area Estimation
under Fay Herriot Model. Multivariate Small Area Estimation (MSAE) is a
development of Univariate Small Area Estimation that considering the
correlation among response variables and borrowing the strength from
related areas and auxiliary variables to increase the effectiveness of
sample size, the multivariate model in this package is based on
multivariate model 1 proposed by Roberto Benavent and Domingo Morales
(2016) <doi:10.1016/j.csda.2015.07.013>. Benchmarking in Small Area
Estimation is a modification of Small Area Estimation model to guarantee
that the aggregate weighted mean of the county predictors equals the
corresponding weighted mean of survey estimates. Difference Benchmarking
is the simplest benchmarking method but widely used by multiplying
empirical best linear unbiased prediction (EBLUP) estimator by the common
adjustment factors (J.N.K Rao and Isabel Molina, 2015).

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
