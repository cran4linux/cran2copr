%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FracFixR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Statistical Framework for RNA Fractionation Analysis

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-future.apply >= 1.8.1
BuildRequires:    R-CRAN-nnls >= 1.4
BuildRequires:    R-CRAN-aod >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-matrixStats >= 0.60.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-future.apply >= 1.8.1
Requires:         R-CRAN-nnls >= 1.4
Requires:         R-CRAN-aod >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-matrixStats >= 0.60.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-future 
Requires:         R-grDevices 

%description
A compositional statistical framework for absolute proportion estimation
between fractions in RNA sequencing data. 'FracFixR' addresses the
fundamental challenge in fractionated RNA-seq experiments where library
preparation and sequencing depth obscure the original proportions of RNA
fractions. It reconstructs original fraction proportions using
non-negative linear regression, estimates the "lost" unrecoverable
fraction, corrects individual transcript frequencies, and performs
differential proportion testing between conditions. Supports any RNA
fractionation protocol including polysome profiling, sub-cellular
localization, and RNA-protein complex isolation.

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
