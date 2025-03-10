%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  networktools
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Identifying Important Nodes in Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cocor 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-eigenmodel 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-wordcloud 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-cocor 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-eigenmodel 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-wordcloud 

%description
Includes assorted tools for network analysis. Bridge centrality;
goldbricker; MDS, PCA, & eigenmodel network plotting.

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
