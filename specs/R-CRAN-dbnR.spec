%global packname  dbnR
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}
Summary:          Dynamic Bayesian Network Learning and Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bnlearn >= 4.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-bnlearn >= 4.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Learning and inference over dynamic Bayesian networks of arbitrary
Markovian order.  Extends some of the functionality offered by the
'bnlearn' package to learn the networks from data and perform exact
inference. It offers a modification of Trabelsi (2013)
<doi:10.1007/978-3-642-41398-8_34> dynamic max-min hill climbing algorithm
for structure learning and the possibility to perform forecasts of
arbitrary length. A tool for visualizing the structure of the net is also
provided via the 'visNetwork' package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
