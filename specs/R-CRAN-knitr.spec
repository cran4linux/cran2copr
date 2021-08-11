%global __brp_check_rpaths %{nil}
%global packname  knitr
%global packver   1.33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.33
Release:          1%{?dist}%{?buildtag}
Summary:          A General-Purpose Package for Dynamic Report Generation in R

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-stringr >= 0.6
BuildRequires:    R-CRAN-xfun >= 0.21
BuildRequires:    R-CRAN-evaluate >= 0.10
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-tools 
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-stringr >= 0.6
Requires:         R-CRAN-xfun >= 0.21
Requires:         R-CRAN-evaluate >= 0.10
Requires:         R-CRAN-highr 
Requires:         R-methods 
Requires:         R-CRAN-markdown 
Requires:         R-tools 

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.

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
