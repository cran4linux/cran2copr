%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  henna
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Versatile Visualization Suite

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-abdiv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggalluvial 
BuildRequires:    R-CRAN-ggeasy 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-liver 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-abdiv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggalluvial 
Requires:         R-CRAN-ggeasy 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-CRAN-liver 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-viridis 

%description
A visualization suite primarily designed for single-cell RNA-sequencing
data analysis applications, but adaptable to other purposes as well. It
introduces novel plots to represent two-variable and frequency data and
optimizes some commonly used plotting options (e.g., correlation, network,
density and alluvial plots) for ease of usage and flexibility.

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
