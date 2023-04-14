%global __brp_check_rpaths %{nil}
%global packname  fastclime
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Fast Solver for Parameterized LP Problems, Constrained L1Minimization Approach to Sparse Precision Matrix Estimation andDantzig Selector

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-lattice 
Requires:         R-CRAN-igraph 
Requires:         R-MASS 
Requires:         R-Matrix 

%description
Provides a method of recovering the precision matrix efficiently and
solving for the dantzig selector by applying the parametric simplex
method.  The computation is based on a linear optimization solver. It also
contains a generic LP solver and a parameterized LP solver using
parametric simplex method.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
