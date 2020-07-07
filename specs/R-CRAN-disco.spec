%global packname  disco
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          3%{?dist}
Summary:          Discordance and Concordance of Transcriptomic Responses

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tmod 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tmod 
Requires:         R-CRAN-RColorBrewer 

%description
Concordance and discordance of homologous gene regulation allows comparing
reaction to stimuli in different organisms, for example human patients and
animal models of a disease. The package contains functions to calculate
discordance and concordance score for homologous gene pairs, identify
concordantly or discordantly regulated transcriptional modules and
visualize the results. It is intended for analysis of transcriptional
data.

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
