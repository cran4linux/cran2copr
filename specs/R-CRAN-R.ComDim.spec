%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R.ComDim
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Common Dimensions (ComDim) Multi-Block Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ConsensusOPLS 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ConsensusOPLS 

%description
Common Dimensions (ComDim) is a multi-block method that simultaneously
considers multiple data tables to find latent components that are common
to all the tables as well as those specific to each data table, along with
the contribution of each table to each component. See Jouan-Rimbaud
Bouveresse and Rutledge (2024) <doi:10.1002/cem.3454>, Boccard and
Rutledge (2013) <doi:10.1016/j.aca.2013.01.022>, and Puig-Castellví et al.
(2021) <doi:10.1016/j.chemolab.2021.104422>.

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
