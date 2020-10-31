%global packname  tidyBF
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Wrapper for 'BayesFactor' Package

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ipmisc >= 4.1.0
BuildRequires:    R-CRAN-parameters >= 0.9.0
BuildRequires:    R-CRAN-metaBMA >= 0.6.5
BuildRequires:    R-CRAN-performance >= 0.5.1
BuildRequires:    R-CRAN-effectsize >= 0.4.0
BuildRequires:    R-CRAN-insight >= 0.10.0
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ipmisc >= 4.1.0
Requires:         R-CRAN-parameters >= 0.9.0
Requires:         R-CRAN-metaBMA >= 0.6.5
Requires:         R-CRAN-performance >= 0.5.1
Requires:         R-CRAN-effectsize >= 0.4.0
Requires:         R-CRAN-insight >= 0.10.0
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Provides helper functions that make it easy to run 'BayesFactor' package
tests on a data which is in a tidy format. Additionally, it provides a
more consistent syntax and by default returns a dataframe with rich
details. These functions can also return expressions containing results
from Bayes Factor tests that can then be displayed on custom plots.
Posterior estimation is carried out using the 'bayestestR' package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
