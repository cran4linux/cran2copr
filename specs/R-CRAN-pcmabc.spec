%global packname  pcmabc
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Approximate Bayesian Computations for Phylogenetic ComparativeMethods

License:          GPL (>= 2) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.1
Requires:         R-core >= 2.9.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvSLOUCH 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TreeSim 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yuima 
Requires:         R-CRAN-ape >= 3.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mvSLOUCH 
Requires:         R-CRAN-phangorn 
Requires:         R-stats 
Requires:         R-CRAN-TreeSim 
Requires:         R-utils 
Requires:         R-CRAN-yuima 

%description
Fits by ABC, the parameters of a stochastic process modelling the
phylogeny and evolution of a suite of traits following the tree. The user
may define an arbitrary Markov process for the trait and phylogeny.
Importantly, trait-dependent speciation models are handled and fitted to
data. See K. Bartoszek, P. Lio' (2019) <10.5506/APhysPolBSupp.12.25>. The
suggested geiger package can be obtained from CRAN's archive
<https://cran.r-project.org/src/contrib/Archive/geiger/>, suggested to
take latest version. Otherwise its required code is present in the pcmabc
package. The suggested distory package can be obtained from CRAN's archive
<https://cran.r-project.org/src/contrib/Archive/distory/>, suggested to
take latest version. Both distory and geiger are orphaned at the moment.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/GPL-2
%doc %{rlibdir}/%{packname}/GPL-3
%{rlibdir}/%{packname}/INDEX
