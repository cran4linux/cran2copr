%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nhanesR
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Download, Parse, and Analyze NHANES Data with Mortality Linkage

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-haven >= 2.5.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-tools 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-haven >= 2.5.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-tools 

%description
Provides tools for downloading and organizing National Health and
Nutrition Examination Survey (NHANES) public-use data files and the
National Center for Health Statistics (NCHS) Public-Use Linked Mortality
Files (LMF). Supports structured local caching, codebook access,
survey-aware merging, and preparation of survival analysis datasets using
NHANES-National Death Index (NDI) linked mortality data (follow-up through
December 31, 2019). NHANES methodology is described at
<https://wwwn.cdc.gov/nchs/nhanes/Default.aspx>.

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
