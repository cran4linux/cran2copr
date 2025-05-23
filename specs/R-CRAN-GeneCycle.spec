%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeneCycle
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Identification of Periodically Expressed Genes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool >= 1.2.5
BuildRequires:    R-CRAN-longitudinal >= 1.1.3
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-fdrtool >= 1.2.5
Requires:         R-CRAN-longitudinal >= 1.1.3
Requires:         R-CRAN-MASS 

%description
The GeneCycle package implements the approaches of Wichert et al. (2004)
<doi:10.1093/bioinformatics/btg364>, Ahdesmaki et al. (2005)
<doi:10.1186/1471-2105-6-117> and Ahdesmaki et al. (2007)
<DOI:10.1186/1471-2105-8-233> for detecting periodically expressed genes
from gene expression time series data.

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
