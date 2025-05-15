%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hce
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis of Hierarchical Composite Endpoints

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
Requires:         R-base 
Requires:         R-stats 

%description
Simulate and analyze hierarchical composite endpoints. Win odds, also
called Wilcoxon-Mann-Whitney or success odds, is the main analysis method.
Other win statistics (win probability, win ratio, net benefit) are also
implemented in the univariate case, provided there is no censoring. The
win probability analysis is based on the Brunner-Munzel test and uses the
DeLong-DeLong-Clarke-Pearson variance estimator, as described by Brunner
and Konietschke (2025) in “An unbiased rank-based estimator of the
Mann–Whitney variance including the case of ties” (Statistical Papers 66
(1): 20, <doi:10.1007/s00362-024-01635-0>). Stratification and covariate
adjustment are performed based on the methodology presented by Koch GG et
al. in “Issues for covariance analysis of dichotomous and ordered
categorical data from randomized clinical trials and non-parametric
strategies for addressing them” (Statistics in Medicine 17 (15-16):
1863–92). For a review, see Gasparyan SB et al (2021) “Adjusted win ratio
with stratification: Calculation methods and interpretation” (Statistical
Methods in Medical Research 30 (2): 580–611,
<doi:10.1177/0962280220942558>).

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
