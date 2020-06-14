%global packname  causalMGM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Causal Learning of Mixed Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-rJava 

%description
Allows users to learn undirected and directed (causal) graphs over mixed
data types (i.e., continuous and discrete variables). To learn a directed
graph over mixed data, it first calculates the undirected graph (Sedgewick
et al, 2016) and then it uses local search strategies to prune-and-orient
this graph (Sedgewick et al, 2017). AJ Sedgewick, I Shi, RM Donovan, PV
Benos (2016) <doi:10.1186/s12859-016-1039-0>. AJ Sedgewick, JD Ramsey, P
Spirtes, C Glymour, PV Benos (2017) <arXiv:1704.02621>.

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
%doc %{rlibdir}/%{packname}/txt
%{rlibdir}/%{packname}/INDEX
