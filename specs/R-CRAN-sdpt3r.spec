%global __brp_check_rpaths %{nil}
%global packname  sdpt3r
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Semi-Definite Quadratic Linear Programming Solver

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-stats 

%description
Solves the general Semi-Definite Linear Programming formulation using an R
implementation of SDPT3 (K.C. Toh, M.J. Todd, and R.H. Tutuncu (1999)
<doi:10.1080/10556789908805762>). This includes problems such as the
nearest correlation matrix problem (Higham (2002)
<doi:10.1093/imanum/22.3.329>), D-optimal experimental design (Smith
(1918) <doi:10.2307/2331929>), Distance Weighted Discrimination (Marron
and Todd (2012) <doi:10.1198/016214507000001120>), as well as graph theory
problems including the maximum cut problem. Technical details surrounding
SDPT3 can be found in R.H Tutuncu, K.C. Toh, and M.J. Todd (2003)
<doi:10.1007/s10107-002-0347-5>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
