%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdaPOIFD
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Partially Observed Integrated Functional Depth

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-igraph 

%description
Integrated Functional Depth for Partially Observed Functional Data and
applications to visualization, outlier detection and classification. It
implements the methods proposed in: Elías, A., Jiménez, R., Paganoni, A.
M. and Sangalli, L. M., (2023), "Integrated Depth for Partially Observed
Functional Data", Journal of Computational and Graphical Statistics,
<doi:10.1080/10618600.2022.2070171>. Elías, A., Jiménez, R., & Shang, H.
L. (2023), "Depth-based reconstruction method for incomplete functional
data", Computational Statistics, <doi:10.1007/s00180-022-01282-9>. Elías,
A., Nagy, S. (2024), "Statistical properties of partially observed
integrated functional depths", TEST, <doi:10.1007/s11749-024-00954-6>.

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
