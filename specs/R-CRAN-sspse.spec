%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sspse
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Hidden Population Size using Respondent Driven Sampling Data

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RDS 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-coda 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-RDS 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-coda 

%description
Estimate the size of a networked population based on respondent-driven
sampling data. The package is part of the "RDS Analyst" suite of packages
for the analysis of respondent-driven sampling data. See Handcock, Gile
and Mar (2014) <doi:10.1214/14-EJS923> and Handcock, Gile and Mar (2015)
<doi:10.1111/biom.12255>.

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
