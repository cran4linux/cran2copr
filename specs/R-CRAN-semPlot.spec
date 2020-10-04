%global packname  semPlot
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          2%{?dist}%{?buildtag}
Summary:          Path Diagrams and Visual Analysis of Various SEM Packages'Output

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sem >= 3.1.0
BuildRequires:    R-CRAN-qgraph >= 1.2.4
BuildRequires:    R-CRAN-igraph >= 0.6.3
BuildRequires:    R-CRAN-lavaan >= 0.5.11
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-lisrelToR 
BuildRequires:    R-CRAN-rockchalk 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-CRAN-regsem 
Requires:         R-CRAN-sem >= 3.1.0
Requires:         R-CRAN-qgraph >= 1.2.4
Requires:         R-CRAN-igraph >= 0.6.3
Requires:         R-CRAN-lavaan >= 0.5.11
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-lisrelToR 
Requires:         R-CRAN-rockchalk 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-corpcor 
Requires:         R-methods 
Requires:         R-CRAN-OpenMx 
Requires:         R-CRAN-regsem 

%description
Path diagrams and visual analysis of various SEM packages' output.

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
