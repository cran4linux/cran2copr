%global __brp_check_rpaths %{nil}
%global packname  mefa
%global packver   3.2-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.7
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Data Handling in Ecology and Biogeography

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
A framework package aimed to provide standardized computational
environment for specialist work via object classes to represent the data
coded by samples, taxa and segments (i.e. subpopulations, repeated
measures). It supports easy processing of the data along with cross
tabulation and relational data tables for samples and taxa. An object of
class `mefa' is a project specific compendium of the data and can be
easily used in further analyses. Methods are provided for extraction,
aggregation, conversion, plotting, summary and reporting of `mefa'
objects. Reports can be generated in plain text or LaTeX format. Vignette
contains worked examples.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/SampleReport
%{rlibdir}/%{packname}/INDEX
