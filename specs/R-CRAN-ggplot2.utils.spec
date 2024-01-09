%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggplot2.utils
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Selected Utilities Extending 'ggplot2'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-ggpp 
BuildRequires:    R-CRAN-ggstats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-ggpp 
Requires:         R-CRAN-ggstats 
Requires:         R-CRAN-survival 

%description
Selected utilities, in particular 'geoms' and 'stats' functions, extending
the 'ggplot2' package. This package imports functions from 'EnvStats'
<doi:10.1007/978-1-4614-8456-1> by Millard (2013), 'ggpp'
<https://CRAN.R-project.org/package=ggpp> by Aphalo et al. (2023) and
'ggstats' <doi:10.5281/zenodo.10183964> by Larmarange (2023), and then
exports them. This package also contains modified code from 'ggquickeda'
<https://CRAN.R-project.org/package=ggquickeda> by Mouksassi et al. (2023)
for Kaplan-Meier lines and ticks additions to plots. All functions are
tested to make sure that they work reliably.

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
