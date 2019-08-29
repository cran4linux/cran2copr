%global packname  lassoshooting
%global packver   0.1.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5.1
Release:          1%{?dist}
Summary:          L1 regularized regression (Lasso) solver using the CyclicCoordinate Descent algorithm aka Lasso Shooting

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0

%description
L1 regularized regression (Lasso) solver using the Cyclic Coordinate
Descent algorithm aka Lasso Shooting is fast. This implementation can
choose which coefficients to penalize. It support coefficient-specific
penalities and it can take X'X and X'y instead of X and y.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
