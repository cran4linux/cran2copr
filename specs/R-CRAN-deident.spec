%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deident
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Persistent Data Anonymization Pipeline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-lemon 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-R6 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-lemon 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-fs 

%description
A framework for the replicable removal of personally identifiable data
(PID) in data sets.  The package implements a suite of methods to suit
different data types based on the suggestions of Garfinkel (2015)
<doi:10.6028/NIST.IR.8053> and the ICO "Guidelines on Anonymization"
(2012) <https://ico.org.uk/media/1061/anonymisation-code.pdf>.

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
