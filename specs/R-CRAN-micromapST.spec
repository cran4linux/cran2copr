%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  micromapST
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linked Micromap Plots for U. S. and Other Geographic Areas

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-rmapshaper 
BuildRequires:    R-CRAN-cleangeo 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-rmapshaper 
Requires:         R-CRAN-cleangeo 
Requires:         R-CRAN-pbapply 

%description
Provides the users with the ability to quickly create linked micromap
plots for a collection of geographic areas. Linked micromap plots are
visualizations of geo-referenced data that link statistical graphics to an
organized series of small maps or graphic images. The Help description
contains examples of how to use the 'micromapST' function. Contained in
this package are border group datasets to support creating linked micromap
plots for the 50 U.S. states and District of Columbia (51 areas), the U.
S. 20 Seer Registries, the 105 counties in the state of Kansas, the 62
counties of New York, the 24 counties of Maryland, the 29 counties of
Utah, the 32 administrative areas in China, the 218 administrative areas
in the UK and Ireland (for testing only), the 25 districts in the city of
Seoul South Korea, and the 52 counties on the Africa continent. A border
group dataset contains the boundaries related to the data level areas, a
second layer boundaries, a top or third layer boundary, a parameter list
of run options, and a cross indexing table between area names,
abbreviations, numeric identification and alias matching strings for the
specific geographic area.  By specifying a border group, the package
create linked micromap plots for any geographic region.  The user can
create and provide their own border group dataset for any area beyond the
areas contained within the package. References: Carr and Pickle, Chapman
and Hall/CRC, Visualizing Data Patterns with Micromaps, CRC Press, 2010.
Pickle, Pearson, and Carr (2015), micromapST: Exploring and Communicating
Geospatial Patterns in US State Data., Journal of Statistical Software,
63(3), 1-25., <https://www.jstatsoft.org/v63/i03/>. Copyrighted 2013,
2014, 2015, 2016, and 2022 by Carr, Pearson and Pickle.

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
