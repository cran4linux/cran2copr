%global packname  PriorCD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Prioritizing Cancer Drugs for Interested Cancer

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-visNetwork 

%description
Prioritize candidate cancer drugs for drug repositioning based on the
random walk with restart algorithm in a drug-drug functional similarity
network. 1) We firstly constructed a drug-drug functional similarity
network by integrating pathway activity and drug activity derived from the
NCI-60 cancer cell lines. 2) Secondly, we calculated drug repurposing
score according to a set of approved therapeutic drugs of interested
cancer based on the random walk with restart algorithm in the drug-drug
functional similarity network. 3) Finally, the permutation test was used
to calculate the statistical significance level for the drug repurposing
score.

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
%doc %{rlibdir}/%{packname}/html_page.jpg
%doc %{rlibdir}/%{packname}/roc.jpeg
%{rlibdir}/%{packname}/INDEX
