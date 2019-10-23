%global packname  NeuralSens
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}
Summary:          Sensitivity Analysis of Neural Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-NeuralNetTools 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-NeuralNetTools 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Hmisc 

%description
Analysis functions to quantify inputs importance in neural network models.
Functions are available for calculating and plotting the inputs importance
and obtaining the activation function of each neuron layer and its
derivatives. The importance of a given input is defined as the
distribution of the derivatives of the output with respect to that input
in each training data point.

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
