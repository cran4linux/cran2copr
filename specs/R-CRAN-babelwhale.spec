%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  babelwhale
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Talking to 'Docker' and 'Singularity' Containers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         docker
Requires:         singularity
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.5.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-dynutils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-processx >= 3.5.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-dynutils 
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-glue 

%description
Provides a unified interface to interact with 'docker' and 'singularity'
containers.  You can execute a command inside a container, mount a volume
or copy a file.

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
