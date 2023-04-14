%global __brp_check_rpaths %{nil}
%global packname  BayesLCA
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Latent Class Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-fields 
Requires:         R-nlme 
Requires:         R-CRAN-MCMCpack 

%description
Bayesian Latent Class Analysis using several different methods.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
