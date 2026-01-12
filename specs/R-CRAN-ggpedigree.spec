%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggpedigree
%global packver   1.1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Pedigrees with 'ggplot2' and 'plotly'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BGmisc >= 1.4.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-BGmisc >= 1.4.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 

%description
Provides plotting functions for visualizing pedigrees and family trees.
The package complements a behavior genetics package 'BGmisc' [Garrison et
al. (2024) <doi:10.21105/joss.06203>] by rendering pedigrees using the
'ggplot2' framework. Features include support for duplicated individuals,
complex mating structures, integration with simulated pedigrees, and
layout customization. Due to the impending deprecation of kinship2,
version 1.0 incorporates the layout helper functions from kinship2. The
pedigree alignment algorithms are adapted from 'kinship2' [Sinnwell et al.
(2014) <doi:10.1159/000363105>]. We gratefully acknowledge the original
authors: Jason Sinnwell, Terry Therneau, Daniel Schaid, and Elizabeth
Atkinson for their foundational work.

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
