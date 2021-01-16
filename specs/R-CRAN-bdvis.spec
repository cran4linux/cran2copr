%global packname  bdvis
%global packver   0.2.28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.28
Release:          1%{?dist}%{?buildtag}
Summary:          Biodiversity Data Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-treemap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-leafletR 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-treemap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-leafletR 
Requires:         R-CRAN-rgdal 

%description
Provides a set of functions to create basic visualizations to quickly
preview different aspects of biodiversity information such as inventory
completeness, extent of coverage (taxonomic, temporal and geographic),
gaps and biases.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
