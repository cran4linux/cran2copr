%global __brp_check_rpaths %{nil}
%global packname  iva
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Instrumental Variable Analysis in Case-Control AssociationStudies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-Formula 

%description
Mendelian randomization (MR) analysis is a special case of instrumental
variable analysis with genetic instruments. It is used to estimate the
unconfounded causal effect of an exposure. This package implements
estimating and testing methods in Zhang et al. (2019) for MR analysis in
case-control studies. It (1) estimates the causal effect of a quantitative
exposure by the quasi empirical likelihood approach; (2) uses Lagrange
multiplier test for testing the presence of causal; (3) provides a test
for the presence of confounder.

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
%{rlibdir}/%{packname}/INDEX
