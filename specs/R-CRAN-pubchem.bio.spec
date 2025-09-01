%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pubchem.bio
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Biologically Informed Metabolomic Databases from 'PubChem'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rcdk 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-CHNOSZ 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rcdk 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-CHNOSZ 

%description
All 'PubChem' compounds are downloaded to a local computer, but for each
compound, only partial records are used.  The data are organized into
small files referenced by 'PubChem' CID.  This package also contains
functions to parse the biologically relevant compounds from all 'PubChem'
compounds, using biological database sources, pathway presence, and
taxonomic relationships. Taxonomy is used to generate a lowest common
ancestor taxonomy ID (NCBI) for each biological metabolite, which then
enables creation of taxonomically specific metabolome databases for any
taxon.

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
