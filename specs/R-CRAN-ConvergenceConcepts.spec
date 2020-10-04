%global packname  ConvergenceConcepts
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Seeing Convergence Concepts in Action

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-lattice 
BuildRequires:    R-grDevices 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-lattice 
Requires:         R-grDevices 

%description
This is a pedagogical package, designed to help students understanding
convergence of random variables. It provides a way to investigate
interactively various modes of convergence (in probability, almost surely,
in law and in mean) of a sequence of i.i.d. random variables.
Visualisation of simulated sample paths is possible through interactive
plots. The approach is illustrated by examples and exercises through the
function 'investigate', as described in Lafaye de Micheaux and Liquet
(2009) <doi:10.1198/tas.2009.0032>. The user can study his/her own
sequences of random variables.

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
%doc %{rlibdir}/%{packname}/HISTORY
%{rlibdir}/%{packname}/INDEX
