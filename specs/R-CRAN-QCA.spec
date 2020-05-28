%global packname  QCA
%global packver   3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.8
Release:          1%{?dist}
Summary:          Qualitative Comparative Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-admisc >= 0.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-venn 
Requires:         R-CRAN-admisc >= 0.8
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-venn 

%description
An extensive set of functions to perform Qualitative Comparative Analysis:
crisp sets ('csQCA'), temporal ('tQCA'), multi-value ('mvQCA') and fuzzy
sets ('fsQCA'), using a GUI - graphical user interface. 'QCA' is a
methodology that bridges the qualitative and quantitative divide in social
science research. It uses a Boolean algorithm that results in a minimal
causal combination that explains a given phenomenon.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/gui
%doc %{rlibdir}/%{packname}/staticdocs
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
