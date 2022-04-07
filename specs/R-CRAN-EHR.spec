%global __brp_check_rpaths %{nil}
%global packname  EHR
%global packver   0.4-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Electronic Health Record (EHR) Data Processing and Analysis Tool

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-pkdata 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-pkdata 

%description
Process and analyze electronic health record (EHR) data. The 'EHR' package
provides modules to perform diverse medication-related studies using data
from EHR databases. Especially, the package includes modules to perform
pharmacokinetic/pharmacodynamic (PK/PD) analyses using EHRs, as outlined
in Choi, Beck, McNeer, Weeks, Williams, James, Niu, Abou-Khalil, Birdwell,
Roden, Stein, Bejan, Denny, and Van Driest (2020) <doi:10.1002/cpt.1787>.
Additional modules will be added in future. In addition, this package
provides various functions useful to perform Phenome Wide Association
Study (PheWAS) to explore associations between drug exposure and
phenotypes obtained from EHR data, as outlined in Choi, Carroll, Beck,
Mosley, Roden, Denny, and Van Driest (2018)
<doi:10.1093/bioinformatics/bty306>.

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
