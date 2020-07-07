%global packname  fit.models
%global packver   0.63
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.63
Release:          2%{?dist}
Summary:          Compare Fitted Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
Requires:         R-lattice 
Requires:         R-stats 

%description
The fit.models function and its associated methods (coefficients, print,
summary, plot, etc.) were originally provided in the robust package to
compare robustly and classically fitted model objects. See chapters 2, 3,
and 5 in Insightful (2002) 'Robust Library User's Guide'
<http://robust.r-forge.r-project.org/Robust.pdf>). The aim of the
fit.models package is to separate this fitted model object comparison
functionality from the robust package and to extend it to support fitting
methods (e.g., classical, robust, Bayesian, regularized, etc.) more
generally.

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
