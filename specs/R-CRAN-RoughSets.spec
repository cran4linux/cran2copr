%global __brp_check_rpaths %{nil}
%global packname  RoughSets
%global packver   1.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          3%{?dist}%{?buildtag}
Summary:          Data Analysis Using Rough Set and Fuzzy Rough Set Theories

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Implementations of algorithms for data analysis based on the rough set
theory (RST) and the fuzzy rough set theory (FRST). We not only provide
implementations for the basic concepts of RST and FRST but also popular
algorithms that derive from those theories. The methods included in the
package can be divided into several categories based on their
functionality: discretization, feature selection, instance selection, rule
induction and classification based on nearest neighbors. RST was
introduced by Zdzisław Pawlak in 1982 as a sophisticated mathematical tool
to model and process imprecise or incomplete information. By using the
indiscernibility relation for objects/instances, RST does not require
additional parameters to analyze the data. FRST is an extension of RST.
The FRST combines concepts of vagueness and indiscernibility that are
expressed with fuzzy sets (as proposed by Zadeh, in 1965) and RST.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
