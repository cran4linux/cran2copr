%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timeEL
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Time to Event Analysis via Empirical Likelihood Inference

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Computation of t-year survival probabilities and t-year risks with right
censored survival data. The Kaplan-Meier estimator is used to provide
estimates for data without competing risks and the Aalen-Johansen
estimator is used when there are competing risks. Confidence intervals and
p-values are obtained using either usual Wald-type inference or empirical
likelihood inference, as described in Thomas and Grunkemeier (1975)
<doi:10.1080/01621459.1975.10480315> and Blanche (2020)
<doi:10.1007/s10985-018-09458-6>. Functions for both one-sample and
two-sample inference are provided. Unlike Wald-type inference, empirical
likelihood inference always leads to consistent conclusions, in terms of
statistical significance, when comparing two risks (or survival
probabilities) via either a ratio or a difference.

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
