%global packname  accSDA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Accelerated Sparse Discriminant Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-grid >= 3.2.2
BuildRequires:    R-CRAN-ggthemes >= 3.2.0
BuildRequires:    R-CRAN-gridExtra >= 2.2.1
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-rARPACK >= 0.10.0
BuildRequires:    R-CRAN-sparseLDA >= 0.1.7
Requires:         R-MASS >= 7.3.45
Requires:         R-grid >= 3.2.2
Requires:         R-CRAN-ggthemes >= 3.2.0
Requires:         R-CRAN-gridExtra >= 2.2.1
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-rARPACK >= 0.10.0
Requires:         R-CRAN-sparseLDA >= 0.1.7

%description
Implementation of sparse linear discriminant analysis, which is a
supervised classification method for multiple classes. Various novel
optimization approaches to this problem are implemented including
alternating direction method of multipliers (ADMM), proximal gradient (PG)
and accelerated proximal gradient (APG) (See Atkins et al.
<arXiv:1705.07194>). Functions for performing cross validation are also
supplied along with basic prediction and plotting functions. Sparse zero
variance discriminant analysis (SZVD) is also included in the package (See
Ames and Hong, <arXiv:1401.5492>). See the github wiki for a more extended
description.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
