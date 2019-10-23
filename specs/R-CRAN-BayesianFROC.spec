%global debug_package %{nil}
%global packname  BayesianFROC
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          FROC Analysis by Bayesian Approaches

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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

%description
Before reading this, execute BayesianFROC::fit_GUI() or
BayesianFROC::fit_GUI_simple() or BayesianFROC::fit_GUI_dashboard(), then
reader will understand this package without any explanation. Provides new
methods for the so-called Free-response Receiver Operating Characteristic
(FROC) analysis. The ultimate aim of FROC analysis is to compare observer
performances, which means comparing characteristics, such as area under
the curve (AUC) or figure of merit (FOM). In this package, we only use the
notion of AUC for modality comparison, where by "modality", we mean
imaging methods such as Magnetic Resonance Imaging (MRI), Computed
Tomography (CT), Positron Emission Tomography (PET), ..., etc. So there is
a problem that which imaging method is better to detect lesions from
shadows in radiographs. To solve modality comparison issues, this package
provides new methods using hierarchical Bayesian models proposed by the
author of this package. Using this package, one can obtain at least one
conclusion that which imaging methods are better for finding lesions in
radiographs with the case of your data. Fitting FROC statistical models is
sometimes not so good, it can easily confirm by drawing FROC curves and
comparing these curves and the points constructed by False Positive
fractions (FPFs) and True Positive Fractions (TPFs), we can validate the
goodness of fit intuitively. Such validation is also implemented by the
Chi square goodness of fit statistics in the Bayesian context which means
that the parameter is not deterministic, thus by integrating it with the
posterior predictive measure, we get a desired value. To compare
modalities (imaging methods: MRI, CT, PET, ... , etc), we evaluate AUCs
for each modality. FROC is developed by Dev Chakraborty, his FROC model in
his 1989 paper relies on the maximal likelihood methodology. The author
modified and provided the alternative Bayesian FROC model. Strictly
speaking, his model does not coincide with models in this package. In FROC
context, we means by multiple reader and multiple case (MRMC) the case of
the number of reader or modality is two or more. The MRMC data is
available for functions of this package. I hope that medical researchers
use not only the frequentist method but also alternative Bayesian methods.
In medical research, many problems are considered under only frequentist
methods, such as the notion of p-values. But p-value is sometimes
misunderstood. Bayesian methods provide very simple, direct, intuitive
answer for research questions. Combining frequentist methods with Bayesian
methods, we can obtain more reliable answer for research questions. Please
execute the following R scripts from the R (R studio) console,
demo(demo_MRMC, package = "BayesianFROC"); demo(demo_srsc, package =
"BayesianFROC"); demo(demo_stan, package = "BayesianFROC");
demo(demo_drawcurves_srsc, package = "BayesianFROC");
demo_Bayesian_FROC(); demo_Bayesian_FROC_without_pause(). References: Dev
Chakraborty (1989) <doi:10.1118/1.596358> Maximum likelihood analysis of
free - response receiver operating characteristic (FROC) data. Pre-print:
Issei Tsunoda; Bayesian Models for free-response receiver operating
characteristic analysis. See the vignettes for more details.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/image
%doc %{rlibdir}/%{packname}/myapp
%doc %{rlibdir}/%{packname}/myappp
%{rlibdir}/%{packname}/INDEX
