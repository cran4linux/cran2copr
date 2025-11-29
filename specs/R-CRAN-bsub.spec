%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bsub
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Submitter and Monitor of the 'LSF Cluster'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GetoptLong >= 0.1.8
BuildRequires:    R-CRAN-GlobalOptions >= 0.1.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-ssh 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-GetoptLong >= 0.1.8
Requires:         R-CRAN-GlobalOptions >= 0.1.1
Requires:         R-CRAN-digest 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-crayon 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-ssh 
Requires:         R-CRAN-igraph 

%description
It submits R code/R scripts/shell commands to 'LSF cluster'
(<https://en.wikipedia.org/wiki/Platform_LSF>, the 'bsub' system) without
leaving R. There is also an interactive 'shiny' application for monitoring
job status.

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
