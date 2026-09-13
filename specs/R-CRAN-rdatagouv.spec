%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdatagouv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Download and Explore Datasets from Data.gouv.fr

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-nanoparquet 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vroom 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-nanoparquet 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vroom 

%description
Provides a client for the public API of data.gouv.fr, the French
government's open data platform. It helps you find a dataset that matches
your interests, judge whether it is usable, download it, and re-fetch the
exact same table later in a reproducible way. You can search the catalog
and filter by producer or theme (dg_find_datasets(),
dg_find_organization(), dg_find_topics()), pull a dataset's tabular
resources into tidy tibbles (dg_pull_dataset()), inspect the documented
variables of its data schema (dg_schema()), and compute summary metrics
such as size, number of columns and missing-value rate (dg_summary(),
dg_summarise()). Each returned table carries a stable identifier
(dg_table_id(), dg_refetch()) so it can be re-fetched later. Requests are
built on top of 'httr2'.

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
