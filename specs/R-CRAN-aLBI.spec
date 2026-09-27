%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aLBI
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Length-Based Indicators for Fish Stock Assessment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-openxlsx 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for estimating length-based indicators (LBIs) from
length-frequency data to assess fish stock status and evaluate growth and
recruitment overfishing in data-limited fisheries. Implements the
sustainability indicators of Froese (2004)
<doi:10.1111/j.1467-2979.2004.00144.x>, empirical biological reference
points from Froese and Binohlan (2000)
<doi:10.1111/j.1095-8649.2000.tb00870.x>, and the decision framework of
Cope and Punt (2009) <doi:10.1577/C08-025.1>. Incorporates a three-tier
Monte Carlo and bootstrap uncertainty propagation framework for
sustainability indicators, optimum bin size calculations following Wang et
al. (2020) <doi:10.1016/j.fishres.2019.105474>, multi-month
length-frequency harmonization, and length-weight relationship fitting.
Methodology is detailed in Ali et al. (2025)
<doi:10.1016/j.fishres.2025.107467>.

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
