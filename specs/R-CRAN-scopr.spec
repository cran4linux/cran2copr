%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scopr
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Read Ethoscope Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-behavr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-behavr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-memoise 

%description
Handling of behavioural data from the Ethoscope platform (Geissmann,
Garcia Rodriguez, Beckwith, French, Jamasb and Gilestro (2017)
<DOI:10.1371/journal.pbio.2003026>). Ethoscopes
(<https://giorgiogilestro.notion.site/Ethoscope-User-Manual-a9739373ae9f4840aa45b277f2f0e3a7>)
are an open source/open hardware framework made of interconnected
raspberry pis (<https://www.raspberrypi.org>) designed to quantify the
behaviour of multiple small animals in a distributed and real-time
fashion. The default tracking algorithm records primary variables such as
xy coordinates, dimensions and speed. This package is part of the
rethomics framework <https://rethomics.github.io/>.

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
