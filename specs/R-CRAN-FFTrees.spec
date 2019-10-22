%global packname  FFTrees
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Generate, Visualise, and Evaluate Fast-and-Frugal Decision Trees

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-yarrr 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-caret 
Requires:         R-rpart 
Requires:         R-CRAN-yarrr 
Requires:         R-CRAN-circlize 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-caret 

%description
Create, visualize, and test fast-and-frugal decision trees (FFTs). FFTs
are very simple decision trees for binary classification problems. FFTs
can be preferable to more complex algorithms because they are easy to
communicate, require very little information, and are robust against
overfitting.

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
%doc %{rlibdir}/%{packname}/confusiontable.jpg
%doc %{rlibdir}/%{packname}/CoronaryArtery.jpg
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/FFTrees_Logo.jpg
%doc %{rlibdir}/%{packname}/HeartFFT.jpeg
%doc %{rlibdir}/%{packname}/mushrooms.jpg
%doc %{rlibdir}/%{packname}/titanic.jpg
%doc %{rlibdir}/%{packname}/virginica.jpg
%{rlibdir}/%{packname}/INDEX
