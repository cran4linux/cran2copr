%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QurvE
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust and User-Friendly Analysis of Growth and Fluorescence Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 

%description
High-throughput analysis of growth curves and fluorescence data using
three methods: linear regression, growth model fitting, and smooth spline
fit. Analysis of dose-response relationships via smoothing splines or
dose-response models. Complete data analysis workflows can be executed in
a single step via user-friendly wrapper functions. The results of these
workflows are summarized in detailed reports as well as intuitively
navigable 'R' data containers. A 'shiny' application provides access to
all features without requiring any programming knowledge. The package is
described in further detail in Wirth et al. (2023)
<doi:10.1038/s41596-023-00850-7>.

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
