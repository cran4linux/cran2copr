%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wmwAUC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Test of No Group Discrimination Using the WMW Statistic

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch

%description
Implements a wmwAUC test of H0: AUC = 1/2 for continuous, discrete, or
mixed random variables, based on the Wilcoxon-Mann-Whitney (WMW)
statistic. The classic WMW test is calibrated under H0: {(F, G): F = G}
which does not match the set {(F, G): AUC = 1/2}, implied by the test
statistic, and consequently leads to erroneous inferences. wmwAUC is
calibrated under the correct null and implements two finite-sample
corrected p-value methods: an Exact Unbiased (EU) method and a
Bias-Corrected (BC) method, both valid for any tie pattern. Methods are
described in M. Grendar (2025) "Wilcoxon-Mann-Whitney Test of No Group
Discrimination" <doi:10.48550/arXiv.2511.20308>.

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
