%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bootnet
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Methods for Various Network Estimation Routines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgm >= 1.2
BuildRequires:    R-CRAN-NetworkToolbox >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.3.0.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-IsingFit 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-IsingSampler 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-networktools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-mgm >= 1.2
Requires:         R-CRAN-NetworkToolbox >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.3.0.2
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-IsingFit 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-IsingSampler 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-networktools 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
Bootstrap methods to assess accuracy and stability of estimated network
structures and centrality indices <doi:10.3758/s13428-017-0862-1>. Allows
for flexible specification of any undirected network estimation procedure
in R, and offers default sets for various estimation routines.

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
