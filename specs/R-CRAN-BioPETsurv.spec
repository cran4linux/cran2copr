%global __brp_check_rpaths %{nil}
%global packname  BioPETsurv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Biomarker Prognostic Enrichment Tool for Time-to-Event Trial

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Prognostic Enrichment is a strategy of enriching a clinical trial for
testing an intervention intended to prevent or delay an unwanted clinical
event.  A prognostically enriched trial enrolls only patients who are more
likely to experience the unwanted clinical event than the broader patient
population (R. Temple (2010) <doi:10.1038/clpt.2010.233>). By testing the
intervention in an enriched study population, the trial may be adequately
powered with a smaller sample size, which can have both practical and
ethical advantages. This package provides tools to evaluate biomarkers for
prognostic enrichment of clinical trials with survival/time-to-event
outcomes.

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
%{rlibdir}/%{packname}/INDEX
