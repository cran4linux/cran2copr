%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SNPannotator
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Functional Annotation of Genetic Variants and Linked Proxies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.5.2
BuildRequires:    R-methods >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-rmarkdown >= 2.26
BuildRequires:    R-CRAN-ggraph >= 2.2.1
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-httr >= 1.4.7
BuildRequires:    R-CRAN-futile.logger >= 1.4.3
BuildRequires:    R-CRAN-kableExtra >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.6
BuildRequires:    R-CRAN-progress >= 1.2.3
BuildRequires:    R-CRAN-data.table >= 1.15.4
BuildRequires:    R-CRAN-ini >= 0.3.1
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-openxlsx >= 4.2.5.2
Requires:         R-methods >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-rmarkdown >= 2.26
Requires:         R-CRAN-ggraph >= 2.2.1
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-httr >= 1.4.7
Requires:         R-CRAN-futile.logger >= 1.4.3
Requires:         R-CRAN-kableExtra >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.6
Requires:         R-CRAN-progress >= 1.2.3
Requires:         R-CRAN-data.table >= 1.15.4
Requires:         R-CRAN-ini >= 0.3.1
Requires:         R-CRAN-png 

%description
To automated functional annotation of genetic variants and linked proxies.
Linked SNPs in moderate to high linkage disequilibrium (e.g. r2>0.50) with
the corresponding index SNPs will be selected for further analysis.

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
