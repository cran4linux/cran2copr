%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rGrSPTT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sampling Inspection Plan for Time Truncated Life Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Designing group acceptance sampling inspection plans under time-truncated
life tests. The package calculates the required minimum number of groups
subject to a consumer's risk constraint on the probability of acceptance.
Users can supply failure probabilities obtained from any lifetime
distribution, allowing the methodology to be applied without restricting
the analysis to a particular probability model. The package also provides
a function for plotting the required minimum number of groups against the
termination ratio. Saha et al. (2025) <doi:10.1007/s41872-025-00305-w>;
Tripathi et al. (2020) <doi:10.1080/02664763.2020.1759031>; Tripathi and
Aslam (2024) <doi:10.1285/i20705948v17n3p636>.

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
