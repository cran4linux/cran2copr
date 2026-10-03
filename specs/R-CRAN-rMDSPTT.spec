%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rMDSPTT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Dependent State Sampling Inspection Plan for Time Truncated Life Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides functions for designing multiple dependent state sampling
inspection plans for time-truncated life tests. The package determines the
minimum sample size required to satisfy a specified consumer's risk
constraint and evaluates the probability of acceptance under different
quality and termination ratios. Users can directly provide failure
probabilities, allowing the sampling plan to be applied to different
lifetime distributions without requiring distribution-specific functions.
Provide operating characteristic analysis, sample size analysis, and
graphical comparison with single sampling inspection plans. Aslam et al.
(2016) <doi:10.1080/08982112.2015.1068331>; Rao et al. (2020)
<doi:10.1080/25742558.2020.1857915>; Balamurali et al. (2017)
<doi:10.1080/07474946.2016.1275459>; Saha et al. (2021)
<doi:10.1080/21681015.2021.1893843>; Tripathi et al. (2020)
<doi:10.1007/s40745-020-00267-z>; Tripathi et al. (2023)
<doi:10.1007/s41872-023-00221-x>.

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
