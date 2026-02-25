%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggpubr
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot2' Based Publication Ready Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.2
BuildRequires:    R-CRAN-rstatix >= 0.7.2
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggsignif 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-ggrepel >= 0.9.2
Requires:         R-CRAN-rstatix >= 0.7.2
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-grid 
Requires:         R-CRAN-ggsci 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggsignif 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 

%description
The 'ggplot2' package is excellent and flexible for elegant data
visualization in R. However the default generated plots requires some
formatting before we can send them for publication. Furthermore, to
customize a 'ggplot', the syntax is opaque and this raises the level of
difficulty for researchers with no advanced R programming skills. 'ggpubr'
provides some easy-to-use functions for creating and customizing
'ggplot2'- based publication ready plots.

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
