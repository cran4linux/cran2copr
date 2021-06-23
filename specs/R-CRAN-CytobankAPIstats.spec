%global __brp_check_rpaths %{nil}
%global packname  CytobankAPIstats
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Computes Signaling and Population Stats for Cytometry Data onCytobank using 'CytobankAPI'

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CytobankAPI 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-pheatmap 
Requires:         R-CRAN-CytobankAPI 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-pheatmap 

%description
Tools to process cytometry data from Cytobank into easily usable form for
analysis of populations, markers, and signaling using the 'CytobankAPI'
package. Learn more about Cytobank at <https://www.cytobank.org>. For more
information about types of cytometry data that can be analyzed, please
see: Bendall, S. C., Simonds, E. F., Qiu, P., Amir, E. D., Krutzik, P. O.,
Finck, R.,... Nolan, G. P. (2011) <doi:10.1126/science.1198704> and Adan,
A., Alizada, G., Kiraz, Y., Baran, Y., Nalbant, A. (2017).
<doi:10.3109/07388551.2015.1128876>.

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
