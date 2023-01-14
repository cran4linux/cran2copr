%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dblcens
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Compute the NPMLE of Distribution Function from Doubly Censored Data, Plus the Empirical Likelihood Ratio for F(T)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5

%description
Doubly censored data, as described in Chang and Yang (1987) <doi:
10.1214/aos/1176350608>), are commonly seen in many fields. We use EM
algorithm to compute the non-parametric MLE (NPMLE) of the cummulative
probability function/survival function and the two censoring
distributions. One can also specify a constraint F(T)=C, it will return
the constrained NPMLE and the -2 log empirical likelihood ratio for this
constraint. This can be used to test the hypothesis about the constraint
and, by inverting the test, find confidence intervals for probability or
quantile via empirical likelihood ratio theorem. Influence functions of
hat F may also be calculated, but currently, the it may be slow.

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
