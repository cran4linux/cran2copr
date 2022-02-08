%global __brp_check_rpaths %{nil}
%global packname  fcfdr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible cFDR

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-locfdr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-polyCub 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-bigsplines 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-locfdr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-polyCub 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-bigsplines 
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 

%description
Provides functions to implement the Flexible cFDR (Hutchinson et al.
(2021) <doi:10.1371/journal.pgen.1009853>) and Binary cFDR (Hutchinson et
al. (2021) <doi:10.1101/2021.10.21.465274>) methodologies to leverage
auxiliary data from arbitrary distributions, for example functional
genomic data, with GWAS p-values to generate re-weighted p-values.

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
