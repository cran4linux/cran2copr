%global packname  MOQA
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Basic Quality Data Assurance for Epidemiological Research

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-gplots 
Requires:         R-grid 
Requires:         R-CRAN-readr 

%description
With the provision of several tools and templates the MOSAIC project
(DFG-Grant Number HO 1937/2-1) supports the implementation of a central
data management in epidemiological research projects. The 'MOQA' package
enables epidemiologists with none or low experience in R to generate basic
data quality reports for a wide range of application scenarios. See
<https://mosaic-greifswald.de/> for more information. Please read and cite
the corresponding open access publication (using the former package-name)
in METHODS OF INFORMATION IN MEDICINE by M. Bialke, H. Rau, T.
Schwaneberg, R. Walk, T. Bahls and W. Hoffmann (2017)
<doi:10.3414/ME16-01-0123>.
<https://methods.schattauer.de/en/contents/most-recent-articles/issue/2483/issue/special/manuscript/27573/show.html>.

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
