%global packname  mineCitrus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Extract and Analyze Median Molecule Intensity from 'citrus'Output

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Citrus is a computational technique developed for the analysis of high
dimensional cytometry data sets. This package extracts, statistically
analyzes, and visualizes marker expression from 'citrus' data. This code
was used to generate data for Figures 3 and 4 in the forthcoming
manuscript: Throm et al. “Identification of Enhanced Interferon-Gamma
Signaling in Polyarticular Juvenile Idiopathic Arthritis with Mass
Cytometry”, JCI-Insight. For more information on Citrus, please see:
Bruggner et al. (2014) <doi:10.1073/pnas.1408792111>. To download the
'citrus' package, please see <https://github.com/nolanlab/citrus>.

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
