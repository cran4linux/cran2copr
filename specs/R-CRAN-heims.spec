%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heims
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Decode and Validate HEIMS Data from Department of Education, Australia

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hutils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hutils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-lubridate 

%description
Decode elements of the Australian Higher Education Information Management
System (HEIMS) data for clarity and performance. HEIMS is the record
system of the Department of Education, Australia to record enrolments and
completions in Australia's higher education system, as well as a range of
relevant information. For more information, including the source of the
data dictionary, see
<https://web.archive.org/web/20180210074903/http://heimshelp.education.gov.au/sites/heimshelp/dictionary/pages/data-element-dictionary>.
That collection has since been superseded by the Tertiary Collection of
Student Information, whose data element dictionary is at
<https://www.tcsisupport.gov.au/element>.

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
