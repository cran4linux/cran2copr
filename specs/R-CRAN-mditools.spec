%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mditools
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Microdata Infrastructure Tools for Firm-Level Microdata Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-mclust 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Supports the full analysis pipeline for researchers working with
firm-level microdata. Provides data tools for panel preparation (import,
outlier detection, classification harmonization), analytical methods
(production function estimation, capital stock measurement, markups,
intensity measures, distributions, regression, clustering), and disclosure
tools for tagging outputs with dominance and observation counts before
aggregation and publication. Production function estimation implements
methods by Ackerberg, Caves and Frazer (2015) <doi:10.3982/ECTA13408>,
Levinsohn and Petrin (2003) <doi:10.1111/1467-937X.00246>, Wooldridge
(2009) <doi:10.1016/j.econlet.2009.04.026>, Petrin, Poi and Levinsohn
(2004) <doi:10.1177/1536867X0400400202>, and Arellano and Bond (1991)
<doi:10.2307/2297968> with the "too many instruments" correction by
Roodman (2009) <doi:10.1111/j.1468-0084.2008.00542.x>. Markup estimation
follows De Loecker and Warzynski (2012) <doi:10.1257/aer.102.6.2437>.
Cost-share production function estimation follows Basu and Fernald (1997)
<doi:10.1086/262073>. Capital stock estimation via the Perpetual Inventory
Method follows OECD (2009) <doi:10.1787/9789264068476-en>.

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
