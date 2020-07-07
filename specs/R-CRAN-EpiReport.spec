%global packname  EpiReport
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Epidemiological Report

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-png 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-extrafont 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-rmarkdown 

%description
Drafting an epidemiological report in 'Microsoft Word' format for a given
disease, similar to the Annual Epidemiological Reports published by the
European Centre for Disease Prevention and Control. Through standalone
functions, it is specifically designed to generate each disease specific
output presented in these reports and includes: - Table with the
distribution of cases by Member State over the last five years; -
Seasonality plot with the distribution of cases at the European Union /
European Economic Area level, by month, over the past five years; - Trend
plot with the trend and number of cases at the European Union / European
Economic Area level, by month, over the past five years; - Age and gender
bar graph with the distribution of cases at the European Union / European
Economic Area level. Two types of datasets can be used: - The default
dataset of salmonella 2012-2016 data; - Any dataset specified as described
in the vignette.

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
%doc %{rlibdir}/%{packname}/maps
%doc %{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/INDEX
