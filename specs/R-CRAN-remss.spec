%global packname  remss
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Refining Evaluation Methodology on Stage System

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-survival 
Requires:         R-survival 

%description
T (extent of the primary tumor), N (absence or presence and extent of
regional lymph node metastasis) and M (absence or presence of distant
metastasis) are three components to describe the anatomical tumor extent.
TNM stage is important in treatment decision-making and outcome
predicting. The existing oropharyngeal Cancer (OPC) TNM stages have not
made distinction of the two sub sites of Human papillomavirus positive
(HPV+) and Human papillomavirus negative (HPV-) diseases. We developed
novel criteria to assess performance of the TNM stage grouping schemes
based on parametric modeling adjusting on important clinical factors.
These criteria evaluate the TNM stage grouping scheme in five different
measures: hazard consistency, hazard discrimination, explained variation,
likelihood difference, and balance. The methods are described in Xu, W.,
et al. (2015)
<https://www.austinpublishinggroup.com/biometrics/fulltext/biometrics-v2-id1014.php>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
