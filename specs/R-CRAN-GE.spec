%global packname  GE
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}
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
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-CGE 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-graphics 
Requires:         R-CRAN-stringr 

%description
Some tools for developing general equilibrium models and some general
equilibrium models. These models can be used for teaching economic theory
and are built by the methods of new structural economics (see
<https://www.nse.pku.edu.cn/> and LI Wu, 2019, General Equilibrium and
Structural Dynamics: Perspectives of New Structural Economics. Beijing:
Economic Science Press).

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
