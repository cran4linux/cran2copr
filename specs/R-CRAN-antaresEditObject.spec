%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  antaresEditObject
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Edit an 'Antares' Simulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-antaresRead >= 2.4.2
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-memuse 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-antaresRead >= 2.4.2
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-memuse 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-future 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-lifecycle 

%description
Edit an 'Antares' simulation before running it : create new areas, links,
thermal clusters or binding constraints or edit existing ones. Update
'Antares' general & optimization settings. 'Antares' is an open source
power system generator, more information available here :
<https://antares-simulator.org/>.

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
