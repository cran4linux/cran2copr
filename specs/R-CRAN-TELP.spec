%global __brp_check_rpaths %{nil}
%global packname  TELP
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Social Representation Theory Application: The Free Evocation ofWords Technique

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-arulesViz 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-arulesViz 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Using The Free Evocation of Words Technique method with some functions,
this package will make a social representation and other analysis. The
Free Evocation of Words Technique consists of collecting a number of words
evoked by a subject facing exposure to an inducer term. The purpose of
this technique is to understand the relationships created between words
evoked by the individual and the inducer term. This technique is included
in the theory of social representations, therefore, on the information
transmitted by an individual, seeks to create a profile that define a
social group.

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
%{rlibdir}/%{packname}/INDEX
