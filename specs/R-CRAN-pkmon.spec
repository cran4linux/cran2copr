%global packname  pkmon
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Least-Squares Estimator under k-Monotony Constraint for DiscreteFunctions

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
We implement two least-squares estimators under k-monotony constraint
using a method based on the Support Reduction Algorithm from Groeneboom et
al (2008) <DOI:10.1111/j.1467-9469.2007.00588.x>. The first one is a
projection estimator on the set of k-monotone discrete functions. The
second one is a projection on the set of k-monotone discrete
probabilities. This package provides functions to generate samples from
the spline basis from Lefevre and Loisel (2013)
<DOI:10.1239/jap/1378401239>, and from mixtures of splines.

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
