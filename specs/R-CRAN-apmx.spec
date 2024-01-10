%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apmx
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Population Pharmacokinetic Dataset Assembly

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-this.path 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-arsenal 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-this.path 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-arsenal 

%description
Automated methods to assemble population PK (pharmacokinetic) and PKPD
(pharmacodynamic) datasets for analysis in 'NONMEM' (non-linear mixed
effects modeling) by Bauer (2019) <doi:10.1002/psp4.12404>. The package
includes functions to build datasets from SDTM (study data tabulation
module) <https://www.cdisc.org/standards/foundational/sdtm>, ADaM
(analysis dataset module)
<https://www.cdisc.org/standards/foundational/adam>, or other dataset
formats. The package will combine population datasets, add covariates, and
create documentation to support regulatory submission and internal
communication.

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
