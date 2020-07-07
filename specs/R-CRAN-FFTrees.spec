%global packname  FFTrees
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          3%{?dist}
Summary:          Generate, Visualise, and Evaluate Fast-and-Frugal Decision Trees

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-rpart 
Requires:         R-CRAN-circlize 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 

%description
Create, visualize, and test fast-and-frugal decision trees (FFTs). FFTs
are very simple decision trees for binary classification problems. FFTs
can be preferable to more complex algorithms because they are easy to
communicate, require very little information, and are robust against
overfitting.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
