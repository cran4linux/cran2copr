%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAIRmaterials
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Make Materials Data FAIR

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-svDialogs 
BuildRequires:    R-CRAN-tidyjson 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonld 
BuildRequires:    R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-svDialogs 
Requires:         R-CRAN-tidyjson 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-jsonld 
Requires:         R-utils 

%description
We provide here tools used by the Solar Durability and Lifetime Extension
Center (SDLE) for FAIRifying data from materials science projects.
Functions have been created for numerous tools common in the field in
order to make the metadata more Findable, Accessible, Interoperable, and
Reproducible.

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
