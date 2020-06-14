%global packname  kernelFactory
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Kernel Factory: An Ensemble of Kernel Machines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-AUC 
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-AUC 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-kernlab 
Requires:         R-stats 

%description
Binary classification based on an ensemble of kernel machines ("Ballings,
M. and Van den Poel, D. (2013), Kernel Factory: An Ensemble of Kernel
Machines. Expert Systems With Applications, 40(8), 2904-2913"). Kernel
factory is an ensemble method where each base classifier (random forest)
is fit on the kernel matrix of a subset of the training data.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
