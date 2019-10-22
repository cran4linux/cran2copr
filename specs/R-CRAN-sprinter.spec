%global packname  sprinter
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Framework for Screening Prognostic Interactions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CoxBoost 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-GAMBoost 
BuildRequires:    R-CRAN-randomForestSRC 
BuildRequires:    R-CRAN-LogicReg 
Requires:         R-CRAN-CoxBoost 
Requires:         R-survival 
Requires:         R-CRAN-GAMBoost 
Requires:         R-CRAN-randomForestSRC 
Requires:         R-CRAN-LogicReg 

%description
The main function of this package builds prognostic models that consider
interactions by combining available statistical components. Furthermore,
it provides a function for evaluating the relevance of the selected
interactions by resampling techniques.

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
