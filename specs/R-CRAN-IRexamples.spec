%global __brp_check_rpaths %{nil}
%global packname  IRexamples
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Practical Institutional Research Examples and Tutorials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-RSelenium 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-DisImpact 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-twang 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-RSelenium 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-DisImpact 
Requires:         R-CRAN-forcats 

%description
Provides examples of code for analyzing data or accomplishing tasks that
may be useful to institutional or educational researchers.

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
