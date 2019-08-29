%global packname  ammistability
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Additive Main Effects and Multiplicative Interaction ModelStability Parameters

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
Computes various stability parameters from Additive Main Effects and
Multiplicative Interaction (AMMI) analysis results such as Modified AMMI
Stability Value (MASV), Sums of the Absolute Value of the Interaction
Principal Component Scores (SIPC), Sum Across Environments of
Genotype-Environment Interaction Modelled by AMMI (AMGE), Sum Across
Environments of Absolute Value of Genotype-Environment Interaction
Modelled by AMMI (AV_(AMGE)), AMMI Stability Index (ASI), Modified ASI
(MASI), AMMI Based Stability Parameter (ASTAB), Annicchiarico's D
Parameter (DA), Zhang's D Parameter (DZ), Averages of the Squared
Eigenvector Values (EV), Stability Measure Based on Fitted AMMI Model
(FA), Absolute Value of the Relative Contribution of IPCs to the
Interaction (Za). Further calculates the Simultaneous Selection Index for
Yield and Stability from the computed stability parameters. See the
vignette for complete list of citations for the methods implemented.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
