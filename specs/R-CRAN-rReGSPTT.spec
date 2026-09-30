%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rReGSPTT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Repetitive Group Acceptance Sampling Inspection Plans for Time Truncated Life Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Designing repetitive group acceptance sampling inspection plans for
time-truncated life tests. The package uses a distribution-free
formulation in which the user supplies the failure probability. The
functions compute operating characteristic probabilities and average
sample numbers subject to a consumer's risk constraint. The package also
provides graphical and comparative tools for comparing repetitive group,
group and single sampling inspection plans. Sherman (1965)
<doi:10.2307/1266124>; Aslam and Jun (2013)
<doi:10.1007/s00170-013-4747-x>. Saha et al. (2025)
<doi:10.1007/s41872-025-00305-w>; Tripathi et al. (2020)
<doi:10.1080/02664763.2020.1759031>; Tripathi and Aslam (2024)
<doi:10.1285/i20705948v17n3p636>; Tripathi et al. (2022)
<doi:10.1007/s40745-020-00267-z>; Saha et al. (2021)
<doi:10.1080/21681015.2021.1893843>; Tripathi et al. (2023)
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
