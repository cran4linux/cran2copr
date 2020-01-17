%global packname  tensorregress
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Generalized Tensor Regression with Covariates on Multiple Modes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-MASS 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-speedglm 
Requires:         R-MASS 

%description
Implement the generalized tensor regression in Xu, Hu and Wang (2019)
<arXiv:1910.09499>. Solve tensor-response regression given covariates on
multiple modes with alternating updating algorithm.

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
