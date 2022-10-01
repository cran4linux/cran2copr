%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rgff
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          R Utilities for GFF Files

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-withr >= 2.4.3
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-stringi >= 1.7.6
BuildRequires:    R-CRAN-RJSONIO >= 1.3.1.6
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-data.tree >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.12
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-withr >= 2.4.3
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-stringi >= 1.7.6
Requires:         R-CRAN-RJSONIO >= 1.3.1.6
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-data.tree >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.12

%description
R utilities for gff files, either general feature format (GFF3) or gene
transfer format (GTF) formatted files. This package includes functions for
producing summary stats, check for consistency and sorting errors,
conversion from GTF to GFF3 format, file sorting, visualization and
plotting of feature hierarchy, and exporting user defined feature subsets
to SAF format. This tool was developed by the BioinfoGP core facility at
CNB-CSIC.

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
