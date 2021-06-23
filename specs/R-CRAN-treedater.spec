%global __brp_check_rpaths %{nil}
%global packname  treedater
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Molecular Clock Dating of Phylogenetic Trees with RateVariation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-limSolve >= 1.5.5.0
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-limSolve >= 1.5.5.0

%description
Functions for estimating times of common ancestry and molecular clock
rates of evolution using a variety of evolutionary models, parametric and
nonparametric bootstrap confidence intervals, methods for detecting
outlier lineages, root-to-tip regression, and a statistical test for
selecting molecular clock models. The methods are described in Volz, E.M.
and S.D.W. Frost (2017) <doi:10.1093/ve/vex025>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/tdcl
%{rlibdir}/%{packname}/INDEX
