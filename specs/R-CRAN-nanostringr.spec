%global packname  nanostringr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Performs Quality Control, Data Normalization, and Batch Effect Correction for 'NanoString nCounter' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-ccaPP 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-ccaPP 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-epiR 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 

%description
Provides quality control (QC), normalization, and batch effect correction
operations for 'NanoString nCounter' data, Talhouk et al. (2016)
<doi:10.1371/journal.pone.0153844>.  Various metrics are used to determine
which samples passed or failed QC.  Gene expression should first be
normalized to housekeeping genes, before a reference-based approach is
used to adjust for batch effects.  Raw NanoString data can be imported in
the form of Reporter Code Count (RCC) files.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
