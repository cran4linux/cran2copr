%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  divraster
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Diversity Metrics Calculations for Rasterized Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BAT 
BuildRequires:    R-CRAN-SESraster 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-BAT 
Requires:         R-CRAN-SESraster 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Alpha and beta diversity for taxonomic (TD), functional (FD), and
phylogenetic (PD) dimensions based on rasters. Spatial and temporal beta
diversity can be partitioned into replacement and richness difference
components. It also calculates standardized effect size for FD and PD
alpha diversity and the average individual traits across multilayer
rasters. The layers of the raster represent species, while the cells
represent communities. Methods details can be found at Cardoso et al. 2022
<https://CRAN.R-project.org/package=BAT> and Heming et al. 2023
<https://CRAN.R-project.org/package=SESraster>.

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
