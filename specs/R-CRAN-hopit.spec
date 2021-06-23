%global __brp_check_rpaths %{nil}
%global packname  hopit
%global packver   0.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.3
Release:          3%{?dist}%{?buildtag}
Summary:          Hierarchical Ordered Probit Models with Application to ReportingHeterogeneity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survey >= 3.35
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-survey >= 3.35
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Self-reported health, happiness, attitudes, and other statuses or
perceptions are often the subject of biases that may come from different
sources. For example, the evaluation of an individual’s own health may
depend on previous medical diagnoses, functional status, and symptoms and
signs of illness; as on well as life-style behaviors, including contextual
social, gender, age-specific, linguistic and other cultural factors (Jylha
2009 <doi:10.1016/j.socscimed.2009.05.013>; Oksuzyan et al. 2019
<doi:10.1016/j.socscimed.2019.03.002>). The hopit package offers versatile
functions for analyzing different self-reported ordinal variables, and for
helping to estimate their biases. Specifically, the package provides the
function to fit a generalized ordered probit model that regresses original
self-reported status measures on two sets of independent variables (King
et al. 2004 <doi:10.1017/S0003055403000881>; Jurges 2007
<doi:10.1002/hec.1134>; Oksuzyan et al. 2019
<doi:10.1016/j.socscimed.2019.03.002>). The first set of variables (e.g.,
health variables) included in the regression are individual statuses and
characteristics that are directly related to the self-reported variable.
In the case of self-reported health, these could be chronic conditions,
mobility level, difficulties with daily activities, performance on grip
strength tests, anthropometric measures, and lifestyle behaviors. The
second set of independent variables (threshold variables) is used to model
cut-points between adjacent self-reported response categories as functions
of individual characteristics, such as gender, age group, education, and
country (Oksuzyan et al. 2019 <doi:10.1016/j.socscimed.2019.03.002>). The
model helps to adjust for specific socio-demographic and cultural
differences in how the continuous latent health is projected onto the
ordinal self-rated measure. The fitted model can be used to calculate an
individual predicted latent status variable, a latent index, and
standardized latent coefficients; and makes it possible to reclassify a
categorical status measure that has been adjusted for inter-individual
differences in reporting behavior.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
