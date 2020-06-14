%global packname  MLGL
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          2%{?dist}
Summary:          Multi-Layer Group-Lasso

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gglasso 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-parallelDist 
Requires:         R-CRAN-gglasso 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-parallelDist 

%description
It implements a new procedure of variable selection in the context of
redundancy between explanatory variables, which holds true with high
dimensional data (Grimonprez et al. (2018)
<https://hal.inria.fr/hal-01857242>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
