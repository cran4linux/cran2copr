%global packname  GE
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          General Equilibrium Modeling

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CGE 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-CRAN-CGE 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-DiagrammeR 

%description
Some tools for developing general equilibrium models and some general
equilibrium models. These models can be used for teaching economic theory
and are built by the methods of new structural economics (see
<https://www.nse.pku.edu.cn/> and LI Wu, 2019, ISBN: 9787521804225,
General Equilibrium and Structural Dynamics: Perspectives of New
Structural Economics. Beijing: Economic Science Press). The model form and
mathematical methods can be traced back to von Neumann, J. (1945, A Model
of General Economic Equilibrium. The Review of Economic Studies, 13. pp.
1-9) and Kemeny, J. G., O. Morgenstern and G. L. Thompson (1956, A
Generalization of the von Neumann Model of an Expanding Economy,
Econometrica, 24, pp. 115-135) et al. By the way, J. G. Kemeny is a
co-inventor of the computer language BASIC.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
