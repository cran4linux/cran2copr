%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsBaseClient
%global packver   6.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          'DataSHIELD' Client Side Base Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DSI >= 1.7.1
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-DSI >= 1.7.1
Requires:         R-CRAN-fields 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 

%description
Base 'DataSHIELD' functions for the client side. 'DataSHIELD' is a
software package which allows you to do non-disclosive federated analysis
on sensitive data. 'DataSHIELD' analytic functions have been designed to
only share non disclosive summary statistics, with built in automated
output checking based on statistical disclosure control. With data sites
setting the threshold values for the automated output checks. For more
details, see citation('dsBaseClient').

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
