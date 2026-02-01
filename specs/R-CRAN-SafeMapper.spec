%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SafeMapper
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fault-Tolerant Functional Programming with Automatic Checkpointing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-tools 
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-digest 
Requires:         R-tools 

%description
Provides drop-in replacements for 'purrr' and 'furrr' mapping functions
with built-in fault tolerance, automatic checkpointing, and seamless
recovery capabilities. When long-running computations are interrupted due
to errors, system crashes, or other failures, simply re-run the same code
to automatically resume from the last checkpoint. Ideal for large-scale
data processing, API calls, web scraping, and other time-intensive
operations where reliability is critical. For 'purrr' methodology, see
Wickham and Henry (2023) <https://purrr.tidyverse.org/>.

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
