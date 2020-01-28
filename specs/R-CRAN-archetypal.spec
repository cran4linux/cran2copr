%global packname  archetypal
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Finds the Archetypal Analysis of a Data Frame

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-inflection 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-Matrix 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-inflection 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-lpSolve 
Requires:         R-methods 
Requires:         R-CRAN-plot3D 

%description
Performs archetypal analysis by using Principal Convex Hull Analysis
(PCHA) under a full control of all algorithmic parameters. It contains a
set of functions for determining the initial solution, the optimal
algorithmic parameters and the optimal number of archetypes. Post run
tools are also available for the assessment of the derived solution.
Morup, M., Hansen, LK (2012) <doi:10.1016/j.neucom.2011.06.033>. Hochbaum,
DS, Shmoys, DB (1985) <doi:10.1287/moor.10.2.180>. Eddy, WF (1977)
<doi:10.1145/355759.355768>. Barber, CB, Dobkin, DP, Huhdanpaa, HT (1996)
<doi:10.1145/235815.235821>. Christopoulos, DT (2016)
<doi:10.2139/ssrn.3043076>. Christopoulos, DT (2015)
<doi:10.1016/j.jastp.2015.03.009> . Falk, A. et al. (2018),
<doi:10.1093/qje/qjy013> .

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
