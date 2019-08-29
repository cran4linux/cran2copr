%global packname  gensvm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          A Generalized Multiclass Support Vector Machine

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
The GenSVM classifier is a generalized multiclass support vector machine
(SVM). This classifier aims to find decision boundaries that separate the
classes with as wide a margin as possible. In GenSVM, the loss function is
very flexible in the way that misclassifications are penalized.  This
allows the user to tune the classifier to the dataset at hand and
potentially obtain higher classification accuracy than alternative
multiclass SVMs.  Moreover, this flexibility means that GenSVM has a
number of other multiclass SVMs as special cases. One of the other
advantages of GenSVM is that it is trained in the primal space, allowing
the use of warm starts during optimization.  This means that for common
tasks such as cross validation or repeated model fitting, GenSVM can be
trained very quickly. Based on: G.J.J. van den Burg and P.J.F. Groenen
(2018) <http://www.jmlr.org/papers/v17/14-526.html>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
