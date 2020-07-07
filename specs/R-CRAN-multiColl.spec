%global packname  multiColl
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Collinearity Detection in a Multiple Linear Regression Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The detection of worrying approximate collinearity in a multiple linear
regression model is a problem addressed in all existing statistical
packages. However, we have detected deficits regarding to the incorrect
treatment of qualitative independent variables and the role of the
intercept of the model. The objective of this package is to correct these
deficits. In this package will be available detection and treatment
techniques traditionally used as the recently developed. D.A. Belsley
(1982) <doi:10.1016/0304-4076(82)90020-3>. D. A. Belsley (1991, ISBN:
978-0471528890). C. Garcia, R. Salmeron and C.B. Garcia (2019)
<doi:10.1080/00949655.2018.1543423>. R. Salmeron, C.B. Garcia and J.
Garcia (2018) <doi:10.1080/00949655.2018.1463376>. G.W. Stewart (1987)
<doi:10.1214/ss/1177013444>.

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
