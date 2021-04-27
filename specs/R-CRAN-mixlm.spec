%global packname  mixlm
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Model ANOVA and Statistics for Education

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-leaps 
Requires:         R-CRAN-car 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-leaps 

%description
The main functions perform mixed models analysis by least squares or REML
by adding the function r() to formulas of lm() and glm(). A collection of
text-book statistics for higher education is also included, e.g.
modifications of the functions lm(), glm() and associated summaries from
the package 'stats'.

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
