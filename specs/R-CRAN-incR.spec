%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  incR
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Incubation Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-utils 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-suncalc 
Requires:         R-CRAN-lubridate 
Requires:         R-utils 

%description
Suite of functions to study animal incubation. At the core of incR lies an
algorithm that allows for the scoring of incubation behaviour.
Additionally, several functions extract biologically relevant metrics of
incubation such as off-bout number and off-bout duration - for a review of
avian incubation studies, see Nests, Eggs, and Incubation: New ideas about
avian reproduction (2015) edited by D. Charles Deeming and S. James
Reynolds <doi:10.1093/acprof:oso/9780198718666.001.0001>.

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
