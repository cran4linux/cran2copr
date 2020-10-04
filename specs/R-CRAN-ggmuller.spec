%global packname  ggmuller
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          3%{?dist}%{?buildtag}
Summary:          Create Muller Plots of Evolutionary Dynamics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ape 

%description
Create plots that combine a phylogeny and frequency dynamics. Phylogenetic
input can be a generic adjacency matrix or a tree of class "phylo".
Inspired by similar plots in publications of the labs of RE Lenski and JE
Barrick. Named for HJ Muller (who popularised such plots) and H Wickham
(whose code this package exploits).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
