%global packname  LDAvis
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Interactive Visualization of Topic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-parallel 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-RJSONIO 
Requires:         R-parallel 

%description
Tools to create an interactive web-based visualization of a topic model
that has been fit to a corpus of text data using Latent Dirichlet
Allocation (LDA). Given the estimated parameters of the topic model, it
computes various summary statistics as input to an interactive
visualization built with D3.js that is accessed via a browser. The goal is
to help users interpret the topics in their LDA topic model.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/htmljs
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
