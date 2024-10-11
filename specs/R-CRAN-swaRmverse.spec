%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  swaRmverse
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Swarm Space Creation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-trackdf 
BuildRequires:    R-CRAN-swaRm 
BuildRequires:    R-CRAN-geosphere 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-trackdf 
Requires:         R-CRAN-swaRm 
Requires:         R-CRAN-geosphere 

%description
Provides a pipeline for the comparative analysis of collective movement
data (e.g. fish schools, bird flocks, baboon troops) by processing
2-dimensional positional data (x,y,t) from GPS trackers or computer vision
tracking systems, discretizing events of collective motion, calculating a
set of established metrics that characterize each event, and placing the
events in a multi-dimensional swarm space constructed from these metrics.
The swarm space concept, the metrics and data sets included are described
in: Papadopoulou Marina, Furtbauer Ines, O'Bryan Lisa R., Garnier Simon,
Georgopoulou Dimitra G., Bracken Anna M., Christensen Charlotte and King
Andrew J. (2023) <doi:10.1098/rstb.2022.0068>.

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
