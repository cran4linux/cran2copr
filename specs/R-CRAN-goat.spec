%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  goat
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Gene Set Analysis Using the Gene Set Ordinal Association Test

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-treemap >= 2.4
BuildRequires:    R-CRAN-ggraph >= 2.0.0
BuildRequires:    R-CRAN-readxl >= 1.4.1
BuildRequires:    R-CRAN-writexl >= 1.4.1
BuildRequires:    R-CRAN-Matrix >= 1.4.0
BuildRequires:    R-CRAN-igraph >= 1.2.5
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-pheatmap >= 1.0.8
BuildRequires:    R-CRAN-dplyr >= 1.0.3
BuildRequires:    R-CRAN-vctrs >= 0.3.8
BuildRequires:    R-CRAN-MonoPoly >= 0.3.10
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-treemap >= 2.4
Requires:         R-CRAN-ggraph >= 2.0.0
Requires:         R-CRAN-readxl >= 1.4.1
Requires:         R-CRAN-writexl >= 1.4.1
Requires:         R-CRAN-Matrix >= 1.4.0
Requires:         R-CRAN-igraph >= 1.2.5
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-pheatmap >= 1.0.8
Requires:         R-CRAN-dplyr >= 1.0.3
Requires:         R-CRAN-vctrs >= 0.3.8
Requires:         R-CRAN-MonoPoly >= 0.3.10

%description
Perform gene set enrichment analyses using the Gene set Ordinal
Association Test (GOAT) algorithm and visualize your results. Koopmans, F.
(2024) <doi:10.1038/s42003-024-06454-5>.

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
