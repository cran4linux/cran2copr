%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSQCA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Threshold Sweep Extensions for Qualitative Comparative Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-QCA 
Requires:         R-CRAN-QCA 

%description
Provides threshold sweep methods for Qualitative Comparative Analysis
(QCA). Implements Condition Threshold Sweep-Single (CTS-S), Condition
Threshold Sweep-Multiple (CTS-M), Outcome Threshold Sweep (OTS), and Dual
Threshold Sweep (DTS) for systematic exploration of threshold calibration
effects on crisp-set QCA results. These methods extend traditional
robustness approaches by treating threshold variation as an exploratory
tool for discovering causal structures. Built on top of the 'QCA' package
by Dusa (2019) <doi:10.1007/978-3-319-75668-4>, with function arguments
following 'QCA' conventions. Based on set-theoretic methods by Ragin
(2008) <doi:10.7208/chicago/9780226702797.001.0001> and established
robustness protocols by Rubinson et al. (2019)
<doi:10.1177/00491241211036158>.

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
