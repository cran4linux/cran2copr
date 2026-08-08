%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbif.range
%global packver   1.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Species Range Mapping from GBIF Using Ecoregion Constraints

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-CoordinateCleaner 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-CoordinateCleaner 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-class 
Requires:         R-CRAN-NMOF 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Provides a workflow to retrieve, filter, and analyze 'GBIF' occurrence
records and to generate ecologically informed species range maps using
downloaded or custom ecoregions. The package includes tools for querying
the 'GBIF' backbone taxonomy with get_status(), counting or downloading
occurrences with get_gbif_count() and get_gbif(), creating custom
ecoregion layers with make_ecoreg(), building range maps with get_range(),
and evaluating them against independent validation data with
evaluate_range() and cv_range(). A disk-based batch workflow
(split_gbif_by_species(), species_csvs_to_ranges(), read_range_rds())
supports large multi-species 'GBIF' exports without loading the full table
into memory. Bundled ecoregion layers cover terrestrial (Olson et al. 2001
<doi:10.1641/0006-3568(2001)051[0933:TEOTWA]2.0.CO;2>), marine (Spalding
et al. 2007 <doi:10.1641/B570707>), and freshwater (Abell et al. 2008
<doi:10.1641/B580507>) realms. The 'GBIF' API is accessed via the 'rgbif'
package, and coordinate cleaning uses 'CoordinateCleaner' (Zizka et al.
2019 <doi:10.1111/2041-210X.13152>). The 'GBIF' API is described at
<https://www.gbif.org/developer/summary>.

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
