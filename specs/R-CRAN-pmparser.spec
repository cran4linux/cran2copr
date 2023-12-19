%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pmparser
%global packver   1.0.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.19
Release:          1%{?dist}%{?buildtag}
Summary:          Create and Maintain a Relational Database of Data from PubMed/MEDLINE

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3.2
BuildRequires:    R-CRAN-withr >= 2.3.0
BuildRequires:    R-CRAN-R.utils >= 2.10.1
BuildRequires:    R-CRAN-RCurl >= 1.98
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-xml2 >= 1.3.3
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-iterators >= 1.0.12
Requires:         R-CRAN-curl >= 4.3.2
Requires:         R-CRAN-withr >= 2.3.0
Requires:         R-CRAN-R.utils >= 2.10.1
Requires:         R-CRAN-RCurl >= 1.98
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-xml2 >= 1.3.3
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-iterators >= 1.0.12

%description
Provides a simple interface for extracting various elements from the
publicly available PubMed XML files, incorporating PubMed's regular
updates, and combining the data with the NIH Open Citation Collection. See
Schoenbachler and Hughey (2021) <doi:10.7717/peerj.11071>.

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
