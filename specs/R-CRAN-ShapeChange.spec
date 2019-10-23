%global packname  ShapeChange
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Change-Point Estimation using Shape-Restricted Splines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog >= 1.5.5
BuildRequires:    R-CRAN-coneproj >= 1.11
Requires:         R-CRAN-quadprog >= 1.5.5
Requires:         R-CRAN-coneproj >= 1.11

%description
In a scatterplot where the response variable is Gaussian, Poisson or
binomial, we consider the case in which the mean function is smooth with a
change-point, which is a mode, an inflection point or a jump point. The
main routine estimates the mean curve and the change-point as well using
shape-restricted B-splines. An optional subroutine delivering a bootstrap
confidence interval for the change-point is incorporated in the main
routine.

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
%{rlibdir}/%{packname}/INDEX
