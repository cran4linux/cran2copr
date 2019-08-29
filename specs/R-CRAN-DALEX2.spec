%global packname  DALEX2
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Descriptive mAchine Learning EXplanations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch

%description
Machine Learning models are widely used and have various applications in
classification or regression tasks. Due to increasing computational power,
availability of new data sources and new methods, ML models are more and
more complex. Models created with techniques like boosting, bagging of
neural networks are true black boxes. It is hard to trace the link between
input variables and model outcomes. They are used because of high
performance, but lack of interpretability is one of their weakest sides.
In many applications we need to know, understand or prove how input
variables are used in the model and what impact do they have on final
model prediction. DALEX2 is a collection of tools that help to understand
how complex predictive models are working. DALEX2 is a part of DrWhy
universe for tools for Explanation, Exploration and Visualisation for
Predictive Models.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
