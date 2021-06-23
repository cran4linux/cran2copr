%global __brp_check_rpaths %{nil}
%global packname  paleopop
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pattern-Oriented Modeling Framework for Coupled Niche-Population Paleo-Climatic Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-trend >= 1.1.4
BuildRequires:    R-CRAN-poems >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-trend >= 1.1.4
Requires:         R-CRAN-poems >= 1.0.0
Requires:         R-CRAN-sf >= 0.9

%description
This extension of the poems pattern-oriented modeling (POM) framework
provides a collection of modules and functions customized for
paleontological time-scales, and optimized for single-generation
transitions and large populations, across multiple generations.

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
