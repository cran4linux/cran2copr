%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jellyfisher
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize Spatiotemporal Tumor Evolution with Jellyfish Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 

%description
Generates interactive Jellyfish plots to visualize spatiotemporal tumor
evolution by integrating sample and phylogenetic trees into a unified
plot. This approach provides an intuitive way to analyze tumor
heterogeneity and evolution over time and across anatomical locations. The
Jellyfish plot visualization design was first introduced by Lahtinen,
Lavikka, et al. (2023, <doi:10.1016/j.ccell.2023.04.017>). This package
also supports visualizing ClonEvol results, a tool developed by Dang, et
al. (2017, <doi:10.1093/annonc/mdx517>), for analyzing clonal evolution
from multi-sample sequencing data. The 'clonevol' package is not available
on CRAN but can be installed from its GitHub repository
(<https://github.com/hdng/clonevol>).

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
