%global packname  Deducer
%global packver   0.7-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.9
Release:          1%{?dist}
Summary:          A Data Analysis GUI for R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-JGR >= 1.7.10
BuildRequires:    R-CRAN-car 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-effects 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-JGR >= 1.7.10
Requires:         R-CRAN-car 
Requires:         R-MASS 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plyr 
Requires:         R-foreign 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-effects 

%description
An intuitive, cross-platform graphical data analysis system. It uses menus
and dialogs to guide the user efficiently through the data manipulation
and analysis process, and has an excel like spreadsheet for easy data
frame visualization and editing. Deducer works best when used with the
Java based R GUI JGR, but the dialogs can be called from the command line.
Dialogs have also been integrated into the Windows Rgui.

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
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
