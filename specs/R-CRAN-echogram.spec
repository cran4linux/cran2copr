%global packname  echogram
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Echogram Visualisation and Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-readHAC 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-readHAC 

%description
Easily import multi-frequency acoustic data stored in 'HAC' files (see
<http://biblio.uqar.ca/archives/30005500.pdf> for more information on the
format), and produce echogram visualisations with predefined or customized
color palettes. It is also possible to merge consecutive echograms; mask
or delete unwanted echogram areas; model and subtract background noise;
and more important, develop, test and interpret different combinations of
frequencies in order to perform acoustic filtering of the echogram's data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/hac
%{rlibdir}/%{packname}/INDEX
