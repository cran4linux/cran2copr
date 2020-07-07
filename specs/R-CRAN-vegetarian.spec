%global packname  vegetarian
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Jost Diversity Measures for Community Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
This package computes diversity for community data sets using the methods
outlined by Jost (2006, 2007). While there are differing opinions on the
ideal way to calculate diversity (e.g. Magurran 2004), this method offers
the advantage of providing diversity numbers equivalents, independent
alpha and beta diversities, and the ability to incorporate 'order' (q) as
a continuous measure of the importance of rare species in the metrics. The
functions provided in this package largely correspond with the equations
offered by Jost in the cited papers. The package computes alpha
diversities, beta diversities, gamma diversities, and similarity indices.
Confidence intervals for diversity measures are calculated using a
bootstrap method described by Chao et al. (2008).  For datasets with many
samples (sites, plots), sim.table creates tables of all pairwise
comparisons possible, and for grouped samples sim.groups calculates
pairwise combinations of within- and between-group comparisons.

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
%{rlibdir}/%{packname}/INDEX
