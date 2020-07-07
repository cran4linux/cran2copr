%global packname  xLLiM
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}
Summary:          High Dimensional Locally-Linear Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-capushe 
Requires:         R-MASS 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-corpcor 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-capushe 

%description
Provides a tool for non linear mapping (non linear regression) using a
mixture of regression model and an inverse regression strategy. The
methods include the GLLiM model (see Deleforge et al (2015)
<DOI:10.1007/s11222-014-9461-5>) based on Gaussian mixtures and a robust
version of GLLiM, named SLLiM (see Perthame et al (2016)
<https://hal.archives-ouvertes.fr/hal-01347455>) based on a mixture of
Generalized Student distributions. The methods also include BLLiM (see
Devijver et al (2017) <https://arxiv.org/abs/1701.07899>) which is an
extension of GLLiM with a sparse block diagonal structure for large
covariance matrices (particularly interesting for transcriptomic data).

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
%{rlibdir}/%{packname}/INDEX
