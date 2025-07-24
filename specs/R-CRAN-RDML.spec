%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RDML
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Importing Real-Time Thermo Cycler (qPCR) Data from RDML Format Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-tools >= 3.2
BuildRequires:    R-CRAN-R6 >= 2.0.1
BuildRequires:    R-CRAN-checkmate >= 1.6.2
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-xml2 >= 1.0
BuildRequires:    R-CRAN-rlist >= 0.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
Requires:         R-tools >= 3.2
Requires:         R-CRAN-R6 >= 2.0.1
Requires:         R-CRAN-checkmate >= 1.6.2
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-xml2 >= 1.0
Requires:         R-CRAN-rlist >= 0.4
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pipeR 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 

%description
Imports real-time thermo cycler (qPCR) data from Real-time PCR Data Markup
Language (RDML) and transforms to the appropriate formats of the 'qpcR'
and 'chipPCR' packages, as described in Rodiger et al. (2017)
<doi:10.1093/bioinformatics/btx528>. Contains a dendrogram visualization
for the structure of RDML object and GUI for RDML editing.

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
