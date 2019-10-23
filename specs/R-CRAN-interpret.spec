%global packname  interpret
%global packver   0.1.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.22
Release:          1%{?dist}
Summary:          Fit Interpretable Models and Explain Blackbox Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
Machine Learning package for training interpretable models and explaining
blackbox systems. Historically, the most intelligible models were not very
accurate, and the most accurate models were not intelligible. Microsoft
Research has developed an algorithm called the Explainable Boosting
Machine (EBM) which has both high accuracy and intelligibility. EBM uses
machine learning techniques like bagging and boosting to breathe new life
into traditional GAMs (Generalized Additive Models). This makes them as
accurate as random forests and gradient boosted trees, and also enhances
their intelligibility and editability. Details on the EBM algorithm can be
found in the paper by Rich Caruana, Yin Lou, Johannes Gehrke, Paul Koch,
Marc Sturm, and Noemie Elhadad (2015, <doi:10.1145/2783258.2788613>).

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
%{rlibdir}/%{packname}/libs
