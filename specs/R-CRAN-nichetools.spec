%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nichetools
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Complementary Package to 'nicheROVER' and 'SIBER'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-nicheROVER 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-SIBER 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-nicheROVER 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-SIBER 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Provides functions complementary to packages 'nicheROVER' and 'SIBER'
allowing the user to extract Bayesian estimates from data objects created
by the packages 'nicheROVER' and 'SIBER'. Please see the following
publications for detailed methods on 'nicheROVER' and 'SIBER' Hansen et
al. (2015) <doi:10.1890/14-0235.1>, Jackson et al. (2011)
<doi:10.1111/j.1365-2656.2011.01806.x>, and Layman et al. (2007)
<doi:10.1890/0012-9658(2007)88[42:CSIRPF]2.0.CO;2>, respectfully.

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
