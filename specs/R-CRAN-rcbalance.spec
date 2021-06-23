%global __brp_check_rpaths %{nil}
%global packname  rcbalance
%global packver   1.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.5
Release:          3%{?dist}%{?buildtag}
Summary:          Large, Sparse Optimal Matching with Refined Covariate Balance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plyr 
Requires:         R-MASS 
Requires:         R-CRAN-plyr 

%description
Tools for large, sparse optimal matching of treated units and control
units in observational studies.  Provisions are made for refined covariate
balance constraints, which include fine and near-fine balance as special
cases.  Matches are optimal in the sense that they are computed as
solutions to network optimization problems rather than greedy algorithms.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
