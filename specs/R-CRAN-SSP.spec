%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSP
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulated Sampling Procedure for Community Ecology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-vegan 
Requires:         R-stats 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-ggplot2 

%description
The Simulation-based Sampling Protocol (SSP) is an R package designed to
estimate sampling effort in studies of ecological communities. It is based
on the concept of pseudo-multivariate standard error (MultSE) (Anderson &
Santana-Garcon, 2015, <doi:10.1111/ele.12385>) and the simulation of
ecological data. The theoretical background is described in Guerra-Castro
et al. (2020, <doi:10.1111/ecog.05284>).

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
