%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyestimate
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Tidy Implementation of 'ESTIMATE'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggplot2 

%description
The 'ESTIMATE' package infers tumor purity from expression data as a
function of immune and stromal infiltrate, but requires writing of
intermediate files, is un-pipeable, and performs poorly when presented
with modern datasets with current gene symbols. 'tidyestimate' a fast,
tidy, modern reimagination of 'ESTIMATE' (2013) <doi:10.1038/ncomms3612>.

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
