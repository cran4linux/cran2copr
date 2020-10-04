%global packname  directlabels
%global packver   2020.6.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.6.17
Release:          2%{?dist}%{?buildtag}
Summary:          Direct Labels for Multicolor Plots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-grid 
Requires:         R-CRAN-quadprog 

%description
An extensible framework for automatically placing direct labels onto
multicolor 'lattice' or 'ggplot2' plots. Label positions are described
using Positioning Methods which can be re-used across several different
plots. There are heuristics for examining "trellis" and "ggplot" objects
and inferring an appropriate Positioning Method.

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
