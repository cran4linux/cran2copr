%global __brp_check_rpaths %{nil}
%global packname  BioMark
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          3%{?dist}%{?buildtag}
Summary:          Find Biomarkers in Two-Class Discrimination Problems

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-st >= 1.1.6
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-MASS 
Requires:         R-CRAN-st >= 1.1.6
Requires:         R-CRAN-pls 
Requires:         R-CRAN-glmnet 
Requires:         R-MASS 

%description
Variable selection methods are provided for several classification
methods: the lasso/elastic net, PCLDA, PLSDA, and several t-tests. Two
approaches for selecting cutoffs can be used, one based on the stability
of model coefficients under perturbation, and the other on higher
criticism.

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
