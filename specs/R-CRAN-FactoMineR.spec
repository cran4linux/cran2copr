%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FactoMineR
%global packver   2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Exploratory Data Analysis and Data Mining

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-flashClust 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-car 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-flashClust 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 

%description
Exploratory data analysis methods to summarize, visualize and describe
datasets. The main principal component methods are available, those with
the largest potential in terms of applications: principal component
analysis (PCA) when variables are quantitative, correspondence analysis
(CA) and multiple correspondence analysis (MCA) when variables are
categorical, Multiple Factor Analysis when variables are structured in
groups, etc. and hierarchical cluster analysis. F. Husson, S. Le and J.
Pages (2017).

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
