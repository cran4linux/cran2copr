%global packname  featurefinder
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Feature Finder

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grDevices 
Requires:         R-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-grDevices 

%description
Finds modelling features through a detailed analysis of model residuals
using 'rpart' classification and regression trees. Scans the residuals of
a model across subsets of the data to identify areas where the model
prediction differs from the actual target variable. S. Chatterjee, A. S.
Hadi (2006) <doi:10.1002/0470055464>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
