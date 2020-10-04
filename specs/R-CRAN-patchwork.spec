%global packname  patchwork
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}%{?buildtag}
Summary:          The Composer of Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gtable 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 

%description
The 'ggplot2' package provides a strong API for sequentially building up a
plot, but does not concern itself with composition of multiple plots.
'patchwork' is a package that expands the API to allow for arbitrarily
complex composition of plots by, among others, providing mathematical
operators for combining multiple plots. Other packages that try to address
this need (but with a different approach) are 'gridExtra' and 'cowplot'.

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

%files
%{rlibdir}/%{packname}
