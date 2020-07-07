%global packname  pKSEA
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Prediction-Based Kinase-Substrate Enrichment Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch

%description
A tool for inferring kinase activity changes from phosphoproteomics data.
'pKSEA' uses kinase-substrate prediction scores to weight observed changes
in phosphopeptide abundance to calculate a phosphopeptide-level
contribution score, then sums up these contribution scores by kinase to
obtain a phosphoproteome-level kinase activity change score (KAC score).
'pKSEA' then assesses the significance of changes in predicted substrate
abundances for each kinase using permutation testing. This results in a
permutation score (pKSEA significance score) reflecting the likelihood of
a similarly high or low KAC from random chance, which can then be
interpreted in an analogous manner to an empirically calculated p-value.
'pKSEA' contains default databases of kinase-substrate predictions from
'NetworKIN' (NetworKINPred_db) <http://networkin.info> Horn, et. al (2014)
<doi:10.1038/nmeth.2968> and of known kinase-substrate links from
'PhosphoSitePlus' (KSEAdb) <https://www.phosphosite.org/> Hornbeck PV, et.
al (2015) <doi:10.1093/nar/gku1267>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
