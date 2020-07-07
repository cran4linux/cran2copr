%global packname  lavaanPlot
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          2%{?dist}
Summary:          Path Diagrams for Lavaan Models via DiagrammeR

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-stringr 

%description
Plots path diagrams from models in lavaan using the plotting functionality
from the DiagrammeR package. DiagrammeR provides nice path diagrams via
Graphviz, and these functions make it easy to generate these diagrams from
a lavaan path model without having to write the DOT language graph
specification.

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
