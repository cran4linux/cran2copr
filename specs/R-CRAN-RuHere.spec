%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RuHere
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flags Spatial Errors in Biological Collection Data Using Specialists' Information

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RcppArmadillo >= 15.0.2.2
BuildRequires:    R-CRAN-florabr >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-faunabr >= 1.0.0
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-rredlist 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-BIEN 
BuildRequires:    R-CRAN-ridigbio 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggnewscale 
Requires:         R-CRAN-florabr >= 1.3.1
Requires:         R-CRAN-faunabr >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-terra 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-rredlist 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-BIEN 
Requires:         R-CRAN-ridigbio 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggnewscale 

%description
Automatically flags common spatial errors in biological collection data
using metadata and specialists' information. RuHere implements a workflow
to manage occurrence data through six steps: dataset merging, metadata
flagging, validation against expert-derived distribution maps,
visualization of flagged records, and sampling bias exploration. It
specifically integrates specialist-curated range information to identify
geographic errors and introductions that often escape standard automated
validation procedures. For details on the methodology, see: Trindade &
Caron (2026) <doi:10.64898/2026.02.02.703373>.

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
