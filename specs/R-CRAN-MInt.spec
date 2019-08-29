%global packname  MInt
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Learn Direct Interaction Networks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.35
BuildRequires:    R-CRAN-glasso >= 1.8
BuildRequires:    R-CRAN-testthat >= 0.9.1
BuildRequires:    R-CRAN-trust >= 0.1.6
Requires:         R-MASS >= 7.3.35
Requires:         R-CRAN-glasso >= 1.8
Requires:         R-CRAN-testthat >= 0.9.1
Requires:         R-CRAN-trust >= 0.1.6

%description
Learns direct microbe-microbe interaction networks using a Poisson
multivariate-normal hierarchical model with an L1 penalized precision
matrix. Optimization is carried out using an iterative conditional modes
algorithm.

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
%{rlibdir}/%{packname}/INDEX
