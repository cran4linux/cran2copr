%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  corridoR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Migration Corridors and Genetic Range Shifts from Landscape Genetic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-gdistance 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Models genetic connectivity along migration corridors and forecasts how it
shifts under climate change, following Maier et al. (2022)
<doi:10.1038/s41437-022-00561-x>. Least cost corridors are built from
accumulated cost surfaces and used as weights to summarize raw
environmental layers between sites; each group of environmental features
can choose its own corridor bandwidth; and pairwise predictions of
differentiation and directional migration are mapped back onto the
landscape as magnitude and net-direction surfaces. Includes readers for
common genotype formats (STRUCTURE, GENEPOP, VCF, GenAlEx, FSTAT and PLINK
files, and 'adegenet' objects), pairwise fixation indices, and the
directional differentiation of Sundqvist et al. (2016)
<doi:10.1002/ece3.2096>.

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
