%global __brp_check_rpaths %{nil}
%global packname  EnsemblePenReg
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Extensible Classes and Methods for Penalized-Regression-BasedIntegration of Base Learners

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EnsembleBase 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-EnsembleBase 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-glmnet 

%description
Extending the base classes and methods of EnsembleBase package for
Penalized-Regression-based (Ridge and Lasso) integration of base learners.
Default implementation uses cross-validation error to choose the optimal
lambda (shrinkage parameter) for the final predictor. The package takes
advantage of the file method provided in EnsembleBase package for writing
estimation objects to disk in order to circumvent RAM bottleneck. Special
save and load methods are provided to allow estimation objects to be saved
to permanent files on disk, and to be loaded again into temporary files in
a later R session. Users and developers can extend the package by
extending the generic methods and classes provided in EnsembleBase package
as well as this package.

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
