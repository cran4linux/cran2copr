%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mclink
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Metabolic Pathway Completeness and Abundance Calculation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-data.table >= 1.17.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-data.table >= 1.17.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-utils 

%description
Provides tools for analyzing metabolic pathway completeness, abundance,
and transcripts using KEGG Orthology (KO) data from (meta)genomic and
(meta)transcriptomic studies. Supports both completeness
(presence/absence) and abundance-weighted analyses. Includes built-in KEGG
reference datasets. For more details see Li et al. (2023)
<doi:10.1038/s41467-023-42193-7>.

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
