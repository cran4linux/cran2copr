%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GABB
%global packver   0.3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.10
Release:          1%{?dist}%{?buildtag}
Summary:          Facilitation of Data Preparation and Plotting Procedures for RDA and PCA Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-egg >= 0.4.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-Hotelling 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-utils 
Requires:         R-CRAN-egg >= 0.4.5
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-Hotelling 
Requires:         R-CRAN-pheatmap 
Requires:         R-stats 
Requires:         R-CRAN-vegan 
Requires:         R-utils 

%description
Help to the occasional R user for synthesis and enhanced graphical
visualization of redundancy analysis (RDA) and principal component
analysis (PCA) methods and objects. Inputs are : data frame, RDA (package
'vegan') and PCA (package 'FactoMineR') objects. Outputs are : synthesized
results of RDA, displayed in console and saved in tables ; displayed and
saved objects of PCA graphic visualization of individuals and variables
projections with multiple graphic parameters.

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
