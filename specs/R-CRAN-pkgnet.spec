%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgnet
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Get Network Representation of an R Package

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 2.1
BuildRequires:    R-CRAN-rmarkdown >= 1.9
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-igraph >= 2.1
Requires:         R-CRAN-rmarkdown >= 1.9
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-CRAN-visNetwork 

%description
Tools from the domain of graph theory can be used to quantify the
complexity and vulnerability to failure of a software package. That is the
guiding philosophy of this package. 'pkgnet' provides tools to analyze the
dependencies between functions in an R package and between its imported
packages.  See the pkgnet website for vignettes and other supplementary
information.

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
