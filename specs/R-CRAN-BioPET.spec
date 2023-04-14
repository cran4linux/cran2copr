%global __brp_check_rpaths %{nil}
%global packname  BioPET
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Biomarker Prognostic Enrichment Tool

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-VGAM 

%description
Prognostic Enrichment is a clinical trial strategy of evaluating an
intervention in a patient population with a higher rate of the unwanted
event than the broader patient population (R. Temple (2010)
<DOI:10.1038/clpt.2010.233>). A higher event rate translates to a lower
sample size for the clinical trial, which can have both practical and
ethical advantages. This package is a tool to help evaluate biomarkers for
prognostic enrichment of clinical trials.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
