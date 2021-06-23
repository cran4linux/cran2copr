%global __brp_check_rpaths %{nil}
%global packname  silicate
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Common Forms for Complex Hierarchical and Relational Data Structures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gibble >= 0.4.0
BuildRequires:    R-CRAN-crsmeta >= 0.3.0
BuildRequires:    R-CRAN-unjoin >= 0.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-decido 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-gridBase 
Requires:         R-CRAN-gibble >= 0.4.0
Requires:         R-CRAN-crsmeta >= 0.3.0
Requires:         R-CRAN-unjoin >= 0.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-decido 
Requires:         R-CRAN-tibble 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-gridBase 

%description
Generate common data forms for complex data suitable for conversions and
transmission by decomposition as paths or primitives. Paths are
sequentially-linked records, primitives are basic atomic elements and both
can model many forms and be grouped into hierarchical structures.  The
universal models 'SC0' (structural) and 'SC' (labelled, relational) are
composed of edges and can represent any hierarchical form. Specialist
models 'PATH', 'ARC' and 'TRI' provide the most common intermediate forms
used for converting from one form to another. The methods are inspired by
the simplicial complex <https://en.wikipedia.org/wiki/Simplicial_complex>
and provide intermediate forms that relate spatial data structures to this
mathematical construct.

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
