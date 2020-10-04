%global packname  depmixS4
%global packver   1.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Dependent Mixture Models - Hidden Markov Models of GLMs andOther Distributions in S4

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-nnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
Requires:         R-nnet 
Requires:         R-MASS 
Requires:         R-CRAN-Rsolnp 
Requires:         R-nlme 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-methods 

%description
Fits latent (hidden) Markov models on mixed categorical and continuous
(time series) data, otherwise known as dependent mixture models, see
Visser & Speekenbrink (2010, <DOI:10.18637/jss.v036.i07>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
