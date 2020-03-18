%global packname  BayesianFROC
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          FROC Analysis by Bayesian Approaches

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.18.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-tcltk 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-rstan >= 2.18.2
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-xlsx 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-tcltk 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-car 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinythemes 

%description
Execute BayesianFROC::fit_GUI_Shiny() (or fit_GUI_Shiny_MRMC()) for a
graphical user interface via Shiny. The free-response receiver operating
characteristic (FROC) method is a generalization of receiver operating
characteristic (ROC) analysis. However, Chakraborty's classical model is
non-generative in the sense that it cannot synthesize data. This package
aims to modify his models to be generative using a Bayesian approach, and
to verify that our models fit practical datasets. We also develop a
Bayesian model for comparing modalities. Chakraborty [1] defined a
free-response receiver operating characteristic (FROC) model based on
maximum likelihood (ML). However, his model is non-generative in the sense
that it cannot generate FROC datasets. In signal detection theory, the
number of true positives never exceeds the number of targets. However,
this is not explained by any existing model. Thus, in this package, the
author contributes to FROC theory by refining Chakraborty’s model to
obtain models that are generative. This modification allows us to use FROC
analysis in a general statistical scheme, and as a benefit, our generative
model can be applied to calculations of posterior predictive p values that
require generation of synthetic datasets from fitted models. Furthermore,
this package presents new models for comparison of modalities. Modality
comparison is a common problem in radiology, and has been studied
extensively. However, in many medical studies, such problems are addressed
with non-Bayesian methods such as ANOVA. As a supplementary topic, this
work presents a Bayesian model that includes individual differences. With
this model, we can account for differences between individual readers when
comparing modalities, using Bayesian rather than ML-methods. The author
found the existing FROC model in [1] to be non-generative for calculation
of posterior predictive p values. Replacing the ML-based method with a
Bayesian approach differs from standard practice but provides insight into
the problems of existing methods. Please execute the following R scripts
from the R (R studio) console, demo(demo_MRMC, package = "BayesianFROC");
demo(demo_srsc, package = "BayesianFROC"); demo(demo_stan, package =
"BayesianFROC"); demo(demo_drawcurves_srsc, package = "BayesianFROC");
demo_Bayesian_FROC(); demo_Bayesian_FROC_without_pause(). References: [1]
Dev Chakraborty (1989) <doi:10.1118/1.596358> Maximum likelihood analysis
of free - response receiver operating characteristic (FROC) data.
Pre-print: Issei Tsunoda; Generative Models for free-response receiver
operating characteristic analysis. See the vignettes for more details.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/myapp
%doc %{rlibdir}/%{packname}/myappp
%{rlibdir}/%{packname}/INDEX
