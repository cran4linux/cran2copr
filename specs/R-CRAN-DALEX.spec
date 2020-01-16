%global packname  DALEX
%global packver   0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          1%{?dist}
Summary:          Descriptive mAchine Learning EXplanations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Machine Learning (ML) models are widely used and have various applications
in classification or regression. Models created with boosting, bagging,
stacking or similar techniques are often used due to their high
performance, but such black-box models usually lack of interpretability.
DALEX package contains various explainers that help to understand the link
between input variables and model output. The single_variable() explainer
extracts conditional response of a model as a function of a single
selected variable. It is a wrapper over packages 'pdp' (Greenwell 2017)
<doi:10.32614/RJ-2017-016>, 'ALEPlot' (Apley 2018) <arXiv:1612.08468> and
'factorMerger' (Sitko and Biecek 2017) <arXiv:1709.04412>. The
single_prediction() explainer attributes parts of a model prediction to
particular variables used in the model. It is a wrapper over 'breakDown'
package (Staniak and Biecek 2018) <doi:10.32614/RJ-2018-072>. The
variable_dropout() explainer calculates variable importance scores based
on variable shuffling (Fisher at al. 2018) <arXiv:1801.01489>. All these
explainers can be plotted with generic plot() function and compared across
different models. 'DALEX' is a part of the 'DrWhy.AI' universe (Biecek
2018) <arXiv:1806.08915>.

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
