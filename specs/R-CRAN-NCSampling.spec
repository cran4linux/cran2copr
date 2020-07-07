%global packname  NCSampling
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Nearest Centroid (NC) Sampling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-CRAN-yaImpute 
Requires:         R-lattice 
Requires:         R-CRAN-randomForest 

%description
Provides functionality for performing Nearest Centroid (NC) Sampling. The
NC sampling procedure was developed for forestry applications and selects
plots for ground measurement so as to maximize the efficiency of
imputation estimates. It uses multiple auxiliary variables and
multivariate clustering to search for an optimal sample. Further details
are given in Melville G. & Stone C. (2016)
<doi:10.1080/00049158.2016.1218265>.

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
