%global packname  pssmooth
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Flexible and Efficient Evaluation of PrincipalSurrogates/Treatment Effect Modifiers

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-osDesign 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-chngpt 
BuildRequires:    R-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-osDesign 
Requires:         R-CRAN-np 
Requires:         R-CRAN-chngpt 
Requires:         R-MASS 

%description
Implements estimation and testing procedures for evaluating an
intermediate biomarker response as a principal surrogate of a clinical
response to treatment (i.e., principal stratification effect modification
analysis), as described in Juraska M, Huang Y, and Gilbert PB (2018),
Inference on treatment effect modification by biomarker response in a
three-phase sampling design, Biostatistics, kxy074
<doi:10.1093/biostatistics/kxy074>. The methods avoid the restrictive
'placebo structural risk' modeling assumption common to past methods and
further improve robustness by the use of nonparametric kernel smoothing
for biomarker density estimation. A randomized controlled two-group
clinical efficacy trial is assumed with an ordered categorical or
continuous univariate biomarker response measured at a fixed timepoint
post-randomization and with a univariate baseline surrogate measure
allowed to be observed in only a subset of trial participants with an
observed biomarker response (see the flexible three-phase sampling design
in the paper for details). Bootstrap-based procedures are available for
pointwise and simultaneous confidence intervals and testing of four
relevant hypotheses. Summary and plotting functions are provided for
estimation results.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
