%global packname  FuzzyR
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}
Summary:          Fuzzy Logic Toolkit for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grid 
Requires:         R-splines 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plyr 
Requires:         R-grid 

%description
Design and simulate fuzzy logic systems using Type-1 and Interval Type-2
Fuzzy Logic. This toolkit includes with graphical user interface (GUI) and
an adaptive neuro- fuzzy inference system (ANFIS). This toolkit is a
continuation from the previous package ('FuzzyToolkitUoN'). Produced by
the Intelligent Modelling & Analysis Group (IMA) and Lab for UnCertainty
In Data and decision making (LUCID), University of Nottingham.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
