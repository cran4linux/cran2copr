%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cauphy
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Trait Evolution on Phylogenies Using the Cauchy Process

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-ape >= 5.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-HDInterval 
Requires:         R-CRAN-ape >= 5.5
Requires:         R-methods 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-HDInterval 

%description
The Cauchy Process can model pulsed continuous trait evolution on
phylogenies. The likelihood is tractable, and is used for parameter
inference and ancestral trait reconstruction. See Bastide and Didier
(2023) <doi:10.1093/sysbio/syad053>.

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
