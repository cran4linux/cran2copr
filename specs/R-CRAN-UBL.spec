%global packname  UBL
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          2%{?dist}
Summary:          An Implementation of Re-Sampling Approaches to Utility-BasedLearning for Both Classification and Regression Tasks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-randomForest 

%description
Provides a set of functions that can be used to obtain better predictive
performance on cost-sensitive and cost/benefits tasks (for both regression
and classification). This includes re-sampling approaches that modify the
original data set biasing it towards the user preferences.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
