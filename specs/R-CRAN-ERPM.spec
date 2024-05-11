%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ERPM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exponential Random Partition Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-snowfall 
Requires:         R-CRAN-numbers 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-snowfall 

%description
Simulates and estimates the Exponential Random Partition Model presented
in the paper Hoffman, Block, and Snijders (2023)
<doi:10.1177/00811750221145166>. It can also be used to estimate
longitudinal partitions, following the model proposed in Hoffman and
Chabot (2023) <doi:10.1016/j.socnet.2023.04.002>. The model is an
exponential family distribution on the space of partitions (sets of
non-overlapping groups) and is called in reference to the Exponential
Random Graph Models (ERGM) for networks.

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
