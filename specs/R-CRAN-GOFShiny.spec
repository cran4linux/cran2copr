%global __brp_check_rpaths %{nil}
%global packname  GOFShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Document for Working with Goodness of Fit Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rhandsontable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-CRAN-rhandsontable 

%description
An interactive document on the topic of goodness of fit analysis using
'rmarkdown' and 'shiny' packages. Runtime examples are provided in the
package function as well as at
<https://predanalyticssessions1.shinyapps.io/ChiSquareGOF/>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
