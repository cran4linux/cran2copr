%global packname  joineRmeta
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Joint Modelling for Meta-Analytic (Multi-Study) Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-JM 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-joineR 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-utils 
Requires:         R-CRAN-lme4 
Requires:         R-survival 
Requires:         R-CRAN-JM 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-joineR 
Requires:         R-MASS 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-utils 

%description
Fits joint models of the type proposed by Henderson and colleagues (2000)
<doi:10.1093/biostatistics/1.4.465>, but extends to the multi-study,
meta-analytic case. Functions for meta-analysis of a single longitudinal
and a single time-to-event outcome from multiple studies using joint
models. Options to produce plots for multi study joint data, to pool joint
model fits from 'JM' and 'joineR' packages in a two stage meta-analysis,
and to model multi-study joint data in a one stage meta-analysis.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
