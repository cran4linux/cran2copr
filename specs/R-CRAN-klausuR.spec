%global packname  klausuR
%global packver   0.12-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.10
Release:          2%{?dist}
Summary:          Multiple Choice Test Evaluation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-psychometric 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-psychometric 
Requires:         R-CRAN-polycor 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-tools 

%description
A set of functions designed to quickly generate results of a multiple
choice test. Generates detailed global results, lists for anonymous
feedback and personalised result feedback (in LaTeX and/or PDF format), as
well as item statistics like Cronbach's alpha or disciminatory power.
klausuR also includes a plugin for the R GUI and IDE RKWard, providing
dialogs for its basic features. To use them, install RKWard from
http://rkward.sf.net (plugins are detected automatically). Due to some
restrictions on CRAN, the full package sources are only available from the
project homepage.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/rkward
%{rlibdir}/%{packname}/INDEX
