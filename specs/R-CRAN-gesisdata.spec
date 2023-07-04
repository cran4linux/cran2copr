%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gesisdata
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Data Retrieval from the GESIS Data Archive

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RSelenium >= 1.7.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-netstat 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-RSelenium >= 1.7.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-netstat 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
Reproducible, programmatic retrieval of datasets from the GESIS Data
Archive.  The GESIS Data Archive <https://search.gesis.org> makes
available thousands of invaluable datasets, but researchers using these
datasets are caught in a bind.  The archive's terms and conditions bar
dissemination of downloaded datasets to third parties, but to ensure that
one's work can be reproduced, assessed, and built upon by others, one must
provide access to the raw data one has employed.  The 'gesisdata' package
cuts this knot by providing registered users with programmatic,
reproducible access to GESIS datasets from within 'R'.

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
