%global __brp_check_rpaths %{nil}
%global packname  doSNOW
%global packver   1.0.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.19
Release:          1%{?dist}%{?buildtag}
Summary:          Foreach Parallel Adaptor for the 'snow' Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-iterators >= 1.0.0
BuildRequires:    R-CRAN-snow >= 0.3.0
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-iterators >= 1.0.0
Requires:         R-CRAN-snow >= 0.3.0
Requires:         R-utils 

%description
Provides a parallel backend for the %%dopar%% function using the snow
package of Tierney, Rossini, Li, and Sevcikova.

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
