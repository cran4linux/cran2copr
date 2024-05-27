%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qreport
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Reporting with 'Quarto'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 5.1.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-Hmisc >= 5.1.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-htmltools 

%description
Provides statistical components, tables, and graphs that are useful in
'Quarto' and 'RMarkdown' reports and that produce 'Quarto' elements for
special formatting such as tabs and marginal notes and graphs. Some of the
functions produce entire report sections with tabs, e.g., the missing data
report created by missChk().  Functions for inserting variables and tables
inside 'graphviz' and 'mermaid' diagrams are included, and so are special
clinical trial graphics for adverse event reporting.

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
