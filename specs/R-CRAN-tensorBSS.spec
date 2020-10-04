%global packname  tensorBSS
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          3%{?dist}%{?buildtag}
Summary:          Blind Source Separation Methods for Tensor-Valued Observations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-JADE 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-tsBSS 
BuildRequires:    R-CRAN-ICtest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-JADE 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-tsBSS 
Requires:         R-CRAN-ICtest 
Requires:         R-CRAN-ggplot2 

%description
Contains several utility functions for manipulating tensor-valued data
(centering, multiplication from a single mode etc.) and the
implementations of the following blind source separation methods for
tensor-valued data: 'tPCA', 'tFOBI', 'tJADE', k-tJADE', 'tgFOBI',
'tgJADE', 'tSOBI', 'tNSS.SD', 'tNSS.JD', 'tNSS.TD.JD', 'tPP' and
'tTUCKER'.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
