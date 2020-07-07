%global packname  tmaptools
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          2%{?dist}
Summary:          Thematic Map Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.9.2
BuildRequires:    R-CRAN-units >= 0.6.1
BuildRequires:    R-CRAN-stars >= 0.4.1
BuildRequires:    R-CRAN-lwgeom >= 0.1.4
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dichromat 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-sf >= 0.9.2
Requires:         R-CRAN-units >= 0.6.1
Requires:         R-CRAN-stars >= 0.4.1
Requires:         R-CRAN-lwgeom >= 0.1.4
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 
Requires:         R-stats 
Requires:         R-CRAN-dichromat 
Requires:         R-CRAN-XML 

%description
Set of tools for reading and processing spatial data. The aim is to supply
the workflow to create thematic maps. This package also facilitates
'tmap', the package for visualizing thematic maps.

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
