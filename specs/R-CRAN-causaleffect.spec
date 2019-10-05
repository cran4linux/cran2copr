%global packname  causaleffect
%global packver   1.3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.10
Release:          1%{?dist}
Summary:          Deriving Expressions of Joint Interventional Distributions andTransport Formulas in Causal Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggm 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-ggm 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-XML 

%description
Functions for identification and transportation of causal effects.
Provides a conditional causal effect identification algorithm (IDC) by
Shpitser, I. and Pearl, J. (2006)
<http://ftp.cs.ucla.edu/pub/stat_ser/r329-uai.pdf>, an algorithm for
transportability from multiple domains with limited experiments by
Bareinboim, E. and Pearl, J. (2014)
<http://ftp.cs.ucla.edu/pub/stat_ser/r443.pdf> and a selection bias
recovery algorithm by Bareinboim, E. and Tian, J. (2015)
<http://ftp.cs.ucla.edu/pub/stat_ser/r445.pdf>. All of the previously
mentioned algorithms are based on a causal effect identification algorithm
by Tian , J. (2002) <http://ftp.cs.ucla.edu/pub/stat_ser/r309.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
