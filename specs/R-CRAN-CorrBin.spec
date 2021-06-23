%global __brp_check_rpaths %{nil}
%global packname  CorrBin
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametrics with Clustered Binary and Multinomial Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-boot 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-mvtnorm 

%description
Implements non-parametric analyses for clustered binary and multinomial
data. The elements of the cluster are assumed exchangeable, and identical
joint distribution (also known as marginal compatibility, or
reproducibility) is assumed for clusters of different sizes. A trend test
based on stochastic ordering is implemented.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
