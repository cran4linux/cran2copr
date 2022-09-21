%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MCDA
%global packver   0.0.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.22
Release:          1%{?dist}%{?buildtag}
Summary:          Support for the Multicriteria Decision Aiding Process

License:          EUPL (== 1.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-glpkAPI 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 

%description
Support for the analyst in a Multicriteria Decision Aiding (MCDA) process
with algorithms, preference elicitation and data visualisation functions.
Sébastien Bigaret, Richard Hodgett, Patrick Meyer, Tatyana Mironova,
Alexandru Olteanu (2017) Supporting the multi-criteria decision aiding
process : R and the MCDA package, Euro Journal On Decision Processes,
Volume 5, Issue 1 - 4, pages 169 - 194 <doi:10.1007/s40070-017-0064-1>.

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
