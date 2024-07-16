%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SetTest
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Testing Procedures for Signal Detection and Goodness-of-Fit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
It provides cumulative distribution function (CDF), quantile, p-value,
statistical power calculator and random number generator for a collection
of group-testing procedures, including the Higher Criticism tests, the
one-sided Kolmogorov-Smirnov tests, the one-sided Berk-Jones tests, the
one-sided phi-divergence tests, etc. The input are a group of p-values.
The null hypothesis is that they are i.i.d. Uniform(0,1). In the context
of signal detection, the null hypothesis means no signals. In the context
of the goodness-of-fit testing, which contrasts a group of i.i.d. random
variables to a given continuous distribution, the input p-values can be
obtained by the CDF transformation. The null hypothesis means that these
random variables follow the given distribution. For reference, see [1]Hong
Zhang, Jiashun Jin and Zheyang Wu. "Distributions and power of optimal
signal-detection statistics in finite case", IEEE Transactions on Signal
Processing (2020) 68, 1021-1033; [2] Hong Zhang and Zheyang Wu. "The
general goodness-of-fit tests for correlated data", Computational
Statistics & Data Analysis (2022) 167, 107379.

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
