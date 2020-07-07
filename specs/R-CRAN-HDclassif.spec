%global packname  HDclassif
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}
Summary:          High Dimensional Supervised Classification and Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rARPACK 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-rARPACK 

%description
Discriminant analysis and data clustering methods for high dimensional
data, based on the assumption that high-dimensional data live in different
subspaces with low dimensionality proposing a new parametrization of the
Gaussian mixture model which combines the ideas of dimension reduction and
constraints on the model.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
