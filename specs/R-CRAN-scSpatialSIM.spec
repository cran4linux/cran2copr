%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scSpatialSIM
%global packver   0.1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Point Pattern Simulator for Spatial Cellular Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-proxy 

%description
Single cell resolution data has been valuable in learning about tissue
microenvironments and interactions between cells or spots. This package
allows for the simulation of this level of data, be it single cell or
‘spots’, in both a univariate (single metric or cell type) and bivariate
(2 or more metrics or cell types) ways. As more technologies come to
marker, more methods will be developed to derive spatial metrics from the
data which will require a way to benchmark methods against each other.
Additionally, as the field currently stands, there is not a gold standard
method to be compared against. We set out to develop an R package that
will allow users to simulate point patterns that can be biologically
informed from different tissue domains, holes, and varying degrees of
clustering/colocalization. The data can be exported as spatial files and a
summary file (like 'HALO'). <https://github.com/FridleyLab/scSpatialSIM/>.

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
