%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tm.plugin.dc
%global packver   0.2-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Text Mining Distributed Corpus Plug-in

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.7
BuildRequires:    R-CRAN-DSL >= 0.1.7
BuildRequires:    R-CRAN-slam >= 0.1.22
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-utils 
Requires:         R-CRAN-tm >= 0.7
Requires:         R-CRAN-DSL >= 0.1.7
Requires:         R-CRAN-slam >= 0.1.22
Requires:         R-CRAN-NLP 
Requires:         R-utils 

%description
A plug-in for the text mining framework tm to support text mining in a
distributed way. The package provides a convenient interface for handling
distributed corpus objects based on distributed list objects.

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
