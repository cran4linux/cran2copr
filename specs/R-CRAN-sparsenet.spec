%global packname  sparsenet
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Fit Sparse Linear Regression Models via Nonconvex Optimization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.0.6
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-methods 
Requires:         R-Matrix >= 1.0.6
Requires:         R-CRAN-shape 
Requires:         R-methods 

%description
Efficient procedure for fitting regularization paths between L1 and L0,
using the MC+ penalty of Zhang, C.H. (2010)<doi:10.1214/09-AOS729>.
Implements the methodology described in Mazumder, Friedman and Hastie
(2011) <DOI: 10.1198/jasa.2011.tm09738>. Sparsenet computes the
regularization surface over both the family parameter and the tuning
parameter by coordinate descent.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/mortran
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
