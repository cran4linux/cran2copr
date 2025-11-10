%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyseurat
%global packver   0.8.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.7
Release:          1%{?dist}%{?buildtag}
Summary:          Brings Seurat to the Tidyverse

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 4.3.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-ttservice >= 0.3.8
BuildRequires:    R-CRAN-SeuratObject 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-Seurat >= 4.3.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-ttservice >= 0.3.8
Requires:         R-CRAN-SeuratObject 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fansi 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-generics 

%description
It creates an invisible layer that allow to see the 'Seurat' object as
tibble and interact seamlessly with the tidyverse.

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
