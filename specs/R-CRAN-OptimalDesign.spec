%global packname  OptimalDesign
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          A Toolbox for Computing Efficient Designs of Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-rgl 
Requires:         R-stats 
Requires:         R-utils 

%description
Algorithms for D-, A-, I-, and c-optimal designs. Some of the functions in
this package require the 'gurobi' software and its accompanying R package.
For their installation, please follow the instructions at
<https://www.gurobi.com> and the file gurobi_inst.txt, respectively.

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
%doc %{rlibdir}/%{packname}/gurobi_inst.txt
%{rlibdir}/%{packname}/INDEX
