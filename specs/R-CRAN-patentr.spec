%global __brp_check_rpaths %{nil}
%global packname  patentr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access USPTO Bulk Data in Tidy Rectangular Format

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-magrittr >= 2.0
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-xml2 >= 1.3.2
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr >= 2.0
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-xml2 >= 1.3.2
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-utils 

%description
Converts TXT and XML data curated by the United States Patent and
Trademark Office (USPTO). Allows conversion of bulk data after downloading
directly from the USPTO bulk data website, eliminating need for users to
wrangle multiple data formats to get large patent databases in tidy,
rectangular format. Data details can be found on the USPTO website
<https://bulkdata.uspto.gov/>. Currently, all 3 formats: 1. TXT data
(1976-2001); 2. XML format 1 data (2002-2004); and 3. XML format 2 data
(2005-current) can be converted to rectangular, CSV format. Relevant
literature that uses data from USPTO includes Wada (2020)
<doi:10.1007/s11192-020-03674-4> and Plaza & Albert (2008)
<doi:10.1007/s11192-007-1763-3>.

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
