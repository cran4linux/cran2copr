%global __brp_check_rpaths %{nil}
%global packname  LBSPR
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Length-Based Spawning Potential Ratio

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tidyr 

%description
Simulate expected equilibrium length composition, yield-per-recruit, and
the spawning potential ratio (SPR) using the length-based SPR (LBSPR)
model. Fit the LBSPR model to length data to estimate selectivity,
relative apical fishing mortality, and the spawning potential ratio for
data-limited fisheries. See Hordyk et al (2016)
<doi:10.1139/cjfas-2015-0422> for more information about the LBSPR
assessment method.

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
