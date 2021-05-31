%global packname  C443
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          See a Forest for the Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cluster 
Requires:         R-parallel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-qgraph 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-plyr 

%description
Get insight into a forest of classification trees, by calculating
similarities between the trees, and subsequently clustering them. Each
cluster is represented by it's most central cluster member. The package
implements the methodology described in Sies & Van Mechelen (2020)
<doi:10.1007/s00357-019-09350-4>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
