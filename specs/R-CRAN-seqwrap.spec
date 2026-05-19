%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seqwrap
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Item-by-Item Iterative Model Fitting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-broom.mixed 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-broom.mixed 

%description
Models high-dimensional data, such as RNA-seq or proteomic data using an
item-by-item strategy. The package contains functions to wrap
high-dimensional data and iterate over them using established R packages
for regression modelling (e.g., 'glmmTMB' or 'mgcv').

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
