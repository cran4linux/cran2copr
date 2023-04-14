%global __brp_check_rpaths %{nil}
%global packname  PreKnitPostHTMLRender
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Pre-Knitting Processing and Post HTML-Rendering Processing

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc >= 1.12.3
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.4
BuildRequires:    R-CRAN-knitr >= 1.13
BuildRequires:    R-CRAN-rmarkdown >= 0.9.6
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-XML >= 3.98.1.4
Requires:         R-CRAN-knitr >= 1.13
Requires:         R-CRAN-rmarkdown >= 0.9.6
Requires:         R-utils 
Requires:         R-tools 

%description
Dynamize headers or R code within 'Rmd' files to prevent proliferation of
'Rmd' files for similar reports. Add in external HTML document within
'rmarkdown' rendered HTML doc.

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
