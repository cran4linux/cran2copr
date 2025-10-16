%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bakerrr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Background-Parallel Jobs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 1.1.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-carrier 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-S7 
Requires:         R-CRAN-purrr >= 1.1.0
Requires:         R-CRAN-callr 
Requires:         R-CRAN-carrier 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-config 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-S7 

%description
Easily launch, track, and control functions as background-parallel jobs.
Includes robust utilities for job status, error handling, resource
monitoring, and result collection. Designed for scalable workflows in
interactive and automated settings (local or remote). Integrates with
multiple backends; supports flexible automation pipelines and live job
tracking. For more information, see
<https://anirbanshaw24.github.io/bakerrr/>.

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
