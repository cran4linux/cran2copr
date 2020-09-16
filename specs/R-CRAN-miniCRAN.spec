%global packname  miniCRAN
%global packver   0.2.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.14
Release:          1%{?dist}%{?buildtag}
Summary:          Create a Mini Version of CRAN Containing Only Selected Packages

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-igraph 

%description
Makes it possible to create an internally consistent repository consisting
of selected packages from CRAN-like repositories. The user specifies a set
of desired packages, and 'miniCRAN' recursively reads the dependency tree
for these packages, then downloads only this subset. The user can then
install packages from this repository directly, rather than from CRAN.
This is useful in production settings, e.g. server behind a firewall, or
remote locations with slow (or zero) Internet access.

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
