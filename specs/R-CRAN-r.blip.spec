%global packname  r.blip
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Bayesian Network Learning Improved Project

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn >= 4.0
BuildRequires:    R-foreign 
Requires:         R-CRAN-bnlearn >= 4.0
Requires:         R-foreign 

%description
Allows the user to learn Bayesian networks from datasets containing
thousands of variables. It focuses on score-based learning, mainly the
'BIC' and the 'BDeu' score functions. It provides state-of-the-art
algorithms for the following tasks: (1) parent set identification - Mauro
Scanagatta (2015)
<http://papers.nips.cc/paper/5803-learning-bayesian-networks-with-thousands-of-variables>;
(2) general structure optimization - Mauro Scanagatta (2018)
<doi:10.1007/s10994-018-5701-9>, Mauro Scanagatta (2018)
<http://proceedings.mlr.press/v73/scanagatta17a.html>; (3) bounded
treewidth structure optimization - Mauro Scanagatta (2016)
<http://papers.nips.cc/paper/6232-learning-treewidth-bounded-bayesian-networks-with-thousands-of-variables>;
(4) structure learning on incomplete data sets - Mauro Scanagatta (2018)
<doi:10.1016/j.ijar.2018.02.004>. Distributed under the LGPL-3 by IDSIA.

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
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
