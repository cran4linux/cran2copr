%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gRaphiaExtra
%global packver   0.26.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.26.9
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for Integrating 'Seurat' Objects into 'gRaphia'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.2.0
Requires:         R-core >= 4.4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Utilising graph-based network analysis frameworks, 'Graphia'
<https://graphia.app/> is a powerful open source visual analytics
application developed to aid the interpretation of large and complex
datasets. For more details, see article by Freeman et al. (2022)
<doi:10.1371/journal.pcbi.1010310>. 'gRaphia' is an extension of the
'Graphia' application within the R environment, providing tools for
network analysis and visualisation. 'gRaphiaExtra' provides additional
functionality specifically designed for single-cell RNA-sequencing data,
enabling users to seamlessly integrate and utilise existing 'Seurat'
analysis outputs in 'gRaphia'. The package also provides supplementary
functions to support and enhance the 'gRaphia' analysis framework.

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
