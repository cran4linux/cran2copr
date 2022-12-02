%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ndi
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Neighborhood Deprivation Indices

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidycensus 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidycensus 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Computes various metrics of socio-economic deprivation and disparity in
the United States. Some metrics are considered "spatial" because they
consider the values of neighboring (i.e., adjacent) census geographies in
their computation, while other metrics are "aspatial" because they only
consider the value within each census geography. Two types of aspatial
neighborhood deprivation indices (NDI) are available: including: (1) based
on Messer et al. (2006) <doi:10.1007/s11524-006-9094-x> and (2) based on
Andrews et al. (2020) <doi:10.1080/17445647.2020.1750066> and Slotman et
al. (2022) <doi:10.1016/j.dib.2022.108002> who use variables chosen by
Roux and Mair (2010) <doi:10.1111/j.1749-6632.2009.05333.x>. Both are a
decomposition of multiple demographic characteristics from the U.S. Census
Bureau American Community Survey 5-year estimates (ACS-5; 2006-2010
onward). Using data from the ACS-5 (2005-2009 onward), the package can
also (1) compute the spatial Racial Isolation Index (RI) based on
Anthopolos et al. (2011) <doi:10.1016/j.sste.2011.06.002>, (2) compute the
spatial Educational Isolation Index (EI) based on Bravo et al. (2021)
<doi:10.3390/ijerph18179384>, (3) compute the aspatial Index of
Concentration at the Extremes (ICE) based on Feldman et al. (2015)
<doi:10.1136/jech-2015-205728> and Krieger et al. (2016)
<doi:10.2105/AJPH.2015.302955>, (4) compute the aspatial Dissimilarity
Index based on Duncan & Duncan (1955) <doi:10.2307/2088328>, and (5)
retrieve the aspatial Gini Index based on Gini (1921)
<doi:10.2307/2223319>.

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
