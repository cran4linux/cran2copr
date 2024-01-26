%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modACDC
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Association of Covariance for Detecting Differential Co-Expression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CCP 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-genieclust 
BuildRequires:    R-CRAN-genio 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-partition 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-CCP 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-genieclust 
Requires:         R-CRAN-genio 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-partition 
Requires:         R-parallel 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 

%description
A series of functions to implement association of covariance for detecting
differential co-expression (ACDC), a novel approach for detection of
differential co-expression that simultaneously accommodates multiple
phenotypes or exposures with binary, ordinal, or continuous data types.
Users can use the default method which identifies modules by Partition or
may supply their own modules. Also included are functions to choose an
information loss criterion (ILC) for Partition using OmicS-data-based
Complex trait Analysis (OSCA) and Genome-wide Complex trait Analysis
(GCTA). The manuscript describing these methods is as follows: Queen K,
Nguyen MN, Gilliland F, Chun S, Raby BA, Millstein J. "ACDC: a general
approach for detecting phenotype or exposure associated co-expression"
(2023) <doi:10.3389/fmed.2023.1118824>.

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
