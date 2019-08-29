%global packname  hopit
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Hierarchical Ordered Probit Models with Application to ReportingHeterogeneity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-survey >= 3.35
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-survey >= 3.35
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-CRAN-Rdpack 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Self-reported health, happiness, attitudes, and other statuses or
perceptions are often the subject of biases that may come from different
sources. For example, the evaluation of own health may depend on previous
medical diagnoses, functional status, and symptoms and signs of illness,
as well as life-style behaviors including contextual social, gender,
age-specific, linguistic and other cultural factors (Jylha 2009
<doi:10.1016/j.socscimed.2009.05.013>; Oksuzyan et al. 2019
<doi:10.1016/j.socscimed.2019.03.002>). This package offers versatile
functions for analyzing different self-reported ordinal variables and
helping to estimate their biases. Specifically, the package provides the
function to fit a generalized ordered probit model that regresses original
self-reported status measures on two sets of independent variables (King
et al. 2004 <doi:10.1017/S0003055403000881>; Jurges 2007
<doi:10.1002/hec.1134>; Oksuzyan et al. 2019
<doi:10.1016/j.socscimed.2019.03.002>). In contrast to standard ordered
probit models, generalized ordered probit models relax the assumption that
individuals use a common scale when rating their own statuses, and thus
allow for distinguishing between the status (e.g., health) and reporting
differences based on other individual characteristics. In other words, the
model accounts for heterogeneity in reporting behaviors. The first set of
variables (e.g., health variables) included in the regression are
individual statuses and characteristics that are directly related to the
self-reported variable. In case of self-reported health, these could be
chronic conditions, mobility level, difficulties with daily activities,
performance on grip strength tests, anthropometric measures, and lifestyle
behaviors. The second set of independent variables (threshold variables)
is used to model cut-points between adjacent self-reported response
categories as functions of individual characteristics, such as gender, age
group, education, and country (Oksuzyan et al. 2019
<doi:10.1016/j.socscimed.2019.03.002>). The model helps adjust for these
specific socio-demographic and cultural differences in how the continuous
latent health is projected onto the ordinal self-rated measure. The fitted
model can be used to calculate an individual latent status variable that
serves as a proxy of the true status. In case of self-reported health, the
predicted latent health variable can be standardized to a health index,
which varies from 0 representing the (model-based) worst health state to 1
representing the (model-based) best health in the sample. The standardized
latent coefficients (disability weights for the case of self-rated health)
provide information about the individual impact of the specific latent
(e.g., health) variables on the latent (e.g., health) construct. For
example, they indicate the extent to which the latent health index is
reduced by the presence of Parkinson’s disease, poor mobility, and other
specific health measures (Jurges 2007 <doi:10.1002/hec.1134>; Oksuzyan et
al. 2019 <doi:10.1016/j.socscimed.2019.03.002>). The latent index can in
turn be used to reclassify the categorical status measure that has been
adjusted for inter-individual differences in reporting behavior. Two
methods for doing so are available, one which uses model estimated
cut-points, and a second which reclassifies responses according to the
percentiles of the original categorical response distribution (Jurges 2007
<doi:10.1002/hec.1134>; Oksuzyan et al. 2019
<doi:10.1016/j.socscimed.2019.03.002>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES_VIG.bib
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
