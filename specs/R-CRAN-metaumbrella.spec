%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaumbrella
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Umbrella Review Package for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-powerSurvEpi 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-powerSurvEpi 
Requires:         R-CRAN-readxl 
Requires:         R-tcltk 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-xtable 

%description
A comprehensive range of facilities to perform umbrella reviews with
stratification of the evidence in R. The package accomplishes this aim by
building on three core functions that: (i) automatically perform all
required calculations in an umbrella review (including but not limited to
meta-analyses), (ii) stratify evidence according to various classification
criteria, and (iii) generate a visual representation of the results. Note
that if you are not familiar with R, the core features of this package are
available from a web browser (<https://www.metaumbrella.org/>).

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
