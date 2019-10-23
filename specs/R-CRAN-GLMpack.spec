%global packname  GLMpack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Data and Code to Accompany Generalized Linear Models, 2ndEdition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pBrackets 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-effects 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-foreign 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-censReg 
BuildRequires:    R-CRAN-plm 
Requires:         R-MASS 
Requires:         R-CRAN-pBrackets 
Requires:         R-nnet 
Requires:         R-CRAN-effects 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-pscl 
Requires:         R-foreign 
Requires:         R-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-censReg 
Requires:         R-CRAN-plm 

%description
Contains all the data and functions used in Generalized Linear Models, 2nd
edition, by Jeff Gill and Michelle Torres. Examples to create all models,
tables, and plots are included for each data set.

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
