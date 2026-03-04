%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  factoextra
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract and Visualize the Results of Multivariate Data Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-FactoMineR >= 2.13
BuildRequires:    R-CRAN-cluster >= 2.1.8.2
BuildRequires:    R-CRAN-dendextend >= 1.19.1
BuildRequires:    R-CRAN-rlang >= 1.1.7
BuildRequires:    R-CRAN-ggrepel >= 0.9.5
BuildRequires:    R-CRAN-ggpubr >= 0.6.3
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-FactoMineR >= 2.13
Requires:         R-CRAN-cluster >= 2.1.8.2
Requires:         R-CRAN-dendextend >= 1.19.1
Requires:         R-CRAN-rlang >= 1.1.7
Requires:         R-CRAN-ggrepel >= 0.9.5
Requires:         R-CRAN-ggpubr >= 0.6.3
Requires:         R-grid 
Requires:         R-stats 

%description
Provides easy-to-use functions to extract and visualize the output of
multivariate data analyses, including 'PCA' (Principal Component
Analysis), 'CA' (Correspondence Analysis), 'MCA' (Multiple Correspondence
Analysis), 'FAMD' (Factor Analysis of Mixed Data), 'MFA' (Multiple Factor
Analysis), and 'HMFA' (Hierarchical Multiple Factor Analysis) from
different R packages. It also includes helpers for simplifying clustering
analysis workflows and provides 'ggplot2'-based data visualization.

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
