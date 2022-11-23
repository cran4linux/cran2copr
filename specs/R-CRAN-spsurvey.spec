%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spsurvey
%global packver   5.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Sampling Design and Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.1.1
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-crossdes 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-survey >= 4.1.1
Requires:         R-CRAN-sf 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-crossdes 
Requires:         R-CRAN-deldir 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sampling 
Requires:         R-stats 
Requires:         R-CRAN-units 

%description
A design-based approach to statistical inference, with a focus on spatial
data. Spatially balanced samples are selected using the Generalized Random
Tessellation Stratified (GRTS) algorithm. The GRTS algorithm can be
applied to finite resources (point geometries) and infinite resources
(linear / linestring and areal / polygon geometries) and flexibly
accommodates a diverse set of sampling design features, including
stratification, unequal inclusion probabilities, proportional (to size)
inclusion probabilities, legacy (historical) sites, a minimum distance
between sites, and two options for replacement sites (reverse hierarchical
order and nearest neighbor). Data are analyzed using a wide range of
analysis functions that perform categorical variable analysis, continuous
variable analysis, attributable risk analysis, risk difference analysis,
relative risk analysis, change analysis, and trend analysis. spsurvey can
also be used to summarize objects, visualize objects, select samples that
are not spatially balanced, select panel samples, measure the amount of
spatial balance in a sample, adjust design weights, and more.

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
