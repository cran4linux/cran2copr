%global packname  NNTbiomarker
%global packver   0.29.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.29.11
Release:          3%{?dist}
Summary:          Calculate Design Parameters for Biomarker Validation Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mvbutils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mvbutils 

%description
Helps a clinical trial team discuss the clinical goals of a well-defined
biomarker with a diagnostic, staging, prognostic, or predictive purpose.
From this discussion will come a statistical plan for a (non-randomized)
validation trial. Both prospective and retrospective trials are supported.
In a specific focused discussion, investigators should determine the range
of "discomfort" for the NNT, number needed to treat.  The meaning of the
discomfort range, [NNTlower, NNTupper], is that within this range most
physicians would feel discomfort either in treating or withholding
treatment. A pair of NNT values bracketing that range, NNTpos and NNTneg,
become the targets of the study's design.  If the trial can demonstrate
that a positive biomarker test yields an NNT less than NNTlower, and that
a negative biomarker test yields an NNT less than NNTlower, then the
biomarker may be useful for patients. A highlight of the package is
visualization of a "contra-Bayes" theorem, which produces criteria for
retrospective case-controls studies.

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
%doc %{rlibdir}/%{packname}/debugTools.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/human.html.R
%doc %{rlibdir}/%{packname}/Janes-fit.R
%doc %{rlibdir}/%{packname}/NOTUSED
%doc %{rlibdir}/%{packname}/oncotypeDX-risk-functions.jpg.xml
%doc %{rlibdir}/%{packname}/pageOpenTest.R
%doc %{rlibdir}/%{packname}/plot_digitizer_Figure_7_example.xml
%doc %{rlibdir}/%{packname}/rasterImages
%doc %{rlibdir}/%{packname}/ROCplots-Using-ggplot2.R
%doc %{rlibdir}/%{packname}/shinyAE
%doc %{rlibdir}/%{packname}/shinyCombinePlots
%doc %{rlibdir}/%{packname}/shinyElicit
%doc %{rlibdir}/%{packname}/shinyROC
%doc %{rlibdir}/%{packname}/temp
%doc %{rlibdir}/%{packname}/testing_ggplot_guides.R
%doc %{rlibdir}/%{packname}/ToDo.txt
%{rlibdir}/%{packname}/INDEX
