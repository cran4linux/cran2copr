%global __brp_check_rpaths %{nil}
%global packname  rmumps
%global packver   5.2.1-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2.1.12
Release:          3%{?dist}%{?buildtag}
Summary:          Wrapper for MUMPS Library

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 

%description
Some basic features of 'MUMPS' (Multifrontal Massively Parallel sparse
direct Solver) are wrapped in a class whose methods can be used for
sequentially solving a sparse linear system (symmetric or not) with one or
many right hand sides (dense or sparse). There is a possibility to do
separately symbolic analysis, LU (or LDL^t) factorization and system
solving. Third part ordering libraries are included and can be used:
'PORD', 'METIS', 'SCOTCH'. 'MUMPS' method was first described in Amestoy
et al. (2001) <doi:10.1137/S0895479899358194> and Amestoy et al. (2006)
<doi:10.1016/j.parco.2005.07.004>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
