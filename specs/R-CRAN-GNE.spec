%global packname  GNE
%global packver   0.99-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.2
Release:          1%{?dist}
Summary:          Computation of Generalized Nash Equilibria

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-SQUAREM 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-SQUAREM 

%description
Provide functions to compute standard and generalized Nash Equilibria.
Optimization methods are available nonsmooth reformulation, fixed-point
formulation, minimization problem and constrained-equation reformulation.
See e.g. Kanzow and Facchinei (2010), <doi:10.1007/s10479-009-0653-x>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TODOlist.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
