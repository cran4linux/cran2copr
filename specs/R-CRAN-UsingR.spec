%global packname  UsingR
%global packver   2.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          2%{?dist}
Summary:          Data Sets, Etc. for the Text "Using R for IntroductoryStatistics", Second Edition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-HistData 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-MASS 
Requires:         R-CRAN-HistData 
Requires:         R-CRAN-Hmisc 

%description
A collection of data sets to accompany the textbook "Using R for
Introductory Statistics," second edition.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/answers
%doc %{rlibdir}/%{packname}/errata
%doc %{rlibdir}/%{packname}/samplecode
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/tsEx
%{rlibdir}/%{packname}/INDEX
