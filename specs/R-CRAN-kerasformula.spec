%global packname  kerasformula
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          A High-Level R Interface for Neural Nets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-dplyr 
Requires:         R-Matrix 
Requires:         R-CRAN-ggplot2 

%description
Adds a high-level interface for 'keras' neural nets. kms() fits neural net
and accepts R formulas to aid data munging and hyperparameter selection.
kms() can optionally accept a compiled keras_sequential_model() from
'keras'. kms() accepts a number of parameters (like loss and optimizer)
and splits the data into (optionally sparse) test and training matrices.
kms() facilitates setting advanced hyperparameters (e.g., regularization).
kms() returns a single object with predictions, a confusion matrix, and
function call details.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
