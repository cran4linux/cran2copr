%global packname  mlearning
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Machine learning algorithms with unified interface and confusionmatrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-class 
BuildRequires:    R-nnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ipred 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-class 
Requires:         R-nnet 
Requires:         R-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ipred 

%description
This package provides a unified interface to various machine learning
algorithms. Confusion matrices are provided too.

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
