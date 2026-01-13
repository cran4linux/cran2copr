%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LorMe
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight One-Line Resolving Microbial Ecology Program

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggalluvial 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-HH 
BuildRequires:    R-CRAN-coin 
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggalluvial 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-HH 
Requires:         R-CRAN-coin 

%description
Provides a robust collection of functions tailored for microbial ecology
analysis, encompassing both data analysis and visualization. It introduces
an encapsulation feature that streamlines the process into a summary
object. With the initial configuration of this summary object, users can
execute a wide range of analyses with a single line of code, requiring
only two essential parameters for setup. The package delivers
comprehensive outputs including analysis objects, statistical outcomes,
and visualization-ready data, enhancing the efficiency of research
workflows. Designed with user-friendliness in mind, it caters to both
novices and seasoned researchers, offering an intuitive interface coupled
with adaptable customization options to meet diverse analytical needs.

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
