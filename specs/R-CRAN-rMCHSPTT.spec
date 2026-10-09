%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rMCHSPTT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modified Chain Sampling Inspection Plan for Time-Truncated Life Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Designing and comparing modified chain sampling inspection plan (MChSP).
This package implements ChSP-1, MChSP-1, Multiple Dependent State Sampling
(MDS), and Modified Chain Sampling plans (MChSP). The plans use
user-supplied failure probabilities and determine the minimum sample size
subject to consumer's risk constraints. Functions are provided to compare
the required sample sizes of the four plans and visualize their
performance. The distribution-free formulation allows the methods to be
used with different lifetime distributions. Luca (2018)
<doi:10.1080/02664763.2017.1375084>; Tripathi et al. (2021)
<doi:10.32604/csse.2021.015624>; Tripathi et al. (2023)
<doi:10.1007/s41872-023-00215-9>; Rao et al. (2025)
<doi:10.1080/27684520.2025.2531810>; Tripathi and Saha (2023)
<doi:10.1007/s13198-023-02221-7>.

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
