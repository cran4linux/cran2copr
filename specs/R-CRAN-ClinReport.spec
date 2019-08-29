%global packname  ClinReport
%global packver   0.9.1.13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1.13.1
Release:          1%{?dist}
Summary:          Statistical Reporting for Scientific Publications,Epidemiological Studies and Clinical Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-emmeans >= 1.3.2
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-flextable >= 0.5.1
BuildRequires:    R-CRAN-officer >= 0.3.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-emmeans >= 1.3.2
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-flextable >= 0.5.1
Requires:         R-CRAN-officer >= 0.3.3
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 
Requires:         R-CRAN-xtable 

%description
Export to 'Microsoft Word' or R markdown documents nicely formatted tables
of descriptive or inferential statistics. Can be used within the scope of
clinical trials, or for any scientific publications. Descriptive tables
for quantitative statistics (mean, median, max etc..) and/or qualitative
statistics (frequencies and percentages) are available along with
formatted tables of Least Square Means of Linear Models, Linear Mixed
Models, Cox Models and Generalized Linear Mixed Models. It works mainly
with 'emmeans' 'officer' and 'flextable' packages.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/clean.character.R
%{rlibdir}/%{packname}/data.creation.R
%doc %{rlibdir}/%{packname}/dev_check_build.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/global.report.frailty.R
%doc %{rlibdir}/%{packname}/report.ae.R
%doc %{rlibdir}/%{packname}/report.chisq.frailty.R
%doc %{rlibdir}/%{packname}/report.frailty.R
%doc %{rlibdir}/%{packname}/report.HR.frailty.R
%doc %{rlibdir}/%{packname}/test.R
%doc %{rlibdir}/%{packname}/TODO
%doc %{rlibdir}/%{packname}/transpose.desc.R
%{rlibdir}/%{packname}/INDEX
