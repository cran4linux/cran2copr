%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggpicrust2
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Make 'PICRUSt2' Output Analysis and Visualization Easier

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-aplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggprism 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-utils 
Requires:         R-CRAN-aplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggprism 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-ggraph 
Requires:         R-utils 

%description
Provides a convenient way to analyze and visualize 'PICRUSt2' output with
pre-defined plots and functions. Allows for generating statistical plots
about microbiome functional predictions and offers customization options.
Features a one-click option for creating publication-level plots, saving
time and effort in producing professional-grade figures. Streamlines the
'PICRUSt2' analysis and visualization process. For more details, see Yang
et al. (2023) <doi:10.1093/bioinformatics/btad470>.

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
