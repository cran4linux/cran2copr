%global packname  topicdoc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Topic-Specific Diagnostics for LDA and CTM Topic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-topicmodels 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-topicmodels 

%description
Calculates topic-specific diagnostics (e.g. mean token length,
exclusivity) for Latent Dirichlet Allocation and Correlated Topic Models
fit using the 'topicmodels' package. For more details, see Chapter 12 in
Airoldi et al. (2014, ISBN:9781466504080), pp 262-272 Mimno et al. (2011,
ISBN:9781937284114), and Bischof et al. (2014) <arXiv:1206.4631v1>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/generate_test_topic_models.R
%{rlibdir}/%{packname}/INDEX
