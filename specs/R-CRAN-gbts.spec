%global __brp_check_rpaths %{nil}
%global packname  gbts
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Hyperparameter Search for Gradient Boosted Trees

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-earth 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-earth 

%description
An implementation of hyperparameter optimization for Gradient Boosted
Trees on binary classification and regression problems. The current
version provides two optimization methods: Bayesian optimization and
random search. Instead of giving the single best model, the final output
is an ensemble of Gradient Boosted Trees constructed via the method of
ensemble selection.

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
