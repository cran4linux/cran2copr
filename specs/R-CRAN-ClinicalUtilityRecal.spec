%global packname  ClinicalUtilityRecal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Recalibration Methods for Improved Clinical Utility of RiskScores

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-lattice 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-nloptr 

%description
Recalibrate risk scores (predicting binary outcomes) to improve clinical
utility of risk score using weighted logistic or constrained logistic
recalibration methods. Additionally, produces plots to assess the
potential for recalibration to improve the clinical utility of a risk
model. Methods are described in detail in Mishra, A. (2019) "Methods for
Risk Markers that Incorporate Clinical Utility"
<http://hdl.handle.net/1773/44068>.

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
%{rlibdir}/%{packname}/INDEX
