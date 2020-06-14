%global packname  modQR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Multiple-Output Directional Quantile Regression

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve >= 5.6.1
BuildRequires:    R-CRAN-geometry >= 0.3.1
Requires:         R-CRAN-lpSolve >= 5.6.1
Requires:         R-CRAN-geometry >= 0.3.1

%description
Contains basic tools for performing multiple-output quantile regression
and computing regression quantile contours by means of directional
regression quantiles. In the location case, one can thus obtain halfspace
depth contours in two to six dimensions. Hallin, M., Paindaveine, D. and
Siman, M. (2010) Multivariate quantiles and multiple-output regression
quantiles: from L1 optimization to halfspace depth. Annals of Statistics
38, 635-669 For more references about the method, see Help pages.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
