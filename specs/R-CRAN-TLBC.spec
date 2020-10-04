%global packname  TLBC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Two-Level Behavior Classification

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-HMM 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-HMM 
Requires:         R-tools 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-caret 

%description
Contains functions for training and applying two-level random forest and
hidden Markov models for human behavior classification from raw tri-axial
accelerometer and/or GPS data. Includes functions for training a two-level
model, applying the model to data, and computing performance.

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
