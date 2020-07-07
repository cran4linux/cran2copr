%global packname  concurve
%global packver   2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          3%{?dist}
Summary:          Computes and Plots Compatibility (Confidence) Intervals,P-Values, S-Values, & Likelihood Intervals to Form Consonance,Surprisal, & Likelihood Functions

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-bcaboot 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-ProfileLikelihood 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-MASS 
Requires:         R-CRAN-bcaboot 
Requires:         R-boot 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-officer 
Requires:         R-parallel 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-ProfileLikelihood 
Requires:         R-CRAN-scales 
Requires:         R-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-patchwork 

%description
Allows one to compute compatibility (confidence) intervals for various
statistical tests along with their corresponding P-values, S-values, and
likelihoods. The intervals can be plotted to create consonance, surprisal,
and likelihood functions allowing one to see what effect sizes are
compatible with the test model at various compatibility levels rather than
being limited to one interval estimate such as 95%. Functions can also be
compared to one another to see how much they overlap with one another and
differ. Results can also be exported for Word, Powerpoint, and TeX
documents. The package currently supports bootstrapping, linear models,
generalized linear models, linear mixed-effects models, survival analysis,
and meta-analysis. These methods are discussed by Poole C. (1987)
<doi:10.2105/AJPH.77.2.195>, Schweder T, Hjort NL. (2002)
<doi:10.1111/1467-9469.00285>, Singh K, Xie M, Strawderman WE. (2007)
<arXiv:0708.0976>, Rothman KJ, Greenland S, Lash TL. (2008,
ISBN:9781451190052), Greenland S. (2019)
<doi:10.1080/00031305.2018.1529625>, Chow ZR, Greenland S. (2019)
<arXiv:1909.08579>, and Greenland S, Chow ZR. (2019) <arXiv:1909.08583>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
