%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  banffIT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatize Diagnosis Standardized Assignation Using the Banff Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fabR 
BuildRequires:    R-CRAN-madshapR 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fabR 
Requires:         R-CRAN-madshapR 

%description
Assigns standardized diagnoses using the Banff Classification (Category 1
to 6 diagnoses, including Acute and Chronic active T-cell mediated
rejection as well as Active, Chronic active, and Chronic antibody mediated
rejection). The main function considers a minimal dataset containing
biopsies information in a specific format (described by a data
dictionary), verifies its content and format (based on the data
dictionary), assigns diagnoses, and creates a summary report. The package
is developed on the reference guide to the Banff classification of renal
allograft pathology Roufosse C, Simmonds N, Clahsen-van Groningen M, et
al. A (2018) <doi:10.1097/TP.0000000000002366>. The full description of
the Banff classification is available at <https://banfffoundation.org/>.

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
