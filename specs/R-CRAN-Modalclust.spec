%global packname  Modalclust
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          2%{?dist}
Summary:          Hierarchical Modal Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-class 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-zoo 
Requires:         R-class 

%description
Performs Modal Clustering (MAC) including Hierarchical Modal Clustering
(HMAC) along with their parallel implementation (PHMAC) over several
processors.  These model-based non-parametric clustering techniques can
extract clusters in very high dimensions with arbitrary density shapes. By
default clustering is performed over several resolutions and the results
are summarised as a hierarchical tree. Associated plot functions are also
provided. There is a package vignette that provides many examples. This
version adheres to CRAN policy of not spanning more than two child
processes by default.

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
