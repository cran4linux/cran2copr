%global packname  rmonad
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          2%{?dist}
Summary:          A Monadic Pipeline System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-digest 

%description
A monadic solution to pipeline analysis. All operations -- and the errors,
warnings and messages they emit -- are merged into a directed graph. Infix
binary operators mediate when values are stored, how exceptions are
handled, and where pipelines branch and merge. The resulting structure may
be queried for debugging or report generation. 'rmonad' complements,
rather than competes with, non-monadic pipeline packages like 'magrittr'
or 'pipeR'. This work is funded by the NSF (award number 1546858).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/JOSS
%{rlibdir}/%{packname}/INDEX
