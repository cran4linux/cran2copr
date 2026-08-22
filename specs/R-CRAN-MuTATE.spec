%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MuTATE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Target Automated Tree Engine (MuTATE)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggraph 
Requires:         R-grDevices 

%description
Recursively partitions datasets on binary splits across multiple targets
having different dependent variable types, including categorical,
continuous, count, and survival outcomes. This overcomes single-target
limitations of traditional decision trees while retaining model
interpretability. See Ayton and Trevino (2023)
<doi:10.1093/bioinformatics/btad507> and Ayton et al. (2025)
<doi:10.1038/s44401-025-00025-4> for details.

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
