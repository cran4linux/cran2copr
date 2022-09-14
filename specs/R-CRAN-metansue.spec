%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metansue
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Studies with Non-Statistically Significant Unreported Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Novel method to unbiasedly include studies with Non-statistically
Significant Unreported Effects (NSUEs) in a meta-analysis. First, the
method calculates the interval where the unreported effects (e.g.,
t-values) should be according to the threshold of statistical significance
used in each study. Afterwards, the method uses maximum likelihood
techniques to impute the expected effect size of each study with NSUEs,
accounting for between-study heterogeneity and potential covariates.
Multiple imputations of the NSUEs are then randomly created based on the
expected value, variance, and statistical significance bounds. Finally, it
conducts a restricted-maximum likelihood random-effects meta-analysis
separately for each set of imputations and it conducts estimations from
these meta-analyses. Please read the reference in 'metansue' for details
of the procedure.

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
