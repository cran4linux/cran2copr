%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hytest
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Testing Based on Neyman-Pearson Lemma and Likelihood Ratio Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 

%description
Error type I and Optimal critical values to test statistical hypothesis
based on Neyman-Pearson Lemma and Likelihood ratio test based on random
samples from several distributions. The families of distributions are
Bernoulli, Exponential, Geometric, Inverse Normal, Normal, Gamma, Gumbel,
Lognormal, Poisson, and Weibull. This package is an ideal resource to help
with the teaching of Statistics. The main references for this package are
Casella G. and Berger R. (2003,ISBN:0-534-24312-6 , "Statistical
Inference. Second Edition", Duxbury Press) and Hogg, R., McKean, J., and
Craig, A. (2019,ISBN:013468699, "Introduction to Mathematical Statistic.
Eighth edition", Pearson).

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
