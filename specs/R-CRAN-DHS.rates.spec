%global packname  DHS.rates
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Calculates Demographic Indicators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-crayon 

%description
Calculates key indicators such as fertility rates (Total Fertility Rate
(TFR), General Fertility Rate (GFR), and Age Specific Fertility Rate
(ASFR)) using Demographic and Health Survey (DHS) women/individual data,
and childhood mortality probabilities and rates such as Neonatal Mortality
Rate (NNMR), Post-neonatal Mortality Rate (PNNMR), Infant Mortality Rate
(IMR), Child Mortality Rate (CMR), and Under-five Mortality Rate (U5MR).
In addition to the indicators, the 'DHS.rates' package estimates sampling
errors indicators such as Standard Error (SE), Design Effect (DEFT),
Relative Standard Error (RSE) and Confidence Interval (CI). The package is
developed according to the DHS methodology of calculating the fertility
indicators and the childhood mortality rates outlined in the "Guide to DHS
Statistics" (Croft, Trevor N., Aileen M. J. Marshall, Courtney K. Allen,
et al. 2018,
<https://dhsprogram.com/Data/Guide-to-DHS-Statistics/index.cfm>) and the
DHS methodology of estimating the sampling errors indicators outlined in
the "DHS Sampling and Household Listing Manual" (ICF International 2012,
<https://dhsprogram.com/pubs/pdf/DHSM4/DHS6_Sampling_Manual_Sept2012_DHSM4.pdf>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
