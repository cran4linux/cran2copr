%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GreenManureR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Green Manure Decomposition, Nutrient Release and Crop Response

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Tools for analysing green manure and cover crop experiments, for example
with Mucuna, sunhemp and dhaincha. Fits single-pool, double-pool and
asymptotic litterbag decomposition models and ranks them by the corrected
Akaike information criterion, estimates the time to 50 percent mass loss
with Monte-Carlo confidence intervals, and quantifies nitrogen,
phosphorus, potassium and other nutrient release over time. Further
functions compute nutrient inputs, crop uptake, apparent nitrogen recovery
and fertilizer nitrogen replacement value, estimate residual effects of
green manures on succeeding kharif and rabi crops, link decomposition,
nutrient release and crop response in a joint analysis, and generate
standardized tables, diagnostic plots and a Word report.

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
