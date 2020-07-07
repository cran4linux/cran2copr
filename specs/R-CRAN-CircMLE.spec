%global packname  CircMLE
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Maximum Likelihood Analysis of Circular Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-circular >= 0.4.7
BuildRequires:    R-stats 
Requires:         R-CRAN-circular >= 0.4.7
Requires:         R-stats 

%description
A series of wrapper functions to implement the 10 maximum likelihood
models of animal orientation described by Schnute and Groot (1992)
<DOI:10.1016/S0003-3472(05)80068-5>. The functions also include the
ability to use different optimizer methods and calculate various model
selection metrics (i.e., AIC, AICc, BIC).  The ability to perform variants
of the Hermans-Rasson test and Pycke test is also included as described in
Landler et al. (2019) <DOI:10.1186/s12898-019-0246-8>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
