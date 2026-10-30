%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultinomFourier
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          p-Values of Multinomial Goodness-of-Fit Tests by Fourier Series Inversion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-parallel 
Requires:         R-parallel 

%description
Computes p-values of multinomial goodness-of-fit tests based on an
additive statistic: the log-likelihood ratio, Pearson's chi-squared, the
Cressie-Read power divergence, and the exact multinomial test. The main
function, pval_fourier(), writes the p-value as a Fourier series in the
moment-generating function of the statistic and sums it until an adaptive
stopping rule is met, which makes small p-values of large instances
computationally feasible. The function pval_exact() computes the exact
p-value by branch pruning with bounds from a dynamic program, and
pval_flexible() chooses between the two according to the size of the
instance.

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
