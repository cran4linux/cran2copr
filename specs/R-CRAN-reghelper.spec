%global packname  reghelper
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Helper Functions for Regression Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-stats 
Requires:         R-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-utils 

%description
A set of functions used to automate commonly used methods in regression
analysis. This includes plotting interactions, and calculating simple
slopes, standardized coefficients, regions of significance (Johnson &
Neyman, 1936; cf. Spiller et al., 2012), etc. See the reghelper
documentation for more information, documentation, and examples.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
