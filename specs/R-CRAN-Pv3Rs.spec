%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Pv3Rs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate the Cause of Recurrent Vivax Malaria using Genetic Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-multicool 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 

%description
Plot malaria parasite genetic data on two or more episodes. Compute
per-person posterior probabilities that each Plasmodium vivax (Pv)
recurrence is a recrudescence, relapse, or reinfection (3Rs) using
per-person P. vivax genetic data on two or more episodes and a statistical
model described in Taylor, Foo and White (2022)
<doi:10.1101/2022.11.23.22282669>. Plot per-recurrence posterior
probabilities.

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
