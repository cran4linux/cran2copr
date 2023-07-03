%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ropercenter
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Data Retrieval from the Roper Center Data Archive

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RSelenium 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-netstat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-RSelenium 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-netstat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Reproducible, programmatic retrieval of datasets from the Roper Center
data archive.  The Roper Center for Public Opinion Research
<https://ropercenter.cornell.edu> maintains the largest archive of public
opinion data in existence, but researchers using these datasets are caught
in a bind.  The Center's terms and conditions bar redistribution of
downloaded datasets, but to ensure that one's work can be reproduced,
assessed, and built upon by others, one must provide access to the raw
data one employed.  The `ropercenter` package cuts this knot by providing
registered users with programmatic, reproducible access to Roper Center
datasets from within R.

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
