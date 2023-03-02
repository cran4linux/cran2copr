%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ISO11784Tools
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          ISO11784 PIT Tag ID Format Converters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 

%description
Some tools to assist with converting International Organization for
Standardization (ISO) standard 11784 (ISO11784) animal ID codes between 4
recognised formats commonly displayed on Passive Integrated Transponder
(PIT) tag readers. The most common formats are 15 digit decimal, e.g.,
999123456789012, and 13 character hexadecimal 'dot' format, e.g.,
3E7.1CBE991A14. These are referred to in this package as isodecimal and
isodothex. The other two formats are the raw hexadecimal representation of
the ISO11784 binary structure (see
<https://en.wikipedia.org/wiki/ISO_11784_and_ISO_11785>). There are two
'flavours' of this format, a left and a right variation. Which flavour a
reader happens to output depends on if the developers decided to reverse
the binary number or not before converting to hexadecimal, a decision
based on the fact that the PIT tags will transmit their binary code Least
Significant Bit (LSB) first, or backwards basically.

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
