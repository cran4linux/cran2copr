%global packname  LPmerge
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          2%{?dist}
Summary:          Merging Linkage Maps by Linear Programming

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-Rglpk 
Requires:         R-Matrix 

%description
Creates a consensus genetic map by merging linkage maps from different
populations.  The software uses linear programming (LP) to efficiently
minimize the mean absolute error between the consensus map and the linkage
maps.  This minimization is performed subject to linear inequality
constraints that ensure the ordering of the markers in the linkage maps is
preserved.  When marker order is inconsistent between linkage maps, a
minimum set of ordinal constraints is deleted to resolve the conflicts.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
