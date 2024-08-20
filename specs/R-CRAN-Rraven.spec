%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rraven
%global packver   1.0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.14
Release:          1%{?dist}%{?buildtag}
Summary:          Connecting R and 'Raven' Sound Analysis Software

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-warbleR >= 1.1.32
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-methods 
Requires:         R-CRAN-warbleR >= 1.1.32
Requires:         R-CRAN-pbapply 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-tuneR 
Requires:         R-methods 

%description
A tool to exchange data between R and 'Raven' sound analysis software
(Cornell Lab of Ornithology). Functions work on data formats compatible
with the R package 'warbleR'.

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
