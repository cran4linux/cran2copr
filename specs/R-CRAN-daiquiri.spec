%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  daiquiri
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Quality Reporting for Temporal Datasets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-cowplot >= 0.9.3
BuildRequires:    R-CRAN-reactable >= 0.2.3
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-cowplot >= 0.9.3
Requires:         R-CRAN-reactable >= 0.2.3
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 
Requires:         R-stats 

%description
Generate reports that enable quick visual review of temporal shifts in
record-level data. Time series plots showing aggregated values are
automatically created for each data field (column) depending on its
contents (e.g. min/max/mean values for numeric data, no. of distinct
values for categorical data), as well as overviews for missing values,
non-conformant values, and duplicated rows. The resulting reports are
shareable and can contribute to forming a transparent record of the entire
analysis process. It is designed with Electronic Health Records in mind,
but can be used for any type of record-level temporal data (i.e. tabular
data where each row represents a single "event", one column contains the
"event date", and other columns contain any associated values for the
event).

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
