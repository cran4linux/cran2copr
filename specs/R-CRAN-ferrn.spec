%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ferrn
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Facilitate Exploration of touRR optimisatioN

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-geozoo 
BuildRequires:    R-CRAN-tourr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-geozoo 
Requires:         R-CRAN-tourr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-tidyr 

%description
Diagnostic plots for optimisation, with a focus on projection pursuit.
These show paths the optimiser takes in the high-dimensional space in
multiple ways: by reducing the dimension using principal component
analysis, and also using the tour to show the path on the high-dimensional
space. Several botanical colour palettes are included, reflecting the name
of the package. A paper describing the methodology can be found at
<https://journal.r-project.org/archive/2021/RJ-2021-105/index.html>.

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
