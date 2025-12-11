%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HCUPtools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Work with HCUP Resources and Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-readxl 

%description
A comprehensive R package for accessing and working with publicly
available and free resources from the Agency for Healthcare Research and
Quality (AHRQ) Healthcare Cost and Utilization Project (HCUP). The package
provides streamlined access to HCUP's Clinical Classifications Software
Refined (CCSR) mapping files and Summary Trend Tables, enabling
researchers and analysts to efficiently map ICD-10-CM diagnosis codes and
ICD-10-PCS procedure codes to CCSR categories and access HCUP statistical
reports. Key features include: direct download from HCUP website, multiple
output formats (long/wide/default), cross-classification support, version
management, citation generation, and intelligent caching. The package does
not redistribute HCUP data files but facilitates direct download from the
official HCUP website, ensuring users always have access to the latest
versions and maintain compliance with HCUP data use policies. This package
only accesses free public tools and reports; it does NOT access HCUP
databases (NIS, KID, SID, NEDS, etc.) that require purchase. For more
information, see <https://hcup-us.ahrq.gov/>.

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
