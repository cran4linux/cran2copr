%global packname  esDesign
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Adaptive Enrichment Designs with Sample Size Re-Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Software of 'esDesign' is developed to implement the adaptive enrichment
designs with sample size re-estimation. In details, three-proposed trial
designs are provided, including the AED1-SSR (or ES1-SSR), AED2-SSR (or
ES2-SSR) and AED3-SSR (or ES3-SSR). In addition, this package also
contains several widely used adaptive designs, such as the Marker
Sequential Test (MaST) design proposed Freidlin et al. (2014)
<doi:10.1177/1740774513503739>, the adaptive enrichment designs without
early stopping (AED or ES), the sample size re-estimation procedure (SSR)
based on the conditional power proposed by Proschan and Hunsberger (1995),
and some useful functions. In details, we can calculate the futility
and/or efficacy stopping boundaries, the sample size required, calibrate
the value of the threshold of the difference between subgroup-specific
test statistics, conduct the simulation studies in AED, SSR, AED1-SSR,
AED2-SSR and AED3-SSR.

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
%{rlibdir}/%{packname}/INDEX
