%global packname  multiplex
%global packver   2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9
Release:          1%{?dist}
Summary:          Algebraic Tools for the Analysis of Multiple Social Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Algebraic procedures for the analysis of multiple social networks are
delivered with this package. Among other things, it makes possible to
create and manipulate multivariate network data with different formats,
and there are effective ways available to treat multiple networks with
routines that combine algebraic systems like the partially ordered
semigroup or the semiring structure together with the relational bundles
occurring in different types of multivariate network data sets. It also
provides an algebraic approach for two-mode networks through Galois
derivations between families of the pairs of subsets in the two domains.

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
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
