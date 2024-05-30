%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dartR.data
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Auxiliary Data Package for Our Main Package 'dartR'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-adegenet >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-adegenet >= 2.0.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-crayon 

%description
Data package for 'dartR'. Provides data sets to run examples in 'dartR'.
This was necessary due to the size limit imposed by 'CRAN'. The data in
'dartR.data' is needed to run the examples provided in the 'dartR'
functions. All available data sets are either based on actual data (but
reduced in size) and/or simulated data sets to allow the fast execution of
examples and demonstration of the functions.

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
