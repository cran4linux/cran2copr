%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  packageRank
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Computation and Visualization of Package Download Counts and Percentile Ranks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-cranlogs 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fasttime 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ISOcodes 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-pkgsearch 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rversions 
BuildRequires:    R-CRAN-sugrrants 
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-cranlogs 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fasttime 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ISOcodes 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-pkgsearch 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rversions 
Requires:         R-CRAN-sugrrants 

%description
Compute and visualize package download counts and percentile ranks from
Posit/RStudio's CRAN mirror.

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
