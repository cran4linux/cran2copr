%global packname  eiwild
%global packver   0.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7
Release:          1%{?dist}
Summary:          Ecological Inference with individual and aggregate data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-lattice 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-coda 
Requires:         R-lattice 

%description
This package allows to use the hybrid Multinomial-Dirichlet-Model of
Ecological Inference for estimating inner Cells of RxC-Tables. This was
already implemented in the eiPack-package. eiwild-package now has the
possibility to use individual level data to support the aggregate level
data and using different Hyperpriori-Distributions.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
