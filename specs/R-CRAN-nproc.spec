%global packname  nproc
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Neyman-Pearson (NP) Classification Algorithms and NP ReceiverOperating Characteristic (NP-ROC) Curves

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-naivebayes 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ada 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-tree 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-naivebayes 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-ada 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-tree 

%description
In many binary classification applications, such as disease diagnosis and
spam detection, practitioners commonly face the need to limit type I error
(i.e., the conditional probability of misclassifying a class 0 observation
as class 1) so that it remains below a desired threshold. To address this
need, the Neyman-Pearson (NP) classification paradigm is a natural choice;
it minimizes type II error (i.e., the conditional probability of
misclassifying a class 1 observation as class 0) while enforcing an upper
bound, alpha, on the type I error. Although the NP paradigm has a
century-long history in hypothesis testing, it has not been well
recognized and implemented in classification schemes. Common practices
that directly limit the empirical type I error to no more than alpha do
not satisfy the type I error control objective because the resulting
classifiers are still likely to have type I errors much larger than alpha.
As a result, the NP paradigm has not been properly implemented for many
classification scenarios in practice. In this work, we develop the first
umbrella algorithm that implements the NP paradigm for all scoring-type
classification methods, including popular methods such as logistic
regression, support vector machines and random forests. Powered by this
umbrella algorithm, we propose a novel graphical tool for NP
classification methods: NP receiver operating characteristic (NP-ROC)
bands, motivated by the popular receiver operating characteristic (ROC)
curves. NP-ROC bands will help choose in a data adaptive way and compare
different NP classifiers.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/nproc
%doc %{rlibdir}/%{packname}/nproc2
%{rlibdir}/%{packname}/INDEX
