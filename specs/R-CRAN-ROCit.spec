%global packname  ROCit
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Performance Assessment of Binary Classifier with Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 

%description
Sensitivity (or recall or true positive rate), false positive rate,
specificity, precision (or positive predictive value), negative predictive
value, misclassification rate, accuracy, F-score- these are popular
metrics for assessing performance of binary classifier for certain
threshold. These metrics are calculated at certain threshold values.
Receiver operating characteristic (ROC) curve is a common tool for
assessing overall diagnostic ability of the binary classifier. Unlike
depending on a certain threshold, area under ROC curve (also known as
AUC), is a summary statistic about how well a binary classifier performs
overall for the classification task. ROCit package provides flexibility to
easily evaluate threshold-bound metrics. Also, ROC curve, along with AUC,
can be obtained using different methods, such as empirical, binormal and
non-parametric. ROCit encompasses a wide variety of methods for
constructing confidence interval of ROC curve and AUC. ROCit also features
the option of constructing empirical gains table, which is a handy tool
for direct marketing. The package offers options for commonly used
visualization, such as, ROC curve, KS plot, lift plot. Along with in-built
default graphics setting, there are rooms for manual tweak by providing
the necessary values as function arguments. ROCit is a powerful tool
offering a range of things, yet it is very easy to use.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
