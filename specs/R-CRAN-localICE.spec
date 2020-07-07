%global packname  localICE
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Local Individual Conditional Expectation

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 

%description
Local Individual Conditional Expectation ('localICE') is a local
explanation approach from the field of eXplainable Artificial Intelligence
(XAI). localICE is a model-agnostic XAI approach which provides
three-dimensional local explanations for particular data instances. The
approach is proposed in the master thesis of Martin Walter as an extension
to ICE (see Reference). The three dimensions are the two features at the
horizontal and vertical axes as well as the target represented by
different colors. The approach is applicable for classification and
regression problems to explain interactions of two features towards the
target. For classification models, the number of classes can be more than
two and each class is added as a different color to the plot. The given
instance is added to the plot as two dotted lines according to the feature
values. The localICE-package can explain features of type factor and
numeric of any machine learning model. Automatically supported machine
learning packages are 'mlr', 'randomForest', 'caret' or all other with an
S3 predict function. For further model types from other libraries, a
predict function has to be provided as an argument in order to get access
to the model. Reference to the ICE approach: Alex Goldstein, Adam
Kapelner, Justin Bleich, Emil Pitkin (2013) <arXiv:1309.6392>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
