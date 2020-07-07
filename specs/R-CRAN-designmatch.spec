%global packname  designmatch
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Matched Samples that are Balanced and Representative by Design

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-Rglpk 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-Rglpk 

%description
Includes functions for the construction of matched samples that are
balanced and representative by design.  Among others, these functions can
be used for matching in observational studies with treated and control
units, with cases and controls, in related settings with instrumental
variables, and in discontinuity designs.  Also, they can be used for the
design of randomized experiments, for example, for matching before
randomization.  By default, 'designmatch' uses the 'GLPK' optimization
solver, but its performance is greatly enhanced by the 'Gurobi'
optimization solver and its associated R interface.  For their
installation, please follow the instructions at
<http://user.gurobi.com/download/gurobi-optimizer> and
<http://www.gurobi.com/documentation/7.0/refman/r_api_overview.html>.  We
have also included directions in the gurobi_installation file in the inst
folder.

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
%doc %{rlibdir}/%{packname}/gurobi_installation.txt
%doc %{rlibdir}/%{packname}/symphony_installation.txt
%{rlibdir}/%{packname}/INDEX
