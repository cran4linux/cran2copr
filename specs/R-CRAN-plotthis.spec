%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plotthis
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          High-Level Plotting Built Upon 'ggplot2' and Other Plotting Packages

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridtext 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridtext 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-zoo 

%description
Provides high-level API and a wide range of options to create stunning,
publication-quality plots effortlessly. It is built upon 'ggplot2' and
other plotting packages, and is designed to be easy to use and to work
seamlessly with 'ggplot2' objects. It is particularly useful for creating
complex plots with multiple layers, facets, and annotations. It also
provides a set of functions to create plots for specific types of data,
such as Venn diagrams, alluvial diagrams, and phylogenetic trees. The
package is designed to be flexible and customizable, and to work well with
the 'ggplot2' ecosystem. The API can be found at
<https://pwwang.github.io/plotthis/reference/index.html>.

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
