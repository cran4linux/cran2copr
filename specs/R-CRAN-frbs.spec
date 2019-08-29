%global packname  frbs
%global packver   3.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          Fuzzy Rule-Based Systems for Classification and Regression Tasks

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
An implementation of various learning algorithms based on fuzzy rule-based
systems (FRBSs) for dealing with classification and regression tasks.
Moreover, it allows to construct an FRBS model defined by human experts.
FRBSs are based on the concept of fuzzy sets, proposed by Zadeh in 1965,
which aims at representing the reasoning of human experts in a set of
IF-THEN rules, to handle real-life problems in, e.g., control, prediction
and inference, data mining, bioinformatics data processing, and robotics.
FRBSs are also known as fuzzy inference systems and fuzzy models. During
the modeling of an FRBS, there are two important steps that need to be
conducted: structure identification and parameter estimation. Nowadays,
there exists a wide variety of algorithms to generate fuzzy IF-THEN rules
automatically from numerical data, covering both steps. Approaches that
have been used in the past are, e.g., heuristic procedures, neuro-fuzzy
techniques, clustering methods, genetic algorithms, squares methods, etc.
Furthermore, in this version we provide a universal framework named
'frbsPMML', which is adopted from the Predictive Model Markup Language
(PMML), for representing FRBS models. PMML is an XML-based language to
provide a standard for describing models produced by data mining and
machine learning algorithms. Therefore, we are allowed to export and
import an FRBS model to/from 'frbsPMML'. Finally, this package aims to
implement the most widely used standard procedures, thus offering a
standard package for FRBS modeling to the R community.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
