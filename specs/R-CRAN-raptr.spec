%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  raptr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Representative and Adequate Prioritization Toolkit in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-PBSmapping >= 2.73.0
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-hypervolume >= 2.0.7
BuildRequires:    R-CRAN-terra >= 1.6.47
BuildRequires:    R-CRAN-sp >= 1.4.6
BuildRequires:    R-CRAN-shape >= 1.4.6
BuildRequires:    R-CRAN-Matrix >= 1.4.1
BuildRequires:    R-CRAN-boot >= 1.3.28
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-ks >= 1.13.5
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-CRAN-sf >= 1.0.9
BuildRequires:    R-CRAN-adehabitatHR >= 0.4.19
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-PBSmapping >= 2.73.0
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-hypervolume >= 2.0.7
Requires:         R-CRAN-terra >= 1.6.47
Requires:         R-CRAN-sp >= 1.4.6
Requires:         R-CRAN-shape >= 1.4.6
Requires:         R-CRAN-Matrix >= 1.4.1
Requires:         R-CRAN-boot >= 1.3.28
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-ks >= 1.13.5
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-CRAN-sf >= 1.0.9
Requires:         R-CRAN-adehabitatHR >= 0.4.19
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Biodiversity is in crisis. The overarching aim of conservation is to
preserve biodiversity patterns and processes. To this end, protected areas
are established to buffer species and preserve biodiversity processes. But
resources are limited and so protected areas must be cost-effective. This
package contains tools to generate plans for protected areas
(prioritizations), using spatially explicit targets for biodiversity
patterns and processes. To obtain solutions in a feasible amount of time,
this package uses the commercial 'Gurobi' software (obtained from
<https://www.gurobi.com/>). For more information on using this package,
see Hanson et al. (2018) <doi:10.1111/2041-210X.12862>.

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
