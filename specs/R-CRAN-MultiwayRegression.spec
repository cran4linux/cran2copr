%global __brp_check_rpaths %{nil}
%global packname  MultiwayRegression
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Perform Tensor-on-Tensor Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Functions to predict one multi-way array (i.e., a tensor) from another
multi-way array, using a low-rank CANDECOMP/PARAFAC (CP) factorization and
a ridge (L_2) penalty [Lock, EF (2018)
<doi:10.1080/10618600.2017.1401544>].  Also includes functions to sample
from the Bayesian posterior of a tensor-on-tensor model.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
