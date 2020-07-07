%global packname  MAP
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Multimodal Automated Phenotyping

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexmix >= 2.3.14
BuildRequires:    R-Matrix >= 1.2.10
Requires:         R-CRAN-flexmix >= 2.3.14
Requires:         R-Matrix >= 1.2.10

%description
Electronic health records (EHR) linked with biorepositories are a powerful
platform for translational studies. A major bottleneck exists in the
ability to phenotype patients accurately and efficiently. Towards that
end, we developed an automated high-throughput phenotyping method
integrating International Classification of Diseases (ICD) codes and
narrative data extracted using natural language processing (NLP).
Specifically, our proposed method, called MAP (Map Automated Phenotyping
algorithm), fits an ensemble of latent mixture models on aggregated ICD
and NLP counts along with healthcare utilization. The MAP algorithm yields
a predicted probability of phenotype for each patient and a threshold for
classifying subjects with phenotype yes/no (See Katherine P. Liao, et al.
(2019) <doi:10.1101/587436>.).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
