%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viscomp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize Multi-Component Interventions in Network Meta-Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.56
BuildRequires:    R-CRAN-Hmisc >= 4.7.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-qgraph >= 1.9.2
BuildRequires:    R-CRAN-plyr >= 1.8.7
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-netmeta >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-ggnewscale >= 0.4.8
BuildRequires:    R-CRAN-circlize >= 0.4.15
BuildRequires:    R-CRAN-ggExtra >= 0.10.0
Requires:         R-CRAN-MASS >= 7.3.56
Requires:         R-CRAN-Hmisc >= 4.7.0
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-qgraph >= 1.9.2
Requires:         R-CRAN-plyr >= 1.8.7
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-netmeta >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-ggnewscale >= 0.4.8
Requires:         R-CRAN-circlize >= 0.4.15
Requires:         R-CRAN-ggExtra >= 0.10.0

%description
A set of functions providing several visualization tools for exploring the
behavior of the components in a network meta-analysis of multi-component
(complex) interventions: - components descriptive analysis - heat plot of
the two-by-two component combinations - leaving one component combination
out scatter plot - violin plot for specific component combinations'
effects - density plot for components' effects - waterfall plot for the
interventions' effects that differ by a certain component combination -
network graph of components - rank heat plot of components for multiple
outcomes. The implemented tools are described by Seitidis et al. (2023)
<doi:10.1002/jrsm.1617>.

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
