%global packname  powerpkg
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}
Summary:          Power analyses for the affected sib pair and the TDT design

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tcltk 
Requires:         R-tcltk 

%description
(1) To estimate the power of testing for linkage using an affected sib
pair design, as a function of the recurrence risk ratios. We will use
analytical power formulae as implemented in R. These are based on a
Mathematica notebook created by Martin Farrall. (2) To examine how the
power of the transmission disequilibrium test (TDT) depends on the disease
allele frequency, the marker allele frequency, the strength of the linkage
disequilibrium, and the magnitude of the genetic effect. We will use an R
program that implements the power formulae of Abel and Muller-Myhsok
(1998). These formulae allow one to quickly compute power of the TDT
approach under a variety of different conditions. This R program was
modeled on Martin Farrall's Mathematica notebook.

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
