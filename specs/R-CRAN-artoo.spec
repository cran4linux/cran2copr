%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  artoo
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Lossless CDISC-Native Input and Output for Clinical Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-nanoparquet >= 0.3.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-utf8 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-nanoparquet >= 0.3.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-utf8 

%description
Reads and writes clinical-trial datasets losslessly across 'SAS' XPORT
(XPT), Clinical Data Interchange Standards Consortium (CDISC)
Dataset-JSON, and 'Apache Parquet', applying a specification to produce
submission-ready Study Data Tabulation Model (SDTM) and Analysis Data
Model (ADaM) datasets. A single canonical metadata model carries labels,
CDISC data types, lengths, 'SAS' display formats, controlled-terminology
references, and sort keys identically across every format, so conversion
between any two formats is lossless by construction. Pure 'R' and
lightweight, with no external 'SAS' or 'Java' runtime. Implements the
published format specifications for CDISC Dataset-JSON
(<https://cdisc-org.github.io/DataExchange-DatasetJson/doc/dataset-json1-1.html>)
and 'SAS' XPORT
(<https://www.loc.gov/preservation/digital/formats/fdd/fdd000466.shtml>).

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
