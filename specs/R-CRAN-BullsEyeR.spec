%global __brp_check_rpaths %{nil}
%global packname  BullsEyeR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Topic Modelling

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-slam 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-topicmodels 
Requires:         R-Matrix 
Requires:         R-CRAN-slam 

%description
Helps in initial processing like converting text to lower case, removing
punctuation, numbers, stop words, stemming, sparsity control and term
frequency inverse document frequency processing. Helps in recognizing
domain or corpus specific stop words. Makes use of 'ldatunig' output to
pick optimal number of topics for topic modelling. Helps in topic
modelling the content.

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
%doc %{rlibdir}/%{packname}/ext
%{rlibdir}/%{packname}/INDEX
