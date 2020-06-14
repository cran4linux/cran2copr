%global packname  SparseBiplots
%global packver   3.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.0
Release:          2%{?dist}
Summary:          'HJ Biplot' using Different Ways of Penalization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sparsepca 
Requires:         R-CRAN-sparsepca 

%description
Contains a set of functions that allow to represent multivariate on a
subspace of low dimension, in such a way that most of the variability of
the information is captured. This representation is carried out through
the 'HJ Biplot' methodology. A first method performs the 'HJ Biplot'.Then,
the package implements three new techniques and constructs in each case
the 'HJ Biplot', adapting restrictions to contract and / or produce zero
charges in the main components, using three methods of regularization:
Ridge, LASSO and Elastic Net.

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
