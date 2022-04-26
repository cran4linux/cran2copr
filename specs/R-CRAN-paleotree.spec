%global __brp_check_rpaths %{nil}
%global packname  paleotree
%global packver   3.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Paleontological and Phylogenetic Analyses of Evolution

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 4.1
BuildRequires:    R-CRAN-phangorn >= 2.6.3
BuildRequires:    R-CRAN-phytools >= 0.6.00
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape >= 4.1
Requires:         R-CRAN-phangorn >= 2.6.3
Requires:         R-CRAN-phytools >= 0.6.00
Requires:         R-stats 
Requires:         R-CRAN-jsonlite 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-RCurl 
Requires:         R-utils 

%description
Provides tools for transforming, a posteriori time-scaling, and modifying
phylogenies containing extinct (i.e. fossil) lineages. In particular, most
users are interested in the functions timePaleoPhy, bin_timePaleoPhy,
cal3TimePaleoPhy and bin_cal3TimePaleoPhy, which date cladograms of fossil
taxa using stratigraphic data. This package also contains a large number
of likelihood functions for estimating sampling and diversification rates
from different types of data available from the fossil record (e.g. range
data, occurrence data, etc). paleotree users can also simulate
diversification and sampling in the fossil record using the function
simFossilRecord, which is a detailed simulator for branching
birth-death-sampling processes composed of discrete taxonomic units
arranged in ancestor-descendant relationships. Users can use
simFossilRecord to simulate diversification in incompletely sampled fossil
records, under various models of morphological differentiation (i.e. the
various patterns by which morphotaxa originate from one another), and with
time-dependent, longevity-dependent and/or diversity-dependent rates of
diversification, extinction and sampling. Additional functions allow users
to translate simulated ancestor-descendant data from simFossilRecord into
standard time-scaled phylogenies or unscaled cladograms that reflect the
relationships among taxon units.

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
