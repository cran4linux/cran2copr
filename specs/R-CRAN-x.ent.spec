%global packname  x.ent
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          2%{?dist}
Summary:          eXtraction of ENTity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl >= 5.0
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-statmod 

%description
Provides a tool for extracting information (entities and relations between
them) in text datasets. It also emphasizes the results exploration with
graphical displays. It is a rule-based system and works with hand-made
dictionaries and local grammars defined by users. 'x.ent' uses parsing
with Perl functions and JavaScript to define user preferences through a
browser and R to display and support analysis of the results extracted.
Local grammars are defined and compiled with the tool Unitex, a tool
developed by University Paris Est that supports multiple languages. See
?xconfig for an introduction.

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
%doc %{rlibdir}/%{packname}/corpus
%doc %{rlibdir}/%{packname}/dico
%doc %{rlibdir}/%{packname}/eval
%doc %{rlibdir}/%{packname}/out
%doc %{rlibdir}/%{packname}/Perl
%doc %{rlibdir}/%{packname}/Unitex
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
